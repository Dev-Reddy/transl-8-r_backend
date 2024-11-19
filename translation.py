import json
import google.generativeai as genai

# from GEMINI_API_KEY import GEMINI_API_KEY
import dotenv
import os

dotenv.load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def translate_text(transcript, source_language, target_language):
    response = model.generate_content(
        f"Translate this audio transcript from {source_language} to {target_language}. There may be some words misspelled or missing in the transcript. Fill them based on the context using your AI capabilities. Ignore grammatical errors and correct them. ignore typos and fit in the closest word resembling the typo .Give me only the translated paragraph as a string. Do not include any other information in the response. This is the paragraph to be translated: {transcript}."
    )
    print("transcript in translate_text", transcript)
    print("source_language in translate_text", source_language)
    print("target_language in translate_text", target_language)
    print(response.text)
    return response.text
    # if "text" in response:
    #     print("response.text in translate_text:", response["text"])
    #     return response["text"]
    # else:
    #     # Log the full response for debugging
    #     print(f"Response: {response}")  # Log the full response for debugging
    #     # Determine the reason for the failure
    #     reason = (
    #         "The translation cannot be completed as the speech contains content which is hateful, "
    #         "harmful, dangerous, or sexually explicit."
    #     )
    #     return reason
