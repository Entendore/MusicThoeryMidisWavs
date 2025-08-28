
# ----------------------------
# CHORD FORMULAS
# ----------------------------
CHORD_FORMULAS = {
    "triads": {
        "major":      [0, 4, 7],
        "minor":      [0, 3, 7],
        "augmented":  [0, 4, 8],
        "diminished": [0, 3, 6],
        "sus2":       [0, 2, 7],
        "sus4":       [0, 5, 7],
        "power":      [0, 7],
    },
    "sixth_chords": {
        "major6": [0, 4, 7, 9],
        "minor6": [0, 3, 7, 9],
        "6":      [0, 4, 7, 9],  
    },
    "seventh_chords": {
        "major7":          [0, 4, 7, 11],
        "minor7":          [0, 3, 7, 10],
        "dominant7":       [0, 4, 7, 10],
        "half_diminished7": [0, 3, 6, 10],
        "diminished7":     [0, 3, 6, 9],
        "augmented7":      [0, 4, 8, 11],
        "7":               [0, 4, 7, 11],
        "dominant":        [0, 4, 7],     
    },
    "extended_chords": {
        "minor9":      [0, 3, 7, 10, 14],
        "major9":      [0, 4, 7, 11, 14],
        "dominant9":   [0, 4, 7, 10, 14],
        "dominant11":  [0, 4, 7, 10, 14, 17],
        "dominant13":  [0, 4, 7, 10, 14, 17, 21],
        "9":           [0, 4, 7, 10, 14], 
        "11":          [0, 4, 7, 10, 14, 17], 
        "13":          [0, 4, 7, 10, 14, 17, 21], 
        "add9":        [0, 4, 7, 14],
    },
    "power_chords": {
        "power9":  [0, 7, 14],
        "power11": [0, 7, 14, 17],
        "power13": [0, 7, 14, 17, 21],
    },
    "diminished_half_augmented_extended": {
        "half_diminished":        [0, 3, 6],
        "half_diminished9":       [0, 3, 6, 10, 14],
        "half_diminished11":      [0, 3, 6, 10, 14, 17],
        "half_diminished13":      [0, 3, 6, 10, 14, 17, 21],
        "diminished9":            [0, 3, 6, 10, 14],
        "diminished11":           [0, 3, 6, 10, 14, 17],
        "diminished13":           [0, 3, 6, 10, 14, 17, 21],
        "augmented9":             [0, 4, 8, 14],
        "augmented11":            [0, 4, 8, 14, 17],
        "augmented13":            [0, 4, 8, 14, 17, 21],
    }
}


def chord_inversions(root_midi, chord_type, chord_formulas=CHORD_FORMULAS, inversion=None):
    # Flatten nested dictionary to find the chord
    flat_chords = {}
    for category in chord_formulas.values():
        flat_chords.update(category)

    if chord_type not in flat_chords:
        raise ValueError(f"Chord type '{chord_type}' not found.")

    intervals = flat_chords[chord_type]
    n = len(intervals)
    inversions = []

    # Generate all inversions
    for i in range(n):
        inv = intervals[i:] + [x + 12 for x in intervals[:i]]  # move first i notes up an octave
        inv_midi = [root_midi + semitone for semitone in inv]
        inversions.append(inv_midi)

    if inversion is None:
        return inversions
    elif 0 <= inversion < n:
        return inversions[inversion]
    else:
        raise ValueError(f"Inversion index must be between 0 and {n-1}")
    


# ----------------------------
# Chord Class
# ----------------------------

class Chord:
    def __init__(self, root_midi: int, chord_type: str, chord_formulas=CHORD_FORMULAS):
        self.root = root_midi
        self.type = chord_type
        self.formulas = chord_formulas
        self.flat_formulas = self._flatten_formulas(chord_formulas)
        
        if chord_type not in self.flat_formulas:
            raise ValueError(f"Chord type '{chord_type}' not found.")
        
        self.intervals = self.flat_formulas[chord_type]
        self.notes = [self.root + i for i in self.intervals]
    
    # ----------------------------
    # Helper Methods
    # ----------------------------
    @staticmethod
    def _flatten_formulas(chord_formulas):
        flat = {}
        for category in chord_formulas.values():
            flat.update(category)
        return flat

    @staticmethod
    def midi_to_name(midi_note: int) -> str:
        octave = (midi_note // 12) - 1
        note = NOTE_NAMES[midi_note % 12]
        return f"{note}{octave}"

    @staticmethod
    def notes_to_names(midi_notes: List[int]) -> List[str]:
        return [Chord.midi_to_name(n) for n in midi_notes]
    
    # ----------------------------
    # Chord Functions
    # ----------------------------
    def get_notes(self) -> List[int]:
        """Return chord notes as MIDI numbers."""
        return self.notes.copy()
    
    def get_note_names(self) -> List[str]:
        """Return chord notes as names."""
        return self.notes_to_names(self.notes)
    
    def transpose(self, semitones: int):
        """Transpose chord by semitones."""
        self.root += semitones
        self.notes = [n + semitones for n in self.notes]
    
    def inversions(self, inversion: Union[int, None] = None) -> Union[List[List[int]], List[int]]:
        """Return all or a specific inversion of the chord."""
        n = len(self.intervals)
        inversions = []
        for i in range(n):
            inv = self.intervals[i:] + [x + 12 for x in self.intervals[:i]]
            inv_midi = [self.root + semitone for semitone in inv]
            inversions.append(inv_midi)
        
        if inversion is None:
            return inversions
        elif 0 <= inversion < n:
            return inversions[inversion]
        else:
            raise ValueError(f"Inversion index must be between 0 and {n-1}")

    def add_note(self, interval: int):
        """Add a note to the chord (interval from root)."""
        new_note = self.root + interval
        if new_note not in self.notes:
            self.notes.append(new_note)
            self.notes.sort()
    
    def remove_note(self, interval: int):
        """Remove a note from the chord (interval from root)."""
        target_note = self.root + interval
        if target_note in self.notes:
            self.notes.remove(target_note)
    
    def identify(self, chord_notes: List[int] = None) -> List[str]:
        """
        Identify possible chord types for given MIDI notes.
        If chord_notes is None, use self.notes.
        """
        if chord_notes is None:
            chord_notes = self.notes
        chord_notes_sorted = sorted([n % 12 for n in chord_notes])
        matches = []
        for name, intervals in self.flat_formulas.items():
            intervals_mod = sorted([i % 12 for i in intervals])
            for shift in range(len(intervals_mod)):
                rotated = intervals_mod[shift:] + intervals_mod[:shift]
                if chord_notes_sorted == rotated:
                    matches.append(name)
                    break
        return matches