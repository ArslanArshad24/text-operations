from better_profanity import profanity

if __name__ == "__main__":
    profanity.load_censor_words()
    text = "You p1ec3 of fuck and shit"
    censored_text = profanity.censor(text)    
    print(censored_text)

    if profanity.contains_profanity(text):
        print('Yes')
    #%%%%%%%%%%%%%%%%%% custom
    custom_badwords = ['bgyrat', 'Dur', 'off']
    profanity.load_censor_words(custom_words=custom_badwords)
    text2 = "You p1ec3 of fuck and shit dur  and    OFF"
    censored_text2 = profanity.censor(text2,'x')
    print(censored_text2)

