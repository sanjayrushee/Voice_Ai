from googletrans import Translator
import pygame
from gtts import gTTS
from io import BytesIO


def translate_voice(inputText,which_lang):
   
        select_language = {
        "english": "en",
        "french": "fr",
        "spanish": "es",
        "german": "de",
        "italian": "it",
        "portuguese": "pt",
        "russian": "ru",
        "chinese (Simplified)": "zh-CN",
        "japanese": "ja",
        "korean": "ko",
        "arabic": "ar",
        "hindi": "hi",
        "bengali": "bn",
        "tamil": "ta",
        "telugu": "te",
        "urdu": "ur" }

        get_target_language = select_language[which_lang]
        translator = Translator()
        translation = translator.translate(inputText, dest=get_target_language)
        pygame.init()
        pygame.mixer.init()
        tts = gTTS(text=translation.text, lang=get_target_language, slow=False)
        speech_bytes = BytesIO()
        tts.write_to_fp(speech_bytes)
        speech_bytes.seek(0)
        pygame.mixer.music.load(speech_bytes)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.quit()
        print(translation.text)
        return translation.text

translate_voice("hello","tamil")