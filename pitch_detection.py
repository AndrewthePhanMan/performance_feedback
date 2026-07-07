import librosa
import numpy as np

def find_frequency(audio, sample_rate, onset, next_onset=None):
    """
        Identifies the fundamental frequency at a specific onset.

        Parameters:
        - audio (np.ndarray): The numerical array that measures its amplitude over time.
        - sample_rate (int): The audio file's sample rate.
        - onset (float): The location of the onset in seconds.

        Returns:
        - frequency (float): The onset's fundamental frequency.
    """
    # Creates a 100 millisecond slice of the audio, beginning from the onset
    start = int(onset * sample_rate)
    window = onset + 0.2 # 200 ms ahead of "start"

    # Shortens the window if the next note starts before the 200 ms runtime
    if next_onset is not None:
        window_end_time = min(window_end_time, next_onset)

    end = int(window * sample_rate) # 200 ms ahead of "start"
    end = min(end, len(audio)) # Checks if "end" goes beyond the audio's length (last note)

    audio_slice = audio[start:end]

    # Checks if the audio_slice is long enough to be analyzed (20 ms)
    if len(audio_slice) < int(0.02 * sample_rate):
        return None

    frequencies, voiced_flags, _ = librosa.pyin(
        y=audio_slice,
        fmin=librosa.note_to_hz("C2"),
        fmax=librosa.note_to_hz("C7"),
        sr=sample_rate
    )

    frequencies = frequencies[voiced_flags & ~np.isnan(frequencies)]
    
    if len(frequencies) == 0:
        return None

    return np.median(frequencies)

def find_pitch(frequency):
    """
        Finds the associated pitch of a given frequency (e.g. C2, A4, D5).

        Parameters:
        - frequency (float): The frequency (Hz) of the note.

        Returns:
        - pitch (str): The musical note's name (e.g. C2, A4, D5).
    """
    if frequency is None:
        return None
    return librosa.hz_to_note(frequency)