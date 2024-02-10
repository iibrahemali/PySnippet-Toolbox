from googletrans import Translator

def translate_text():
    translator = Translator()

    print("Welcome to the Python Translation Tool!")
    source_language = input("Enter the source language (e.g., 'en' for English): ")
    target_language = input("Enter the target language (e.g., 'es' for Spanish): ")

    while True:
        text_to_translate = input("Enter the text to translate (type 'exit' to quit): ")
        if text_to_translate.lower() == 'exit':
            break

        try:
            translation = translator.translate(text_to_translate, src=source_language, dest=target_language)
            print(f"Translation: {translation.text}")
        except Exception as e:
            print(f"Translation failed. Error: {e}")

if __name__ == "__main__":
    translate_text()
