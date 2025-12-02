# validation/research_rules.py
"""
Validations for research/publication-related fields (SPPU Table 2).
Expected example:
{
  "journal_papers": 3,
  "conference_papers": 2,
  "book_international": 1,
  "book_national": 0,
  "patents_national": 0,
  "patents_international": 0,
  ...
}
"""

from typing import Dict, Tuple
from .global_rules import is_non_negative_int


# Allowed research keys - extend as required by your PBAS mapping
ALLOWED_KEYS = {
    "journal_papers",
    "conference_papers",
    "book_international",
    "book_national",
    "patents_national",
    "patents_international",
    "chapters",
    "moocs_completed",
    "guidance_phd_completed",
    "guidance_mtech_completed",
}


def validate_research_payload(payload: Dict) -> Tuple[bool, str]:
    if not isinstance(payload, dict):
        return False, "Research payload must be a JSON object."

    for k, v in payload.items():
        if k not in ALLOWED_KEYS:
            return False, f"Unknown research field '{k}'. Allowed fields: {sorted(ALLOWED_KEYS)}"
        if not is_non_negative_int(v):
            return False, f"Research field '{k}' must be a non-negative integer."

    # One small sanity check: if nothing is supplied, return False (require at least one field)
    if len(payload) == 0:
        return False, "At least one research field must be provided."

    return True, ""
