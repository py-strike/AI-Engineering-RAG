import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

text = "As the stars began to twinkle, the night felt peaceful and full of possibilities. Hi."

sentences = nltk.sent_tokenize(text)
print(f"the tokenized sentences are = {sentences}")


processed_text = nltk.word_tokenize(text.lower())
print(f"the tokenized words are = {processed_text}")

processed_text = [word for word in processed_text if word.isalnum()]
