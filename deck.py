import csv
import genanki
import io
import random


def create_anki_deck_from_csv(csv_text, deck_name, output_filepath, delimiter=','):
    """Create an Anki deck from CSV text and write it to ``output_filepath``."""
    deck_id = random.randrange(1 << 30, 1 << 31)
    model_id = random.randrange(1 << 30, 1 << 31)

    deck = genanki.Deck(deck_id, deck_name)

    model = genanki.Model(
        model_id,
        'Simple Model',
        fields=[{'name': 'Front'}, {'name': 'Back'}],
        templates=[{
            'name': 'Card 1',
            'qfmt': '{{Front}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Back}}',
        }]
    )

    csvfile = io.StringIO(csv_text.strip())
    reader = csv.DictReader(csvfile, delimiter=delimiter, skipinitialspace=True)
    if reader.fieldnames != ['Front', 'Back']:
        raise ValueError("CSV headers must be 'Front' and 'Back'.")

    for row in reader:
        note = genanki.Note(model=model, fields=[row['Front'], row['Back']])
        deck.add_note(note)

    genanki.Package(deck).write_to_file(output_filepath)
