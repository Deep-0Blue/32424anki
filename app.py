# app.py

from flask import Flask, request, render_template, send_file, after_this_request
import os
import random

from deck import create_anki_deck_from_csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        deck_name = request.form.get('deck_name', 'My Anki Deck')
        csv_text = request.form.get('csv_text', '')
        delimiter = request.form.get('delimiter', ',') or ','

        if len(delimiter) != 1:
            return render_template(
                'index.html',
                error="Delimiter must be a single character.",
                deck_name=deck_name,
                csv_text=csv_text,
                delimiter=delimiter,
            )

        if not csv_text.strip():
            return render_template(
                'index.html',
                error="CSV text cannot be empty.",
                deck_name=deck_name,
                csv_text=csv_text,
                delimiter=delimiter,
            )

        # Generate a unique filename for the deck
        deck_filename = f"{deck_name.replace(' ', '_')}_{random.randint(1, 100000)}.apkg"
        deck_filepath = os.path.join('/tmp', deck_filename)

        # Create the deck
        try:
            create_anki_deck_from_csv(csv_text, deck_name, deck_filepath, delimiter)
        except Exception as e:
            return render_template(
                'index.html',
                error=f"An error occurred: {e}",
                deck_name=deck_name,
                csv_text=csv_text,
                delimiter=delimiter,
            )

        @after_this_request
        def remove_file(response):
            try:
                os.remove(deck_filepath)
            except Exception as error:
                app.logger.error(f"Error removing or closing downloaded file handle: {error}")
            return response

        return send_file(deck_filepath, as_attachment=True, download_name=deck_filename)

    return render_template('index.html', delimiter=',')

if __name__ == '__main__':
    app.run(debug=True)
