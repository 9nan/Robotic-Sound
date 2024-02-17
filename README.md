# Real-Time Audio Pitch Shifter

**This Python script allows for real-time pitch shifting of audio input.** It uses the **PyAudio library** to capture audio from the microphone and then applies a pitch shift operation using the **Fast Fourier Transform (FFT)** via **NumPy**. This can be used for various audio processing applications, from music modification to speech transformation.

## Features

- **Real-time audio input and output processing.**
- **Adjustable pitch shift factor.**
- **Uses FFT for pitch shifting.**

## Requirements

- **Python 3.x**
- **PyAudio**
- **NumPy**

## Installation

First, ensure that **Python 3.x** is installed on your system. Then, install the required libraries using pip:

pip install pyaudio numpy

## Usage

To run the pitch shifter, simply execute the script in your terminal:

python example.py


Adjust the **SHIFT** variable in the script to control the pitch shift magnitude. A **SHIFT** value of 2 means the pitch is shifted up by an interval of 2 FFT bins, while a negative value would shift the pitch down.

## How It Works

The script captures audio from the default microphone in chunks, then applies a pitch shift by modifying the FFT of the audio signal. This is achieved by shifting the FFT bins by a specified amount (**SHIFT** variable) and then converting the modified FFT back to a time-domain signal which is played back in real-time.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is open-sourced under the **GNU GENERAL PUBLIC LICENSE**. See the LICENSE file for more details.

## Acknowledgments

- The **PyAudio and NumPy libraries** for providing the essential audio processing and mathematical tools needed for this project.

