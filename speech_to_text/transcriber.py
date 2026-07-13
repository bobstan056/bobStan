import wave
import json
from vosk import Model, KaldiRecognizer


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
    pass


print(transcribe("testSpeech.wav"))
