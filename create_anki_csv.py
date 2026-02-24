import json
import csv
from pathlib import Path
from models import GroupOutput
from utils import process_question_list


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


if __name__ == "__main__":
    main()
