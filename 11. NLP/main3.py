import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas

lemmatizer = WordNetLemmatizer()

text = "Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten raw or cooked."
question = "What are vegetables?"

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemma = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ["n", "v", "a", "r"]:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemma.append(lemma)
    return sentence_lemma

sentence_tokens = nltk.sent_tokenize(text)
sentence_tokens.append(question)

# print(sentence_tokens)

tv = TfidfVectorizer(tokenizer=lemma_me)
tf = tv.fit_transform(sentence_tokens)
# print(tf)

# Dataframe
df = pandas.DataFrame(tf.toarray(), columns=tv.get_feature_names_out())

# cosine similarity
values = cosine_similarity(tf[-1], tf)

# Index
index = values.argsort()[0][-2]

values_flat = values.flatten()
coeff = values_flat[-2]

if coeff > 0.3:
    print(sentence_tokens[index])