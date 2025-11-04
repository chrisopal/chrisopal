"""Template construction utilities for technical proposal sections."""
from __future__ import annotations

from typing import Iterable, List, Optional

from app.parse import Requirements, ScoringItem
from app.plugins import BasePlugin


def _format_scoring_items(items: Iterable[ScoringItem]) -> List[str]:
    bullet_points: List[str] = []
    for item in items:
        pieces = []
        if item.name:
            pieces.append(f"指标：{item.name}")
        if item.score is not None:
            pieces.append(f"分值：{item.score}")
        if item.detail:
            pieces.append(f"要求：{item.detail}")
        if item.line:
            pieces.append(f"原文：{item.line}")
        bullet_points.append("；".join(pieces))
    return bullet_points


def build_tech_sections(
    requirements: Requirements,
    brand: str,
    title: str,
    plugin: Optional[BasePlugin] = None,
) -> List[dict]:
    """Construct proposal sections ready for rendering."""

    sections: List[dict] = []
    plugin_terms = plugin.terms() if plugin else []
    plugin_kpis = plugin.kpis() if plugin else []
    plugin_risks = plugin.risks() if plugin else []

    sections.append(
        {
            "title": "概述",
            "content": (
                f"本技术标由{brand}团队针对《{title}》编制，围绕采购范围提供系统化解决方案。\n"
                f"项目范围摘要：\n{requirements.scope}\n"
                "我们将结合行业最佳实践与自研能力，确保项目可交付、可运营。"
            ),
        }
    )

    architecture_points = [
        "总体架构采用模块化设计，涵盖数据采集、处理、应用展示三大层。",
        "核心组件通过微服务与标准 API 互联，支持弹性扩展。",
        "安全体系包含身份认证、权限控制、日志审计与数据加密。",
    ]
    if plugin_terms:
        architecture_points.append("行业术语重点：" + "、".join(plugin_terms[:10]))

    sections.append(
        {
            "title": "架构设计",
            "content": "\n".join(architecture_points),
        }
    )

    implementation_points = [
        "实施采用敏捷里程碑，需求澄清—原型—开发—联调—验收五个阶段。",
        "设置联合项目管理办公室（PMO），每周例会、双周评审确保沟通透明。",
        "交付物覆盖项目计划、设计文档、测试报告、培训手册与运维指南。",
    ]
    if plugin_kpis:
        implementation_points.append("关键绩效指标（KPI）：" + ", ".join(plugin_kpis))

    sections.append(
        {
            "title": "实施计划",
            "content": "\n".join(implementation_points),
        }
    )

    scoring_bullets = _format_scoring_items(requirements.scoring.items)
    if not scoring_bullets:
        scoring_bullets.append("招标文件未给出明确评分细则，方案中将通过亮点设计主动对齐")

    sections.append(
        {
            "title": "评分对应策略",
            "content": "\n".join(
                [
                    f"目标总分：{requirements.scoring.total or '未明确'}",
                    "关键评分点对齐如下：",
                ]
                + scoring_bullets
            ),
        }
    )

    compliance_points = [
        "合规承诺：完全遵守国家与行业相关标准、法规与安全要求。",
        "资质保障：提供所需资质证书复印件，确保审查通过。",
        "风险控制：建立风险台账、预警机制与应急预案。",
    ]
    if plugin_risks:
        compliance_points.append("行业常见风险与对策：" + "; ".join(plugin_risks))
    if requirements.constraints.lines:
        compliance_points.append("RFP 约束条款响应：" + " | ".join(requirements.constraints.lines[:5]))

    sections.append(
        {
            "title": "合规与保障",
            "content": "\n".join(compliance_points),
        }
    )

    if plugin:
        sections.append(
            {
                "title": f"插件增强-{plugin.name}",
                "content": plugin.summary(requirements),
            }
        )

    return sections


__all__ = ["build_tech_sections"]
