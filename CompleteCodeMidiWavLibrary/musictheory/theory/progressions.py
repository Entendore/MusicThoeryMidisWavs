
# === Progressions ===
PROGRESSIONS = {
    "jazz": {
        "ii-V-I": ["ii","V","I"],
        "turnaround": ["I","vi","ii","V"],
        "modal": ["ii","V7","Imaj7","IVmaj7"],
        "minor_ii-V-i": ["ii°","V7","i"],
        "coltrane_changes": ["I","iii7","vi7","ii7","V7","I"],       # classic "Giant Steps" style
        "jazz_blues": ["I7","IV7","I7","ii7","V7","I7"]
    },
    "pop": {
        "pop_axis": ["I","V","vi","IV"],
        "pop_ballad": ["vi","IV","I","V"],
        "minor_pop": ["i","VI","III","VII"],
        "doo_wop": ["I","vi","IV","V"],
        "pop_vamp": ["I","IV","I","V"],
        "sensitive_pop": ["I","vi","ii","V"],
        "epic_pop": ["IV","I","V","vi"]
    },
    "rock": {
        "classic": ["I","IV","V"],
        "metal_drop": ["i","bVII","bVI","i"],
        "power_chords": ["I5","IV5","V5"],
        "grunge": ["i","bVI","bIII","bVII"]
    },
    "blues": {
        "12bar": ["I","I","I","I","IV","IV","I","I","V","IV","I","V"],
        "shuffle": ["I","IV","I","V","IV","I"],
        "minor_blues": ["i","iv","i","v","iv","i"]
    },
    "funk": {
        "jam": ["i","bVII","IV","i"],
        "chicken_scratch": ["I7","IV7","V7"]
    },
    "latin": {
        "salsa": ["I","IV","V","IV"],
        "bossa_nova": ["Imaj7","VI7","II7","V7"]
    },
    "edm": {
        "drop": ["vi","IV","I","V"],
        "build": ["i","bVI","bIII","bVII"],
        "uplifting": ["I","V","vi","IV"]
    },
    "film_cinematic": {
        "epic": ["I","V","vi","iii","IV","I","IV","V"],
        "tension": ["vi","IV","I","V"],
        "suspense": ["i","VII","VI","v","i"]
    },
    "reggae": {
        "one_drop": ["I","V","vi","IV"],
        "skank": ["I","IV","V","IV"]
    },
    "folk": {
        "folk_progression": ["I","V","vi","iii","IV","I"],
        "modal_folk": ["I","ii","IV","V"]
    },
    "soul_rnb": {
        "soul_progression": ["I","iii","IV","V"],
        "motown": ["I","vi","IV","V7"]
    },
    "hiphop": {
        "loop": ["vi","IV","I","V"],
        "minor_loop": ["i","VI","III","VII"]
    },
    "classical": {
        "pachelbel_canon": ["I","V","vi","iii","IV","I","IV","V"],
        "baroque_circle": ["I","IV","ii","V","I"]
    },
    "circle_of_fifths": {
        "standard": ["I","IV","vii°","iii","vi","ii","V","I"],
        "minor_fifths": ["i","iv","vii°","iii","vi","ii°","V","i"],
        "descending_fifths": ["I","vi","ii","V","I"], 
        "ascending_fifths": ["I","V","ii","vi","iii","vii°","IV","I"],
        "jazz_fifths": ["ii7","V7","Imaj7","VI7","ii7","V7","Imaj7"], 
        "extended_minor_fifths": ["i","iv","vii°","III","VI","ii°","V","i"], 
        "chromatic_fifths": ["I","V7/vi","vi","V7/ii","ii","V7/V","V","I"], 
        "pop_fifths_loop": ["I","V","vi","ii","V","I"],
        "classical_fifths_sequence": ["I","V","vi","iii","IV","ii","V","I"], 
        "minor_jazz_loop": ["i7","IV7","ii7","V7","i7"],
    },
    "chromatic_borrowed": {
        "secondary_dominants": ["I","V7/vi","vi","V7/ii","ii","V7/V","V","I"],
        "borrowed_major": ["i","bVI","bIII","IV"]
    },
    "experimental": {
        "ascending_chromatic": ["I","bII","II","bIII","III","IV"],
        "modal_mixture": ["I","bIII","IV","vii°","I"]
    }
}


# music_progressions.py
from typing import List, Union

class MusicProgressions:
    def __init__(self, notes, scales, chords):
        self.notes = notes
        self.scales = scales
        self.chords = chords

    def progression_from_roman(self, key_root: str, scale_name: str, roman_progression: List[str]) -> List[List[str]]:
        progression = []
        for roman in roman_progression:
            chord_root = self.scales.roman_to_note(roman, key_root)
            chord_notes = self.chords.chord_from_scale(chord_root, scale_name, [0,2,4])
            progression.append(chord_notes)
        return progression

    def progression_from_chord_types(self, root_notes: List[str], chord_types: List[str]) -> List[List[str]]:
        if len(root_notes) != len(chord_types):
            raise ValueError("root_notes and chord_types must have the same length")
        progression = []
        for root, ctype in zip(root_notes, chord_types):
            chord_notes = self.chords.build_chord(root, ctype)[0]  # default inversion 0
            progression.append(chord_notes)
        return progression

    def microtonal_progression(self, root_notes: List[str], intervals_list: List[List[float]]) -> List[List[str]]:
        if len(root_notes) != len(intervals_list):
            raise ValueError("root_notes and intervals_list must have the same length")
        progression = []
        for root, intervals in zip(root_notes, intervals_list):
            chord_notes = self.chords.build_microtonal_chord(root, intervals)[0]
            progression.append(chord_notes)
        return progression

    def transpose_progression(self, progression: List[List[str]], semitones: float) -> List[List[str]]:
        return [self.chords.transpose_chord(chord, semitones) for chord in progression]

    def invert_progression(self, progression: List[List[str]], inversion: int) -> List[List[str]]:
        inverted_progression = []
        for chord in progression:
            root = chord[0]
            chord_type = self.chords.identify_chord(chord)
            if chord_type:
                chord_notes = self.chords.build_chord(root, chord_type[0], inversion=inversion)
                inverted_progression.append(chord_notes)
            else:
                inverted_progression.append(chord)
        return inverted_progression

    def add_note_to_progression(self, progression: List[List[str]], interval: float) -> List[List[str]]:
        return [self.chords.add_note_to_chord(chord, interval) for chord in progression]

    def remove_note_from_progression(self, progression: List[List[str]], interval: float) -> List[List[str]]:
        return [self.chords.remove_note_from_chord(chord, interval) for chord in progression]
