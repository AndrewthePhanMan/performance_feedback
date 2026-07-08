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

def align(reference, performance):
    """
        Aligns 
    """

    _, path = fastdtw(reference, performance, dist=euclidean)