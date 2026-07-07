import librosa
import numpy as np

def load_audio(path):
    """
        Loads an audio sample as a mono time-series.

        Parameters:
        - path (str): A string directory to the audio file's location.

        Returns:
        - audio (np.ndarray): The numerical array that measures its amplitude over time.
        - sample_rate (int): The audio file's sample rate.
    """
    audio, sample_rate = librosa.load(path, sr=None, mono=True)
    return audio, sample_rate

def compute_spectrogram(audio):
    """
        Computes the magnitude spectrogram of an audio signal.

        Parameters:
        - audio (np.ndarray): A numerical array that measures the amplitude of the audio signal over time.

        Returns:
        - spectrogram_db (np.ndarray): The dB-converted spectrogram obtained from the short-time Fourier transform.
    """
    stft = librosa.stft(audio)
    spectrogram = np.abs(stft)
    spectrogram_db = librosa.amplitude_to_db(spectrogram)
    return spectrogram_db