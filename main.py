import json
from typing import List, Optional

import requests

from models import Question, TaskGroupResponse
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
    task_group_id: int,
    chapter_id: Optional[int] = None,
    offset: int = 0,
    limit: int = 20,
) -> List[Question]:
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
        task_groups = task_groups[1:2]

    for task_group in task_groups:
        if task_group.chapters:
            chapters = task_group.chapters
            if settings.TEST_RUN:
                chapters = chapters[:1]
            for chapter in chapters:
                count = get_questions_count(
                    # task_group_id=task_group.id,
                    chapter_id=chapter.id,
                )
                print(
                    f"Fetching {count} questions for {task_group.name} - {chapter.name}"
                )
                questions = get_questions(
                    task_group_id=task_group.id,
                    chapter_id=chapter.id,
                    limit=count,
                )
                print(questions)
        else:
            count = get_questions_count(task_group_id=task_group.id)
            print(f"Fetching {count} questions for {task_group.name}")
            questions = get_questions(task_group_id=task_group.id, limit=count)
            print(questions)


if __name__ == "__main__":
    main()
