from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

text1 = "Hey, what a beautiful day! What an amazing day!"
x = analyzer.polarity_scores(text1)

if analyzer.polarity_scores(text1)["compound"] > 0:
    print("Positive Text")
else:
    print("Negative Text")