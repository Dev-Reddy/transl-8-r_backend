import os
import random
import time
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import threading
from translateAudio import translateAudio

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "/tmp/uploads"  # Directory to temporarily save uploaded files
OUTPUT_FOLDER = "/tmp/output"  # Directory to save processed files
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_unique_filename(filename):
    """Generates a unique filename by appending the current timestamp and a random number."""
    name, ext = os.path.splitext(filename)
    unique_name = f"{name}_{int(time.time())}_{random.randint(1000, 9999)}{ext}"
    return unique_name


def delete_file_later(filepath, delay=5):
    """Deletes a file after a specified delay."""

    def delayed_delete():
        time.sleep(delay)
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"Deleted file: {filepath}")

    threading.Thread(target=delayed_delete).start()


@app.route("/")
def home():
    return "Hey!!! Whatcha doing here?"


@app.route("/translate", methods=["POST"])
def process_audio():
    try:
        # Check if required data is present
        if (
            "audio" not in request.files
            or "sourceLang" not in request.form
            or "destinationLang" not in request.form
        ):
            return jsonify({"error": "Missing required data"}), 400

        # Get the uploaded audio file and form data
        audio = request.files["audio"]
        source_lang = request.form["sourceLang"]
        destination_lang = request.form["destinationLang"]

        if audio.filename == "":
            return jsonify({"error": "No file selected"}), 400

        # Generate a unique filename and save the uploaded file
        unique_filename = generate_unique_filename(audio.filename)
        file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        audio.save(file_path)

        # Perform some operations on the file (e.g., translation, processing, etc.)
        # For demonstration, we'll just simulate creating a new audio file
        output_file = translateAudio(
            file_path, source_lang, destination_lang, unique_filename, OUTPUT_FOLDER
        )

        # Delete the uploaded file after processing
        os.remove(file_path)

        # Schedule the output file for deletion after sending it
        delete_file_later(output_file)

        # Return the processed file and a message
        return (
            send_file(
                output_file,
                as_attachment=True,
                download_name=f"{source_lang}_to_{destination_lang}_{unique_filename}",
            ),
            200,
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
