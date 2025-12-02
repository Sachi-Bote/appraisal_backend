from .teaching import calculate_teaching_score
from .activities import calculate_activity_score
from .research import calculate_research_score
from .pbas import calculate_pbas_score


def calculate_full_score(payload: dict) -> dict:
    """
    Input payload example:
    {
      "teaching": {...},
      "activities": {...},
      "research": {...},
      "pbas": {...}
    }
    """

    teaching_result = calculate_teaching_score(payload["teaching"])
    activity_result = calculate_activity_score(payload["activities"])
    research_result = calculate_research_score(payload["research"])
    pbas_result = calculate_pbas_score(payload["pbas"])

    total_score = (
        teaching_result["score"]
        + activity_result["score"]
        + research_result["total"]
        + pbas_result["total"]
    )

    return {
        "teaching": teaching_result,
        "activities": activity_result,
        "research": research_result,
        "pbas": pbas_result,
        "total_score": total_score,
    }


def research_guidance(
    PhD_degree_awarded,
    PhD_thesis_submitted,
    MPhil_or_PG_dissertation_awarded,
    research_consultancy,
    research_project_completed,
    research_project_ongoing,
    amount,
):
    score = 0
    if PhD_degree_awarded == 'Yes':
        score += 10
    if PhD_thesis_submitted == 'Yes':
        score += 5
    if MPhil_or_PG_dissertation_awarded == 'Yes':
        score += 2

    if research_consultancy == 'Yes':
        score += 3

    if research_project_completed == 'Yes':
        score += 10 if amount > 1000000 else 5

    if research_project_ongoing == 'Yes':
        score += 5 if amount > 1000000 else 2

    return score


def patents(patents_filed, policy_document, Awards_or_fellowship,
            international_level, national_level, state_level):
    score = 0

    if patents_filed == 'Yes':
        if international_level == 'Yes':
            score += 10
        if national_level == 'Yes':
            score += 7

    if policy_document == 'Yes':
        if national_level == 'Yes':
            score += 7
        if international_level == 'Yes':
            score += 10
        if state_level == 'Yes':
            score += 4

    if Awards_or_fellowship == 'Yes':
        if international_level == 'Yes':
            score += 7
        if national_level == 'Yes':
            score += 5

    return score


def presented_papers(presented, international_level_abroad,
                     national_level, state_level, international_level_india):
    score = 0
    if presented == 'Yes':
        if international_level_abroad == 'Yes':
            score += 7
        if national_level == 'Yes':
            score += 3
        if state_level == 'Yes':
            score += 2
        if international_level_india == 'Yes':
            score += 5

    return score


def pedagogy_creation(
    developed_innovative_pedagogy,
    designed_new_curriculum,
    MOOCs,
    complete_course_in_4_quadrants,
    content_writer,
    course_coordinator,
    per_lecture_moocs,
    e_content,
    editor_of_e_content,
    contributor,
    content_per_module,
):
    score = 0

    if developed_innovative_pedagogy == 'Yes':
        score += 5
    if designed_new_curriculum == 'Yes':
        score += 2

    if MOOCs == 'Yes':
        if complete_course_in_4_quadrants == 'Yes':
            score += 20
        if content_writer == 'Yes':
            score += 2
        if course_coordinator == 'Yes':
            score += 8
        if per_lecture_moocs == 'Yes':
            score += 5

    if e_content == 'Yes':
        if complete_course_in_4_quadrants == 'Yes':
            score += 12
        if editor_of_e_content == 'Yes':
            score += 10
        if contributor == 'Yes':
            score += 2
        if content_per_module == 'Yes':
            score += 5

    return score
