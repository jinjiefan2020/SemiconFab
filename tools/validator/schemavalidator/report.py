from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ValidationError:
    field_path: str
    message_en: str
    message_zh: str
    rule: str

    def to_dict(self, lang: str = "en") -> Dict[str, Any]:
        return {
            "field_path": self.field_path,
            "message": self.message_zh if lang == "zh" else self.message_en,
            "message_en": self.message_en,
            "message_zh": self.message_zh,
            "rule": self.rule,
        }

    def __str__(self) -> str:
        return f"[{self.field_path}] {self.message_en} (rule: {self.rule})"


@dataclass
class ValidationWarning:
    field_path: str
    message_en: str
    message_zh: str
    rule: str

    def to_dict(self, lang: str = "en") -> Dict[str, Any]:
        return {
            "field_path": self.field_path,
            "message": self.message_zh if lang == "zh" else self.message_en,
            "message_en": self.message_en,
            "message_zh": self.message_zh,
            "rule": self.rule,
        }

    def __str__(self) -> str:
        return f"[WARNING: {self.field_path}] {self.message_en} (rule: {self.rule})"


@dataclass
class ValidationReport:
    is_valid: bool
    errors: List[ValidationError] = field(default_factory=list)
    warnings: List[ValidationWarning] = field(default_factory=list)
    conformance_detected: Optional[str] = None
    conformance_target: Optional[str] = None
    summary_en: str = ""
    summary_zh: str = ""

    def summary(self, lang: str = "en") -> str:
        return self.summary_zh if lang == "zh" else self.summary_en

    def format_report(self, lang: str = "en") -> str:
        is_zh = lang == "zh"
        lines = []
        status_text = (
            ("✅ 校验通过" if self.is_valid else "❌ 校验失败")
            if is_zh
            else ("✅ VALID" if self.is_valid else "❌ INVALID")
        )
        lines.append(f"Status: {status_text}")
        lines.append(f"Summary: {self.summary(lang)}")
        if self.conformance_target:
            tgt_label = "Target Conformance" if not is_zh else "目标合规等级"
            lines.append(f"{tgt_label}: {self.conformance_target}")
        if self.conformance_detected:
            det_label = "Detected Conformance" if not is_zh else "实际达标等级"
            lines.append(f"{det_label}: {self.conformance_detected}")

        if self.errors:
            err_title = "Errors:" if not is_zh else "错误列表:"
            lines.append(f"\n{err_title} ({len(self.errors)})")
            for i, err in enumerate(self.errors, 1):
                msg = err.message_zh if is_zh else err.message_en
                lines.append(f"  {i}. [{err.field_path}] {msg} (rule: {err.rule})")

        if self.warnings:
            warn_title = "Warnings:" if not is_zh else "告警列表:"
            lines.append(f"\n{warn_title} ({len(self.warnings)})")
            for i, warn in enumerate(self.warnings, 1):
                msg = warn.message_zh if is_zh else warn.message_en
                lines.append(f"  {i}. [{warn.field_path}] {msg} (rule: {warn.rule})")

        return "\n".join(lines)
