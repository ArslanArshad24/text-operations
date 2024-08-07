from deep_translator import GoogleTranslator
from langdetect import detect , detect_langs

while True:
    sent = input('Enter Sentence ==> ')
    lang_detect = detect(text=sent)
    prob1= detect_langs(sent)

    print(prob1)
    print(lang_detect , sent)

    translated_sent = GoogleTranslator(source='auto', target='hi').translate(sent)
    langTranslated = detect(translated_sent)
    prob2= detect_langs(translated_sent)

    print(prob2)
    print(langTranslated , translated_sent)
