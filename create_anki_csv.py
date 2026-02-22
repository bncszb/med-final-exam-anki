import json
import csv
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel
from models import Question

class ChapterOutput(BaseModel):
    name: str
    questions: List[Question]

class GroupOutput(BaseModel):
    name: str
    chapters: Optional[List[ChapterOutput]] = None
    questions: Optional[List[Question]] = None


def main():
    with open("output/output.json", "r") as f:
        data = json.load(f)
    
    groups = [GroupOutput(**group_data) for group_data in data]

    rows = []
    # Header for the CSV file
    rows.append(["Question", "Answer", "Deck"])

    for group in groups:
        group_name = group.name
        if group.chapters:
            for chapter in group.chapters:
                chapter_name = chapter.name
                deck_name = f"Orvosi ZV::{group_name}::{chapter_name}"
                for question in chapter.questions:
                    row = create_csv_row(question, deck_name)
                    if row:
                        rows.append(row)
        elif group.questions:
            deck_name = f"Orvosi ZV::{group_name}"
            for question in group.questions:
                row = create_csv_row(question, deck_name)
                if row:
                    rows.append(row)

    Path("output").mkdir(exist_ok=True)
    with open("output/orvosi_zv.csv", "w", newline="") as f:
        print("#deck column:3", file=f)
        writer = csv.writer(f, delimiter=";")
        writer.writerows(rows)

    print("Anki CSV created successfully at output/orvosi_zv.csv")


def create_csv_row(question: Question, deck_name: str) -> Optional[List[str]]:
    question_field = ""
    answer_field = ""

    if question.task_type_id in [1, 2, 6, 7]:  # Regular question types
        question_text = question.description_plain_text
        answers = question.answers
        if not answers:
            return None

        possible_answers = "<br>".join(
            [f"{ans.letter}) {ans.text_plain_text}" for ans in answers]
        )
        question_field = f"{question_text}<br><br>{possible_answers}"

        correct_answer = next((ans for ans in answers if ans.is_correct), None)
        if not correct_answer:
            return None

        answer_field = (
            f"A helyes válasz: {correct_answer.letter}) {correct_answer.text_plain_text}"
        )
        if correct_answer.explanation:
            answer_field += f"<br><br><b>Magyarázat:</b><br>{correct_answer.explanation}"

    elif question.task_type_id == 3:  # Pairing question type
        association = question.association
        if not association:
            return None

        question_field = association.description_plain_text
        
        pairs = []
        for item in association.items:
             pairs.append(f"{item.letter}) {item.text_plain_text}")

        question_field += "<br><br>" + "<br>".join(pairs)
        
        answer_field = ""
        if question.explanation:
            answer_field = f"<b>Magyarázat:</b><br>{question.explanation}"

    if question_field and answer_field:
        return [question_field, answer_field, deck_name]
    else:
        return None


if __name__ == "__main__":
    main()
