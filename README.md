# Medical Final Exam Anki Deck Generator

This project scrapes Hungarian medical final exam questions (Orvosi Záróvizsga) and converts them into an Anki-compatible CSV format.

## Features

- **Automated Scraping**: Fetches questions from the official source.
- **Anki Integration**: Generates a CSV file ready for import into Anki.
- **Categorization**: Organizes questions into decks based on chapters and topics.

## Supported Question Types

The tool currently handles the following question types:

1.  **Multiple Choice**: Standard questions with options A, B, C, D, E.
2.  **Pairing Questions (Párosítás)**: Questions where you match items from a list (e.g., A, B, C, D) to statements (1, 2, 3...).
3.  **Combination Questions**: Questions involving a set of statements (1, 2, 3, 4) and options that are combinations of these statements (e.g., "A: 1, 2, 3 are correct").

## Prerequisites

- Python 3.x
- `uv` (for dependency management and running scripts)

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Environment Configuration**:
    Create a `.env` file in the root directory and add your session ID (cookie):
    ```env
    SESSION_ID=your_session_id_here
    ```
    You can obtain the session ID by logging into the website and inspecting the cookies in your browser (look for `JSESSIONID` or similar).

## Usage

1.  **Scrape Questions**:
    Run the scraper to fetch questions and save them to `output/output.json`:
    ```bash
    uv run scrape.py
    ```

2.  **Generate Anki CSV**:
    Convert the scraped data into an Anki-compatible CSV file (`output/orvosi_zv.csv`):
    ```bash
    uv run create_anki_csv.py
    ```

## Importing into Anki

1.  Open Anki.
2.  Go to **File** > **Import...**
3.  Select the generated file: `output/orvosi_zv.csv`.
4.  Configure the import settings:
    - **Field separator**: Semicolon (`;`)
    - **Deck**: The file contains deck information in the 3rd column. Ensure "Deck" is mapped correctly if not automatically detected.
    - **Allow HTML in fields**: Checked (the questions contain HTML formatting).
5.  Click **Import**.

## Project Structure

- `scrape.py`: Fetches questions from the API.
- `create_anki_csv.py`: Processes the JSON data and generates the CSV.
- `models.py`: Data models using Pydantic.
- `utils.py`: Helper functions for processing questions.
- `settings.py`: Configuration settings.
- `output/`: Directory where the JSON and CSV files are saved.
