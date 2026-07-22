
from vosk import Model, KaldiRecognizer
import wave
import json
from analyzer import count_words, count_sentences, top_words
from database.database import (
    init_db,
    save_transcription,
    get_all,
)


def transcribe(filepath, model_path="model/vosk-model-small-de-0.15"):
    model = Model(model_path)
    with wave.open(filepath, "rb") as wf:
        recognizer = KaldiRecognizer(model, wf.getframerate())

        result_text = ""

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                result_text += result.get("text", "") + " "
        final_result = json.loads(recognizer.FinalResult())
        result_text += final_result.get("text", "")
        return result_text


def transcribe_and_analyze(filepath, model_path="model/vosk-model-small-de-0.15"):
    text = transcribe(filepath, model_path)
    words = count_words(text)
    sentences = count_sentences(text)
    print(f"\nTranskription:\n{text}")
    print(f"\nWörter:  {count_words(text)}")
    print(f"Sätze:   {count_sentences(text)}")
    print("\nTop-Wörter:")
    for word, count in top_words(text, 5):
        print(f"  {word}: {count}")

    init_db()
    save_transcription(filepath, text, words, sentences)
    print("\n✓ Gespeichert in transcriptions.db")

    print("\n--- Historie ---")
    for row in get_all():
        print(f"  [{row[0]}] {row[1]} | {row[3]} Wörter | {row[5][:10]}")


transcribe_and_analyze("testSpeech6.wav")
