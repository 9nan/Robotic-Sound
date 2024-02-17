import pyaudio
import numpy as np

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
SHIFT = 2  # Pitch shift factor, try adjusting this for different effects

p = pyaudio.PyAudio()

def pitch_shift(data, shift):
    fft = np.fft.fft(data)
    shifted_fft = np.zeros(len(fft), dtype=complex)
    half_len = len(fft) // 2  # Half the length of the FFT array

    # Apply the shift only within the bounds of the array
    for i in range(half_len):
        if 0 <= i + shift < half_len:
            shifted_fft[i + shift] = fft[i]

    # Handle the symmetry for the second half of the FFT array
    # Ensure we don't exceed the array bounds by using min/max
    for i in range(half_len + 1, len(fft)):
        if 0 <= i - shift < len(fft):
            shifted_fft[i - shift] = fft[i]

    # Ensure the result is symmetrical
    shifted_fft[half_len:] = np.conj(shifted_fft[1:half_len + 1][::-1])

    # Convert back to time domain
    shifted_data = np.fft.ifft(shifted_fft)
    return shifted_data.real.astype(np.int16)


def callback(in_data, frame_count, time_info, status):
    audio_data = np.frombuffer(in_data, dtype=np.int16)
    shifted_data = pitch_shift(audio_data, SHIFT)
    return (shifted_data.tobytes(), pyaudio.paContinue)

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

stream.start_stream()

try:
    while stream.is_active():
        pass
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
p.terminate()
