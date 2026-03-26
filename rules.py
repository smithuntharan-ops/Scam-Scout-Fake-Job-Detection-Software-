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
            suggestions=(
                "Be skeptical of hiring processes that bypass interviews and standard checks.",
                "Research the company and look for consistent employment signals (team, location, benefits).",
            ),
            keywords=("instant offer", "guaranteed job", "no experience required"),
        ),
        Rule(
            rule_id="too_good_to_be_true",
            title="Unrealistic promises",
            description="Overly positive guarantees like '100%' or 'risk-free' can indicate scams.",
            points=10,
            patterns=(
                r"\b100\s*%\b",
                r"\brisk[-\s]*free\b",
                r"\bhigh\s*income\b",
                r"\bguaranteed\s*income\b",
                r"\boutstanding\s*pay\b",
            ),
            suggestions=("Treat extreme guarantees as a red flag; verify compensation and requirements.",),
            keywords=("100%", "risk-free", "guaranteed income"),
        ),
        Rule(
            rule_id="work_from_home_no_experience",
            title="Remote + no experience angle",
            description="A common scam pattern is remote work plus claims of needing no experience.",
            points=13,
            patterns=(
                r"\bwork\s*from\s*home\b",
                r"\bremote\b",
                r"\bno\s*experience\b",
                r"\btrain\s*you\b",
            ),
            suggestions=(
                "Remote jobs can be real, but scams often bundle 'no experience' and rapid onboarding.",
            ),
            keywords=("work from home", "remote", "no experience"),
        ),
        Rule(
            rule_id="unusual_salary_bands",
            title="Suspicious compensation wording",
            description="Certain salary formats and unusually broad numbers can correlate with scams.",
            points=14,
            patterns=(
                r"(?:\bcompensation\b|\bsalary\b).{0,40}\$\s?\d{2,3}(?:[,\d]{0,3})+(?:\s*(?:/)?\s*(?:month|year|week))?",
                r"\$\s?\d{2,3}(?:[,\d]{0,3})\s*(?:/)?\s*(?:month|year|week)",
                r"\b(?:earn|income)\s*\$\s?\d{2,3}(?:[,\d]{0,3})\b",
            ),
            suggestions=("Confirm salary ranges and tax/benefits details with the employer’s official HR contact.",),
            keywords=("salary", "compensation", "earn $"),
        ),
        Rule(
            rule_id="training_or_course_fee",
            title="Pays for training / course fees",
            description="Scams may ask candidates to pay for training, onboarding, or materials before employment.",
            points=20,
            patterns=(
                r"\btraining\s*fee\b",
                r"\bcourse\s*fee\b",
                r"\bpay\s*for\s*training\b",
                r"\bpay\s*to\s*start\b",
                r"\bmaterials\s*fee\b",
                r"\bonboarding\s*fee\b",
            ),
            suggestions=("Legitimate training is normally paid by the employer; avoid paying fees to start.",),
            keywords=("training fee", "course fee", "materials fee"),
        ),
        Rule(
            rule_id="generic_email_domain",
            title="Generic or mismatched email",
            description="Legit companies usually use their own domain; generic inboxes can be a warning signal.",
            points=7,
            patterns=(
                r"\b[\w\.-]+@(gmail|yahoo|outlook|hotmail)\.com\b",
                r"\bcontact@(gmail|yahoo|outlook|hotmail)\.com\b",
            ),
            suggestions=("Verify the sender and domain; look up the company’s official email format.",),
            keywords=("gmail.com", "outlook.com", "hotmail.com"),
        ),
    ]