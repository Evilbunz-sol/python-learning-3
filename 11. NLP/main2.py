import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemma = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ["n", "v", "a", "r"]:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemma.append(lemma)
    return sentence_lemma


l1 = lemma_me("vegetables are types of plants.")
l2 = lemma_me("a vegetable is a type of plant.")
print(l1, l2)