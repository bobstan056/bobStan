# German Speech-to-Text using Vosk

A simple Python project that performs **offline German speech recognition** using the Vosk speech recognition toolkit.

The program reads a `.wav` audio file and converts spoken German into text.

---

## Features

- Offline speech recognition
- German language support
- WAV audio processing
- Fast and lightweight Vosk model

---

## Technologies

- Python 3.11
- Vosk
- Wave
- JSON

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your_username/speech_to_text.git
cd speech_to_text
```

Install the required packages:
  
```bash
pip install -r requirements.txt
```

---

## Download the Vosk model

The speech recognition model is not included in this repository because of its size.

Download it here:

https://alphacephei.com/vosk/models/vosk-model-small-de-0.15.zip

Extract the archive into the project folder so the structure becomes:

```

speech_to_text/
│
├── model/
│   └── vosk-model-small-de-0.15/
├── transcriber.py
└── testSpeech.wav

```

---

## Usage

Run:

```bash
python transcriber.py
```

The program will transcribe the provided `testSpeech.wav` file.

---

## Project structure

```

speech_to_text/
│
├── transcriber.py        # Speech recognition logic
├── testSpeech.wav        # Sample audio file
├── README.md
└── model/                # Download separately

```

---

## Example output

```

guten tag ich heiße thomas ich wohne in zürich heute ist das wetter sehr schön ich lerne deutsch und programmiere in python

```

---

## Notes

- Only `.wav` audio files are supported.
- The model must be downloaded manually before running the project.