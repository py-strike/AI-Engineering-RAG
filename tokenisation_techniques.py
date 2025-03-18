import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

text = "As the stars began to twinkle, the night felt peaceful and full of possibilities. Hi."

sentences = nltk.sent_tokenize(text)
print(f"the tokenized sentences are = {sentences}")


# Process the text : tokenization, only alphanumeric,lowercase, no stopwords
def process_text(text):
    processed_text = nltk.word_tokenize(text.lower())
    processed_text = [word for word in processed_text if word.isalnum()]
    processed_text = [
        word
        for word in processed_text
        if word not in nltk.corpus.stopwords.words("english")
    ]

    return processed_text


print(f"the tokenized words are = {process_text(text)}")
