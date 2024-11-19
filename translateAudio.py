import sys
from translation import translate_text  # Your translation logic
from speak import speak  # Function for generating audio
from transcriber import transcribe_audio


def translateAudio(audio_file, source_lang, dest_lang, unique_name, output_folder):

    # Step 1: Transcribe Audio
    print("Transcribing audio...")
    try:
        transcript = transcribe_audio(
            audio_file, source_lang
        )  # Pass source_lang as language_code
    except Exception as e:
        print("Transcription failed:", str(e))
        sys.exit(1)

    # Step 2: Translate the transcript
    print("Translating transcript...")
    try:
        translated_text = translate_text(transcript, source_lang, dest_lang)
    except Exception as e:
        print("Translation failed:", str(e))
        sys.exit(1)

    # Step 3: Convert translated text to speech and save it
    print("Generating translated audio...")
    try:
        translated_audio_path = speak(
            translated_text,
            lang=dest_lang,
            save_to_file=True,
            unique_name=unique_name,
            output_folder=output_folder,
        )
    except Exception as e:
        print("Speech synthesis failed:", str(e))
        sys.exit(1)

    # Return the path of the translated audio file to Node.js
    print("Translated audio file saved at:", translated_audio_path)
    return translated_audio_path
