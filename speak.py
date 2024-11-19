from gtts import gTTS
import os


def speak(
    text,
    lang="en",
    tld="co.in",
    save_to_file=True,
    unique_name="temp.mp3",
    output_folder="output",
):
    tts = gTTS(text=text, lang=lang, tld=tld)
    if save_to_file:
        file_name = f"translated_{unique_name}"
        file_path = os.path.join(output_folder, file_name)
        tts.save(file_path)
        return file_path
    else:
        tts.save("temp.mp3")
        return "temp.mp3"
