from processor import load_audio
from onset_detection import find_onsets
from note_list import add_notes
import librosa

audio, sr = load_audio("samples/piano_good.wav")
duration = librosa.get_duration(y=audio, sr=sr)
onsets = find_onsets(audio, sr)
notes = add_notes(audio, sr, onsets, duration)

for note in notes:
    print(note.pitch, note.onset, note.duration)