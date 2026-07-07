from note import Note
from pitch_detection import find_frequency, find_pitch

def add_notes(audio, sample_rate, onset_times, audio_duration):
    """
        Creates a list of notes using the data of each onset.
        
        Parameters:
        - audio (np.ndarray): Numerical array that measures its amplitude over time.
        - sample_rate (int): Sample rate of audio file.
        - onset_times (np.ndarray): Array of onsets.
        - audio_duration (float): Length of the audio file in seconds.

        Returns:
        - notes (list): The list of note objects.
    """
    notes = []

    # Iterates through each onset
    for i, onset in enumerate(onset_times):
        # Checks if there is an onset after the current one
        if i < len(onset_times) - 1:
            next_onset = onset_times[i+1]
            duration = onset_times[i+1] - onset
        else:
            next_onset = None
            duration = audio_duration - onset

        # Derives a note object from the onset
        frequency = find_frequency(audio, sample_rate, onset, next_onset)
        pitch = find_pitch(frequency)
        note = Note(onset, duration, pitch, frequency)
        
        # Adds the note to the list of anotes
        notes.append(note)
    
    return notes