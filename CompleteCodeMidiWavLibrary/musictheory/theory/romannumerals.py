# roman.py (extended)
from typing import List, Union
from notes import MusicNoteToolkit
from chords import CHORD_FORMULAS, Chord

toolkit = MusicNoteToolkit()

ROMAN_TO_SCALE_DEGREE = {
    "I": 0, "II": 2, "III": 4, "IV": 5, "V": 7, "VI": 9, "VII": 11
}

# ----------------------------
# ROMAN ↔ MIDI
# ----------------------------
def roman_to_midi(roman: str, key_root: str = "C") -> int:
    base_midi = toolkit.note_to_midi(f"{key_root}4")
    if base_midi is None:
        raise ValueError(f"Unknown key root: {key_root}")
    numeral = roman.rstrip("°+")
    octave_shift = 0
    if roman[-1].isdigit():  # e.g., "V5"
        octave_shift = int(roman[-1])
    if numeral.upper() not in ROMAN_TO_SCALE_DEGREE:
        raise ValueError(f"Unknown Roman numeral: {roman}")
    interval = ROMAN_TO_SCALE_DEGREE[numeral.upper()]
    midi_note = base_midi + interval + octave_shift * 12
    if "°" in roman:
        midi_note -= 1
    if "+" in roman:
        midi_note += 1
    return midi_note

def midi_to_roman(midi: int, key_root: str = "C") -> str:
    key_midi = toolkit.note_to_midi(f"{key_root}4")
    if key_midi is None:
        raise ValueError(f"Unknown key root: {key_root}")
    interval = (midi - key_midi) % 12
    closest = min(ROMAN_TO_SCALE_DEGREE.items(), key=lambda x: abs(x[1]-interval))
    numeral = closest[0]
    diff = interval - closest[1]
    if diff == -1:
        numeral += "°"
    elif diff == 1:
        numeral += "+"
    return numeral

# ----------------------------
# ROMAN ↔ CHORD
# ----------------------------
def roman_to_chord(roman: str, key_root: str = "C", chord_formulas=CHORD_FORMULAS) -> Chord:
    root_midi = roman_to_midi(roman, key_root)
    if roman.isupper():
        if "°" in roman:
            chord_type = "diminished7"
        else:
            chord_type = "major"
    elif roman.islower():
        if "°" in roman:
            chord_type = "diminished7"
        else:
            chord_type = "minor"
    else:
        chord_type = "major"
    return Chord(root_midi=root_midi, chord_type=chord_type, chord_formulas=chord_formulas)

def transpose_roman(roman: str, semitones: int, key_root: str = "C") -> str:
    midi = roman_to_midi(roman, key_root)
    new_midi = midi + semitones
    return midi_to_roman(new_midi, key_root)

# ----------------------------
# ROMAN NUMERAL SEQUENCE GENERATION
# ----------------------------
def generate_progression(key_root: str = "C", key_type: str = "major", progression: List[str] = None) -> List[Chord]:
    """
    Generate a sequence of Chord objects from Roman numerals in a key.
    Example: progression=["I","vi","IV","V"]
    """
    if progression is None:
        progression = ["I", "IV", "V", "I"]  # default
    chords = []
    for numeral in progression:
        chords.append(roman_to_chord(numeral, key_root))
    return chords

# ----------------------------
# IDENTIFY ROMAN NUMERAL FROM CHORD
# ----------------------------
def chord_to_roman(chord: Chord, key_root: str = "C") -> str:
    """
    Identify the Roman numeral of a given chord in a key.
    """
    root_midi = chord.root
    numeral = midi_to_roman(root_midi, key_root)
    # Check chord quality
    if "major" in chord.type.lower() and numeral.islower():
        numeral = numeral.upper()
    elif "minor" in chord.type.lower() and numeral.isupper():
        numeral = numeral.lower()
    elif "diminished" in chord.type.lower():
        numeral += "°"
    elif "augmented" in chord.type.lower():
        numeral += "+"
    return numeral

def sequence_to_roman(chords: List[Chord], key_root: str = "C") -> List[str]:
    """
    Convert a list of Chord objects to Roman numerals in a given key.
    """
    return [chord_to_roman(ch, key_root) for ch in chords]
