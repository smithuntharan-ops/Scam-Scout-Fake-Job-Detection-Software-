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
        Rule(
            rule_id="telegram_or_whatsapp_only",
            title="Only contact via chat apps",
            description="Some fake postings push candidates to communicate via Telegram/WhatsApp/Signal instead of formal channels.",
            points=15,
            patterns=(
                r"\btelegram\b",
                r"\bwhatsapp\b",
                r"\bsignal\b",
                r"\btext\s+me\b",
                r"\bmessage\s+me\s+on\b",
            ),
            suggestions=(
                "Be cautious if the employer refuses standard application methods.",
                "Prefer official email domains and the company careers page.",
            ),
            keywords=("Telegram", "WhatsApp", "Signal", "text me"),
        ),
        Rule(
            rule_id="urgency_pressure",
            title="Urgency / pressure tactics",
            description="Scams often create deadlines to prevent verification.",
            points=12,
            patterns=(
                r"\burgent\b",
                r"\bimmediately\b",
                r"\bas\s*soon\s*as\s*possible\b",
                r"\btoday\b",
                r"\b24\s*/\s*7\b",
                r"\bacting\s+now\b",
            ),
            suggestions=("Take time to verify the posting; legitimate roles rarely require instant action.",),
            keywords=("urgent", "immediately", "as soon as possible"),
        ),
        Rule(
            rule_id="no_interview_or_instant_offer",
            title="No interview / instant offer",
            description="Some scams offer roles without screening or interviews.",
            points=18,
            patterns=(
                r"\bno\s*interview\b",
                r"\binstant\s*(offer|hire)\b",
                r"\boffer\s*letter\s*today\b",
                r"\bguaranteed\s*(job|employment)\b",
                r"\bno\s*experience\s*required\b",
            ),
        ),
    ]