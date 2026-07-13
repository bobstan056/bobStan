# Deutsche Spracherkennung mit Vosk

Ein einfaches Python-Projekt zur **Offline-Spracherkennung** mit der Vosk-Bibliothek.

Das Programm liest eine `.wav`-Datei und wandelt gesprochene deutsche Sprache in Text um.

---

## Funktionen

- Offline-Spracherkennung
- Unterstützung der deutschen Sprache
- Verarbeitung von WAV-Dateien
- Schnelles und leichtgewichtiges Vosk-Modell

---

## Technologien

- Python 3.11
- Vosk
- Wave
- JSON

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
└── testSpeech.wav

```

---

## Verwendung

Programm starten:

```bash
python transcriber.py
```

---

## Projektstruktur

```

speech_to_text/
│
├── transcriber.py        # Logik der Spracherkennung
├── testSpeech.wav        # Beispieldatei
├── README.md
└── model/                # Separat herunterladen

```

---

## Beispielausgabe

```

guten tag ich heiße thomas ich wohne in zürich heute ist das wetter sehr schön ich lerne deutsch und programmiere in python

```

---

## Hinweise

- Unterstützt werden ausschließlich `.wav`-Dateien.
- Das Modell muss vor dem ersten Start heruntergeladen werden.