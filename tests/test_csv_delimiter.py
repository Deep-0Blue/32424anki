import os
import tempfile

import pytest

genanki = pytest.importorskip('genanki')

from deck import create_anki_deck_from_csv


def test_create_deck_with_custom_delimiter():
    csv_text = 'Front;Back\nQ1;A1\nQ2;A2'
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        path = tmp.name
    try:
        create_anki_deck_from_csv(csv_text, 'Deck', path, delimiter=';')
        assert os.path.getsize(path) > 0
    finally:
        if os.path.exists(path):
            os.remove(path)

