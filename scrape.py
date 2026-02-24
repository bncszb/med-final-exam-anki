import json

import requests

from models import ChapterOutput, GroupOutput, Question, TaskGroupResponse
from settings import HEADERS, settings


def get_task_groups() -> TaskGroupResponse:
    url = f"{settings.API_URL}/feladatCsoportControl/findByGyujtemenyId"
    data = {"gyujtemenyId": settings.COLLECTION_ID}
    response = requests.post(url, headers=HEADERS, data=json.dumps(data))
    response.raise_for_status()
    return TaskGroupResponse(**response.json())


def get_questions_count(
    task_group_id: int | None = None, chapter_id: int | None = None
) -> int:
    url = f"{settings.API_URL}/kerdesControl/getGroupOrChapterQuestionsCount"
    data = {"feladatcsoport_id": task_group_id, "fejezet_id": chapter_id}
    response = requests.post(url, headers=HEADERS, data=json.dumps(data))
    response.raise_for_status()
    return response.json()["count"]


def get_questions(
    task_group_id: int | None = None,
    chapter_id: int | None = None,
    offset: int = 0,
    limit: int = 20,
) -> list[Question]:
    url = f"{settings.API_URL}/kerdesControl/getQuestionByLimit"
    data = {
        "feladatcsoport_id": task_group_id,
        "fejezet_id": chapter_id,
        "tol": offset,
        "darab": limit,
        "token": None,
    }
    response = requests.post(url, headers=HEADERS, data=json.dumps(data))
    response.raise_for_status()
    return [Question(**item) for item in response.json()]


def main():
    task_group_response = get_task_groups()
    task_groups = task_group_response.result.task_groups
    if settings.TEST_RUN:
        task_groups = task_groups[:2]

    output_data = []

    for task_group in task_groups:
        group_output = GroupOutput(name=task_group.name)
        if task_group.chapters:
            group_output.chapters = []
            chapters = task_group.chapters
            if settings.TEST_RUN:
                chapters = chapters[:1]
            for chapter in chapters:
                count = get_questions_count(
                    chapter_id=chapter.id,
                )
                print(
                    f"Fetching {count} questions for {task_group.name} - {chapter.name}"
                )
                questions = get_questions(
                    chapter_id=chapter.id,
                    limit=count,
                )
                chapter_output = ChapterOutput(
                    name=chapter.name,
                    questions=questions
                )
                group_output.chapters.append(chapter_output)
        else:
            count = get_questions_count(task_group_id=task_group.id)
            print(f"Fetching {count} questions for {task_group.name}")
            questions = get_questions(task_group_id=task_group.id, limit=count)
            group_output.questions = questions

        output_data.append(group_output.model_dump(by_alias=True))

    with open(settings.JSON_OUTPUT_PATH, "w") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
