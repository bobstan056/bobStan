import re


def count_lines(text):
    return (len(text.splitlines()))


def count_words(text):
    return len(text.split())


def count_sentences(text):
    sentences = [s.strip() for s in re.split("[?!.]+", text) if s.strip()]
    return len(sentences)


def top_words(text, n=10):
    words = {}
    for word in text.split():
        words[word] = words.get(word, 0) + 1
    sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]


def analyze(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
        print(f"Datei: {filepath}")
        print(f"Zeilen:    {count_lines(text)}")
        print(f"Wörter:    {count_words(text)}")
        print(f"Sätze:     {count_sentences(text)}")
        print(f"10 most used words are: {top_words(text, 10)}")


analyze("sample.txt")
