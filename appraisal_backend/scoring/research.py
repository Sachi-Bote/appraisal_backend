# scoring/research.py

POINTS = {
    "journal_papers": 8,
    "conference_papers": 5,
    "book_international": 12,
    "book_national": 10,
    "patents_national": 7,
    "patents_international": 10,
    "chapters": 5,
    "moocs_completed": 5,
    "guidance_phd_completed": 10,
    "guidance_mtech_completed": 5
}

def calculate_research_score(payload: dict) -> dict:
    """
    Input:
    {
      "journal_papers": 2,
      "conference_papers": 1,
      "book_international": 0,
      ...
    }
    """

    total = 0
    breakdown = {}

    for key, value in payload.items():
        pts = POINTS.get(key, 0)
        subtotal = value * pts
        breakdown[key] = subtotal
        total += subtotal

    return {
        "breakdown": breakdown,
        "total": total
    }
