# Deutscher Speech-to-Text Analyzer

Eine Python-Anwendung zur **Offline-Spracherkennung** mit anschließender Analyse des transkribierten Textes.

Das Programm wandelt gesprochene deutsche Sprache aus einer `.wav`-Datei in Text um und erstellt anschließend verschiedene Textstatistiken.

---

## Funktionen

- Offline-Spracherkennung
- Unterstützung von WAV-Dateien
- Automatische Textanalyse
- Wörter zählen
- Sätze zählen
- Die fünf häufigsten Wörter anzeigen
- Schnelles und leichtgewichtiges Vosk-Modell

---

## Technologien

- Python 3.11
- Vosk
- Wave
- JSON
- Reguläre Ausdrücke (re)

---

## Installation

Repository klonen:

```bash
git clone https://github.com/your_username/speech_to_text.git
cd speech_to_text
```

Benötigte Bibliotheken installieren:

```bash
pip install -r requirements.txt
```

---

## Vosk-Modell herunterladen

Das Sprachmodell ist aufgrund seiner Größe **nicht** im Repository enthalten.

Download:

https://alphacephei.com/vosk/models/vosk-model-small-de-0.15.zip

Das Archiv entpacken, sodass die Projektstruktur wie folgt aussieht:

```
speech_to_text/
│
├── model/
│   └── vosk-model-small-de-0.15/
├── transcriber.py
├── analyzer.py
└── testSpeech.wav
```

---

## Verwendung

Programm starten:

```bash
python transcriber.py
```

Die Anwendung:

1. Transkribiert die Audiodatei.
2. Zählt Wörter.
3. Zählt Sätze.
4. Zeigt die fünf häufigsten Wörter an.

---

## Projektstruktur

```
speech_to_text/
│
├── transcriber.py      # Spracherkennung
├── analyzer.py         # Textanalyse
├── testSpeech.wav      # Beispieldatei
├── model/              # Separat herunterladen
├── requirements.txt
└── README.md
```

---

## Beispielausgabe

```text
Transkription:

guten tag ich heiße thomas ich wohne in zürich heute ist das wetter sehr schön ich lerne deutsch und programmiere in python

Wörter: 16
Sätze: 2

Top-Wörter:
ich: 2
guten: 1
tag: 1
heute: 1
deutsch: 1
```

---

## Hinweise

- Es werden ausschließlich `.wav`-Dateien unterstützt.
- Das Vosk-Modell muss vor dem ersten Start heruntergeladen werden.
- Der Ordner `model` ist aufgrund seiner Größe nicht im Repository enthalten.