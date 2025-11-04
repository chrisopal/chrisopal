"""FastAPI application exposing BidWriter Agent services."""
from __future__ import annotations

import json
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import JSONResponse

from app.main import _load_rfp
from app.parse import Requirements, parse_rfp_text
from app.plugins import load_plugin
from app.render_docx import export_docx
from app.templates import build_tech_sections
from app.utils.io import write_json

app = FastAPI(title="BidWriter Agent", version="0.1.0")


def _requirements_to_dict(req: Requirements) -> Dict[str, Any]:
    return json.loads(req.json())


@app.post("/v1/parse")
async def parse_endpoint(
    request: Request,
    file: UploadFile | None = File(None),
    rfp_text: str | None = Form(None),
    use_llm: bool = Form(False),
) -> JSONResponse:
    """Parse RFP text or uploaded file."""

    try:
        if request.headers.get("content-type", "").startswith("application/json"):
            payload = await request.json()
            rfp_text = payload.get("rfp_text")
            use_llm = bool(payload.get("use_llm", False))
            if not rfp_text:
                raise ValueError("rfp_text is required in JSON payload")
        elif file is not None:
            suffix = Path(file.filename or "uploaded").suffix.lower()
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                data = await file.read()
                tmp.write(data)
                tmp_path = Path(tmp.name)
            rfp_text = _load_rfp(tmp_path)
            tmp_path.unlink(missing_ok=True)
        elif rfp_text is None:
            raise ValueError("Either rfp_text or file must be provided")

        requirements = parse_rfp_text(rfp_text, use_llm=use_llm)
        return JSONResponse(status_code=200, content=_requirements_to_dict(requirements))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail={"code": "bad_request", "message": str(exc)})
    except Exception as exc:  # pragma: no cover - unexpected
        raise HTTPException(status_code=500, detail={"code": "internal_error", "message": str(exc)})


class GeneratePayload(Requirements):
    brand: str
    title: str
    scene: Optional[str] = None


@app.post("/v1/generate")
async def generate_endpoint(payload: GeneratePayload) -> JSONResponse:
    try:
        plugin = load_plugin(payload.scene)
        requirements = Requirements(
            scope=payload.scope,
            scoring=payload.scoring,
            constraints=payload.constraints,
            sections=payload.sections,
        )
        if plugin:
            requirements = plugin.on_requirements(requirements)
        sections = build_tech_sections(requirements, brand=payload.brand, title=payload.title, plugin=plugin)
        outdir = Path("out/api")
        outdir.mkdir(parents=True, exist_ok=True)
        filename = f"bid_{datetime.now().strftime('%Y%m%d%H%M%S')}.docx"
        docx_path = outdir / filename
        export_docx(sections, docx_path, title=payload.title, brand=payload.brand)
        response = {
            "docx_path": str(docx_path),
            "report": {
                "sections": sections,
                "scene": payload.scene,
            },
        }
        return JSONResponse(status_code=200, content=response)
    except Exception as exc:  # pragma: no cover - unexpected
        raise HTTPException(status_code=500, detail={"code": "internal_error", "message": str(exc)})


@app.post("/v1/full")
async def full_endpoint(payload: Dict[str, Any]) -> JSONResponse:
    try:
        rfp_text = payload.get("rfp_text")
        if not rfp_text:
            raise ValueError("rfp_text is required")
        use_llm = bool(payload.get("use_llm", False))
        brand = payload.get("brand", "BidWriter")
        title = payload.get("title", "RFP Response")
        scene = payload.get("scene")

        requirements = parse_rfp_text(rfp_text, use_llm=use_llm)
        plugin = load_plugin(scene)
        if plugin:
            requirements = plugin.on_requirements(requirements)

        sections = build_tech_sections(requirements, brand=brand, title=title, plugin=plugin)
        outdir = Path("out/api_full")
        outdir.mkdir(parents=True, exist_ok=True)
        docx_path = outdir / f"bid_{datetime.now().strftime('%Y%m%d%H%M%S')}.docx"
        export_docx(sections, docx_path, title=title, brand=brand)
        requirements_path = outdir / "requirements.json"
        write_json(_requirements_to_dict(requirements), requirements_path)

        response = {
            "docx_path": str(docx_path),
            "artifacts_dir": str(outdir),
        }
        return JSONResponse(status_code=200, content=response)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail={"code": "bad_request", "message": str(exc)})
    except Exception as exc:  # pragma: no cover - unexpected
        raise HTTPException(status_code=500, detail={"code": "internal_error", "message": str(exc)})


__all__ = ["app"]
