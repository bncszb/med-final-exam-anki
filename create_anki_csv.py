import json
import csv
from pathlib import Path
from typing import List, Optional, Dict
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
                chapter_rows = process_question_list(chapter.questions, deck_name)
                rows.extend(chapter_rows)
                
        elif group.questions:
            deck_name = f"Orvosi ZV::{group_name}"
            group_rows = process_question_list(group.questions, deck_name)
            rows.extend(group_rows)

    Path("output").mkdir(exist_ok=True)
    with open("output/orvosi_zv.csv", "w", newline="") as f:
        print("#deck column:3", file=f)
        writer = csv.writer(f, delimiter=";")
        writer.writerows(rows)

    print("Anki CSV created successfully at output/orvosi_zv.csv")


def process_question_list(questions: List[Question], deck_name: str) -> List[List[str]]:
    rows = []
    processed_pairing_ids = set()

    # Pre-group pairing questions by association ID for efficiency
    pairing_groups: Dict[int, List[Question]] = {}
    for q in questions:
        if q.task_type_id == 3 and q.association:
            if q.association.id not in pairing_groups:
                pairing_groups[q.association.id] = []
            pairing_groups[q.association.id].append(q)

    for question in questions:
        if question.task_type_id in [1, 2, 6, 7]:  # Regular question types
            row = create_regular_question_row(question, deck_name)
            if row:
                rows.append(row)
        
        elif question.task_type_id == 3:  # Pairing question type
            if not question.association:
                continue
            
            assoc_id = question.association.id
            if assoc_id in processed_pairing_ids:
                continue
            
            processed_pairing_ids.add(assoc_id)
            group_questions = pairing_groups.get(assoc_id, [])
            
            if group_questions:
                row = create_pairing_question_row(group_questions, deck_name)
                if row:
                    rows.append(row)
                    
    return rows


def create_regular_question_row(question: Question, deck_name: str) -> Optional[List[str]]:
    question_field = ""
    answer_field = ""

    question_text = question.description_plain_text
    answers = question.answers
    if not answers:
        return None

    # Sort answers by letter (A, B, C...)
    answers = sorted(answers, key=lambda ans: ans.letter)

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

    if question_field and answer_field:
        return [question_field, answer_field, deck_name]
    else:
        return None


def create_pairing_question_row(questions: List[Question], deck_name: str) -> Optional[List[str]]:
    if not questions:
        return None
    
    # Sort questions by serial number to ensure consistent order
    sorted_questions = sorted(questions, key=lambda q: q.sorszam)
    first_q = sorted_questions[0]
    association = first_q.association
    
    if not association:
        return None

    # --- Question Field ---
    # 1. Description (Párosítsa össze!)
    question_parts = [association.description_plain_text]
    
    # 2. Options (A, B, C, D)
    sorted_items = sorted(association.items, key=lambda item: item.letter)
    for item in sorted_items:
        question_parts.append(f"{item.letter})\t{item.text_plain_text}")
    
    question_parts.append("") # Empty line separator
    
    # 3. Sub-questions (FOG - 45 - ...)
    for q in sorted_questions:
        question_parts.append(f"{q.serial_number} -\t{q.description_plain_text}")
        
    question_field = "<br>".join(question_parts)
    
    # --- Answer Field ---
    answer_parts = []
    
    # Map question IDs to correct answer letters
    q_id_to_letter = {}
    for item in association.items:
        for link in item.links:
            q_id_to_letter[link.question_id] = item.letter
            
    # 1. Answers for each sub-question
    for q in sorted_questions:
        correct_letter = q_id_to_letter.get(q.id, "?")
        answer_parts.append(f"{q.serial_number} -\t{q.description_plain_text}\t- {correct_letter})")
        
        # Add explanation immediately after the answer if it exists
        if q.explanation:
             answer_parts.append(f"<br>{q.explanation}<br>")
        
    answer_field = "<br>".join(answer_parts)

    if question_field and answer_field:
        return [question_field, answer_field, deck_name]
    else:
        return None


if __name__ == "__main__":
    main()
