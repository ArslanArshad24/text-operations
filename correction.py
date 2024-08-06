# %%%%%%%%%%%%%%% Singular Into Plural
from textblob import TextBlob

animals = TextBlob("cat dog octopus")
Plural_words = animals.words.pluralize()

print(Plural_words)

# %%%%%%%%%%%%%%% Spell Correction

b = TextBlob("I havv goood speling!")
print(b.correct())
