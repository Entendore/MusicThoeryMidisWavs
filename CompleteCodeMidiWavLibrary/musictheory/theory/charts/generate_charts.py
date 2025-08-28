import os
import matplotlib.pyplot as plt
from music_notes import MusicNotes

# Create charts folder if it doesn't exist
if not os.path.exists("charts"):
    os.makedirs("charts")

music = MusicNotes()

# Chart 1: Frequencies of Notes in Octave 4
notes = music.list_octave_notes(4)
frequencies = [music.note_to_freq(note) for note in notes]

plt.figure(figsize=(12, 6))
plt.bar(notes, frequencies, color="skyblue", edgecolor="navy")
plt.xlabel("Note")
plt.ylabel("Frequency (Hz)")
plt.title("Frequencies of Notes in Octave 4")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/octave_4_frequencies.png")
plt.close()

# Chart 2: Frequency of Note C Across Octaves
octaves = range(-1, 10)
c_notes = [f"C{octave}" for octave in octaves]
c_frequencies = [music.note_to_freq(note) for note in c_notes]

plt.figure(figsize=(10, 6))
plt.plot(octaves, c_frequencies, marker="o", color="coral")
plt.xlabel("Octave")
plt.ylabel("Frequency (Hz)")
plt.title("Frequency of Note C Across Octaves")
plt.grid(True)
plt.savefig("charts/c_note_frequencies.png")
plt.close()