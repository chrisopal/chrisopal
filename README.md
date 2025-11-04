# BidWriter Agent / 招投标智能体

## Overview / 项目概述
BidWriter Agent is an AI-assisted toolkit for parsing Requests for Proposal (RFP) documents and generating tailored technical proposals in DOCX format. It combines rule-based heuristics with optional LLM augmentation and exposes both CLI and REST API entry points.

BidWriter Agent 是一个面向招投标场景的智能体工具，可以解析 PDF/文本格式的招标文件，输出范围、评分、约束等结构化信息，并基于模板自动生成技术标文档。系统同时提供命令行与 REST API 接入方式，并支持可选的 LLM 增强能力。

## Features / 功能特性
- RFP parsing (text/PDF with OCR fallback) extracting scope, scoring, constraints, sections.
- DOCX technical proposal generation with configurable templates.
- CLI and FastAPI endpoints with shared business logic.
- Plugin hook for industry-specific enhancements (Smart Factory example included).
- Optional OpenAI integration for enhanced understanding when API key is provided.
- Quality tooling: Ruff, mypy, pytest and helper scripts.

## Quick Start / 快速开始
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.main --rfp sample_data/sample_rfp.txt --outdir out
```

```bash
# 启动 FastAPI
uvicorn app.api:app --port 8000 --reload
```

## Configuration / 配置
Environment variables 可配置项：
- `OPENAI_API_KEY` / `OPENAI_MODEL`
- `MAX_PAGES` (default 50)
- `LANG` (default zh)
- `TARGET_SCORE` (default 92)

## CLI Usage / 命令行用法
```bash
python -m app.main --rfp path/to/rfp.pdf --outdir out --brand ExampleCorp --title "智慧园区项目" --scene smart_factory
```

## API Usage / API 调用
```bash
curl -X POST http://127.0.0.1:8000/v1/parse \
  -H "Content-Type: application/json" \
  -d '{"rfp_text": "...", "use_llm": false}'

curl -X POST http://127.0.0.1:8000/v1/full \
  -H "Content-Type: application/json" \
  -d '{"rfp_text": "...", "brand": "ExampleCorp", "title": "智慧园区项目"}'
```

## Tests & Quality / 测试与质量
```bash
scripts/quality_check.sh
```

## Project Structure / 项目结构
```
app/
  main.py          # CLI entry point
  api.py           # FastAPI service
  config.py        # Environment configuration
  ocr.py           # PDF text extraction & OCR fallback
  parse.py         # Rule/LLM parsing logic
  templates.py     # Technical proposal template builder
  render_docx.py   # DOCX export
  table_parse.py   # Table extraction stub
  figures.py       # SVG generation stub
  plugins/         # Plugin examples
  utils/           # Logging & IO helpers
sample_data/       # Sample RFP documents
scripts/           # Helper scripts
```

## FAQ / 常见问题
**Q:** Do I need an OpenAI API key? / 是否必须提供 OpenAI API Key？  
**A:** No, rule-based parsing works offline. Provide `OPENAI_API_KEY` only if LLM augmentation is desired. / 否，内置规则解析即可运行，若需 LLM 增强再提供。

**Q:** How large is the generated DOCX? / 生成的 DOCX 大小是多少？  
**A:** The default sample produces a document larger than 10 KB with rich Chinese content. / 默认示例生成的文档大于 10 KB，包含多章节中文内容。

**Q:** Can I add new industry plugins? / 是否支持自定义行业插件？  
**A:** Yes, implement the `BasePlugin` protocol under `app/plugins/` and load it via `--scene` parameter. / 可以，在 `app/plugins/` 中实现 `BasePlugin` 接口，并通过 `--scene` 参数加载。
