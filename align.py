import librosa
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def notes_to_midi_list(notes):
    """
        Converts a list of Note objects into a list of MIDI note numbers.
 
        Parameters:
        - notes (list): List of Note objects.
 
        Returns:
        - midi_list (list): List of MIDI note numbers.
    """
    midi_list = []

    for i, note in enumerate(notes):
        midi_num = librosa.note_to_midi(note.pitch)
        midi_list.append(midi_num)
    
    return midi_list

def align(reference_notes, performance_notes):
    """
        Aligns a performed melody against a reference melody using dynamic time warping (DTW).

        Parameters:
        - reference_notes (list): List of Note objects for the reference recording.
        - performance_notes (list): List of Note objects for the performance recording.

        Returns:
        - path (list): List of tuples that matches the indexes of both note lists
    """

    reference_midi = notes_to_midi_list(reference_notes)
    performance_midi = notes_to_midi_list(performance_notes)

    if len(reference_midi) == 0 or len(performance_midi) == 0:
        raise ValueError("One of the recordings has no detectable notes.")
    
    reference_points = []
    for m in reference_midi:
        reference_points.append([m])

    performance_points = []
    for m in performance_midi:
        performance_points.append([m])

    _, path = fastdtw(reference_points, performance_points, dist=euclidean)

    return path