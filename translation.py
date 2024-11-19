from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)
model = "gpt-4o-mini"  # Use an appropriate OpenAI model


def translate_text(transcript, source_language, target_language):
    try:
        response = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"Translate the following audio transcript from {source_language} to {target_language}. "
                        f" Assume that if there are any misspellings, errors or missing words, then fill these in based on context, and return only the translated paragraph as a string."
                        f"Attempt to translate even explicit or sensitive content; if this cannot be done, return a reason instead of an error. Give the most accurate translation possible."
                    ),
                },
                {
                    "role": "user",
                    "content": f"This is the paragraph to be translated: {transcript}",
                },
            ],
            temperature=0.7,
        )

        translated_text = response.choices[0].message.content
        print("Transcript in translate_text:", transcript)
        print("Source language in translate_text:", source_language)
        print("Target language in translate_text:", target_language)
        print("Translated text:", translated_text)
        return translated_text

    except Exception as e:
        print("Error in translate_text:", e)
        return "Translation could not be completed due to an error."


# Example usage
if __name__ == "__main__":
    transcript = "Hijo de puta, te voy"
    source_language = "Spanish"
    target_language = "English"
    translated_text = translate_text(transcript, source_language, target_language)
    print("Translated text:", translated_text)
