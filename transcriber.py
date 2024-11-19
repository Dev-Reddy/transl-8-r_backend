import assemblyai as aai
import dotenv
import os

dotenv.load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
transcriber = aai.Transcriber()


def transcribe_audio(audio_file, language_code):
    # Validate language code and select appropriate model
    if language_code in [
        "en",
        "es",
        "zh",
        "fr",
        "de",
        "hi",
        "it",
        "ja",
        "ko",
        "pt",
        "nl",
        "tr",
    ]:
        speech_model = aai.SpeechModel.best
    else:
        speech_model = aai.SpeechModel.nano

    config = aai.TranscriptionConfig(
        speech_model=speech_model, language_code=language_code
    )
    transcript = transcriber.transcribe(
        audio_file, config
    )  # Use dynamic audio file path
    if transcript.status == aai.TranscriptStatus.error:
        print(f"Transcription failed: {transcript.error}")
        exit(1)

    print("text", transcript.text)
    return transcript.text
