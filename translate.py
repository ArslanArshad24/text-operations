from deep_translator import GoogleTranslator
from langdetect import detect

while True:
    sent = input('Enter Sentence ==> ')

    lang_detect = detect(text=sent)
    translated_sent = GoogleTranslator(source='auto', target='hi').translate(sent)
    langTranslated = detect(translated_sent)

    print(lang_detect , sent)
    print(langTranslated , translated_sent)
