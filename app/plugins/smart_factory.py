"""Smart factory industry plugin."""
from __future__ import annotations

from typing import List

from app.parse import Requirements


class SmartFactoryPlugin:
    """Provide terminology and risk library for smart factory scenarios."""

    name = "Smart Factory"

    _TERMS = [
        "MES", "SCADA", "工业互联网", "数字孪生", "边缘计算", "工业大数据", "设备互联", "产线节拍",
        "OEE", "精益生产", "工艺追溯", "质量闭环", "预测性维护",
    ]
    _KPIS = [
        "OEE 提升 ≥ 10%", "良品率 ≥ 99%", "设备故障响应 < 5 分钟", "生产计划达成率 ≥ 98%",
    ]
    _RISKS = [
        "设备互联协议复杂导致集成延迟，设置协议适配层", "老旧设备改造风险，通过网关预评估",
        "数据安全合规风险，部署零信任访问与本地数据隔离", "上线后运维经验不足，提供7x24远程支持",
    ]

    def on_requirements(self, requirements: Requirements) -> Requirements:
        return requirements

    def terms(self) -> List[str]:
        return list(self._TERMS)

    def kpis(self) -> List[str]:
        return list(self._KPIS)

    def risks(self) -> List[str]:
        return list(self._RISKS)

    def summary(self, requirements: Requirements) -> str:
        return (
            "智能工厂场景重点突出数字化产线联动、数据治理与工业安全保障。"
            "方案将利用工业互联网平台整合设备数据，结合预测性维护与质量闭环体系，"
            "确保生产透明化与降本增效。"
        )


__all__ = ["SmartFactoryPlugin"]
