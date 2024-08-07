from pydictionary import Dictionary

while True:
    word = str(input('Enter a word: ' ))
    dict = Dictionary(word)

    meanings_list = dict.meanings()
    synonyms_list = dict.synonyms()
    antonyms_list = dict.antonyms()

    print(f'Meanings: {dict.print_meanings()}')
    print(f'Synonyms: {dict.print_synonyms()}')
    print(f'Antonyms: {dict.print_antonyms()}')



