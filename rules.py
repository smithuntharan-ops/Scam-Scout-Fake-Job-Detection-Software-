import re
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple


@dataclass(frozen=True)
class Rule:
    rule_id: str
    title: str
    description: str
    points: int
    patterns: Tuple[str, ...]
    suggestions: Tuple[str, ...] = ()
    keywords: Tuple[str, ...] = ()


def _compile_rules() -> List[Rule]:

    return [
        Rule(
            rule_id="gift_cards_or_wire",
            title="Upfront payments / gift cards",
            description="Scammers often request payment via gift cards, wire transfers, or similar methods.",
            points=25,
            patterns=(
                r"\bgift\s*cards?\b",
                r"\bwire\s*transfer\b",
                r"\bwestern\s*union\b",
                r"\bpay\s*pal\s*(friends|family)\b",
                r"\bcrypto(?!\s+trading)\b",
                r"\bcryptocurrency\b",
                r"\bbitcoin\b",
                r"\bbtc\b",
                r"\bbank\s*transfer\b",
                r"\bdeposit\s*to\b",
                r"\bprocessing\s*fee\b",
            ),
            suggestions=(
                "Never pay deposits or 'processing fees' to receive a job offer.",
                "Verify the employer and payment instructions via official channels.",
            ),
            keywords=("gift card", "wire transfer", "crypto", "processing fee", "bank transfer"),
        ),
    ]