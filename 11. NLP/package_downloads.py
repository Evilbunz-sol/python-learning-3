import nltk
import ssl

# Bypass SSL verification (optional if certificates are fixed)
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Downloads
# nltk.download("wordnet")
# nltk.download("averaged_perceptron_tagger")
# nltk.download("punkt_tab")
# nltk.download("averaged_perceptron_tagger_eng")
# nltk.download("vader_lexicon")
# nltk.download("twitter_samples")


