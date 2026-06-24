import re


def count_lines(text):
    return (len(text.splitlines()))


def count_words(text):
    return len(text.split())


def count_sentences(text):
    sentences = [s.strip() for s in re.split("[?!.]+", text) if s.strip()]
    return len(sentences)


def analyze(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
        print(f"Datei: {filepath}")
        print(f"Zeilen:    {count_lines(text)}")
        print(f"Wörter:    {count_words(text)}")
        print(f"Sätze:     {count_sentences(text)}")


analyze("sample.txt")
