import librosa
import numpy as np

def find_onsets(audio, sample_rate, hop_length=512):
    """
        Scans through an audio file, generating and returning a list of onsets.

        Parameters:
        - audio (np.ndarray): The numerical array that measures its amplitude over time.
        - sample_rate (int): The audio file's sample rate.
        - hop_length (int): The number of samples between successive frames.

        Returns:
        - onset_times (np.ndarray): The array of onsets.
    """
    audio_length = len(audio) / sample_rate
    onset_frames = librosa.onset.onset_detect(y=audio, sr=sample_rate, hop_length=hop_length)
    onset_times = librosa.frames_to_time(onset_frames, sr=sample_rate, hop_length=hop_length)
    onset_times = onset_times[onset_times <= audio_length]
    return onset_times