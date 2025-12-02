# scoring/pbas.py

def calculate_pbas_score(payload: dict) -> dict:
    """
    Input:
    {
      "teaching_process": 20,
      "feedback": 22,
      "department": 15,
      "institute": 8,
      "acr": 8,
      "society": 6
    }
    """

    total = sum(payload.values())

    return {
        "breakdown": payload,
        "total": total
    }
