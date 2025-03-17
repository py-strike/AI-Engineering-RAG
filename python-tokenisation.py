import nltk

nltk.download("punkt")
nltk.download("punkt_tab")

text = [
    "The sun dipped below the horizon,",
    "casting a warm golden glow over the ocean.",
    "A gentle breeze rustled through the trees, ",
    "carrying the scent of salt and sand. ",
    "As the stars began to twinkle, the night felt peaceful and full of possibilities.",
]


def preprocessing(text):
    tokens = nltk.word_tokenize(text.lower())
    return [word for word in tokens if word.isalnum()]


preprocesses_doc = [" ".join(preprocessing(doc)) for doc in text]
print(preprocesses_doc)

# sentence_tokens = nltk.sent_tokenize(text)
# print("Sentence Tokens : ", sentence_tokens)
