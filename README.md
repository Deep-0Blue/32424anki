# Simple Model Deck Generator

This Flask application converts CSV text into an Anki `.apkg` deck. Each row of your CSV becomes a flashcard with the headers `Front` and `Back`.

## Installation

1. Clone the repository.
2. Install the Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the application:

```sh
python app.py
```

Open `http://localhost:5000` in your browser. Provide a deck name, paste your CSV data, choose the delimiter character, and click **Generate Deck** to download the resulting `.apkg` file.

## Example CSV

```csv
Front,Back
What is the capital of France?,Paris
What is 2+2?,4
```

