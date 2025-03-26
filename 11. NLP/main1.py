# Single Word Comparison
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

x = "was"
y = "is"

lemma1 = lemmatizer.lemmatize(x, "v", )
lemma2 = lemmatizer.lemmatize(y, "v", )
print(lemma1, lemma2)