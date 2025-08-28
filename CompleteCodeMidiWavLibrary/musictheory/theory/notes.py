import math

class MusicNotes:
    ROOTS = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

    ENHARMONICS = {
        "C": ["C", "B#", "Dbb"],
        "C#": ["C#", "Db", "B##"],
        "D": ["D", "C##", "Ebb"],
        "D#": ["D#", "Eb", "Fbb"],
        "E": ["E", "Fb", "D##"],
        "F": ["F", "E#", "Gbb"],
        "F#": ["F#", "Gb", "E##"],
        "G": ["G", "F##", "Abb"],
        "G#": ["G#", "Ab"],
        "A": ["A", "G##", "Bbb"],
        "A#": ["A#", "Bb", "Cbb"],
        "B": ["B", "Cb", "A##"],
    }

    BASE_NOTE_NUMS = {
        "C": 0, "B#": 0, "Dbb": 0,
        "C#": 1, "Db": 1, "B##": 1,
        "D": 2, "C##": 2, "Ebb": 2,
        "D#": 3, "Eb": 3, "Fbb": 3,
        "E": 4, "Fb": 4, "D##": 4,
        "F": 5, "E#": 5, "Gbb": 5,
        "F#": 6, "Gb": 6, "E##": 6,
        "G": 7, "F##": 7, "Abb": 7,
        "G#": 8, "Ab": 8,
        "A": 9, "G##": 9, "Bbb": 9,
        "A#": 10, "Bb": 10, "Cbb": 10,
        "B": 11, "Cb": 11, "A##": 11,
    }

    MICROTONES = {
        "C+": 0.5, "C#-": 1.25, "C#+": 1.75,
        "D-": 1.5, "D+": 2.5,
        "D#-": 3.25, "D#+": 3.75,
        "E-": 3.5, "E+": 4.5,
        "F+": 5.5, "F#-": 6.25, "F#+": 6.75,
        "G-": 6.5, "G+": 7.5,
        "G#-": 8.25, "G#+": 8.75,
        "A-": 8.5, "A+": 9.5,
        "A#-": 10.25, "A#+": 10.75,
        "B-": 10.5, "B+": 11.5
    }

    def __init__(self):
        self.NOTE_NUMS, self.MIDI_TO_NOTES = self._build_note_dicts()

    def _build_note_dicts(self):
        note_nums = {}
        midi_to_notes = {}
        # Western notes
        for octave in range(-1, 10):
            for pc, names in self.ENHARMONICS.items():
                midi_base = (octave + 1) * 12 + self.BASE_NOTE_NUMS[pc]
                if 0 <= midi_base <= 127:
                    for name in names:
                        note_nums[f"{name}{octave}"] = midi_base
                        midi_to_notes.setdefault(midi_base, []).append(name)
        # Microtones
        for octave in range(-1, 10):
            for note, offset in self.MICROTONES.items():
                midi_num = (octave + 1) * 12 + offset
                if 0 <= midi_num <= 127:
                    note_nums[f"{note}{octave}"] = midi_num
                    midi_to_notes.setdefault(midi_num, []).append(note)
        return note_nums, midi_to_notes

    # ----------------------------
    # NOTE ↔ MIDI
    # ----------------------------
    def note_to_midi(self, note: str) -> float:
        if note not in self.NOTE_NUMS:
            raise ValueError(f"Unknown note: {note}")
        return self.NOTE_NUMS[note]

    def midi_to_note(self, midi: float, prefer_flats=False, prefer_sharps=False, prefer_natural=False) -> str:
        nearest = min(self.MIDI_TO_NOTES.keys(), key=lambda x: abs(x - midi))
        candidates = self.MIDI_TO_NOTES[nearest]

        # Preference logic
        if prefer_natural:
            for c in candidates:
                if c[0] in "ABCDEFG":
                    return c
        if prefer_flats:
            for c in candidates:
                if "b" in c or "-" in c:
                    return c
        if prefer_sharps:
            for c in candidates:
                if "#" in c or "+" in c:
                    return c
        # Default: canonical
        return candidates[0]

    # ----------------------------
    # Nearest note with deviation in cents
    # ----------------------------
    def midi_to_note_with_cents(self, midi: float, prefer_flats=False, prefer_sharps=False, prefer_natural=False):
        nearest = min(self.MIDI_TO_NOTES.keys(), key=lambda x: abs(x - midi))
        note = self.midi_to_note(nearest, prefer_flats, prefer_sharps, prefer_natural)
        cents_deviation = (midi - nearest) * 100
        return note, cents_deviation

    # ----------------------------
    # FREQUENCY ↔ NOTE
    # ----------------------------
    def note_to_freq(self, note: str, a4_freq=440.0) -> float:
        midi = self.note_to_midi(note)
        return a4_freq * 2 ** ((midi - 69) / 12)

    def freq_to_note(self, freq: float, a4_freq=440.0, prefer_flats=False, prefer_sharps=False, prefer_natural=False):
        midi = 69 + 12 * math.log2(freq / a4_freq)
        return self.midi_to_note(midi, prefer_flats, prefer_sharps, prefer_natural)

    # ----------------------------
    # TRANSPOSE & INTERVAL
    # ----------------------------
    def transpose(self, note: str, semitones: float, prefer_flats=False, prefer_sharps=False, prefer_natural=False) -> str:
        midi = self.note_to_midi(note)
        return self.midi_to_note(midi + semitones, prefer_flats, prefer_sharps, prefer_natural)

    def interval(self, note1: str, note2: str) -> float:
        return self.note_to_midi(note2) - self.note_to_midi(note1)

    def interval_cents(self, note1: str, note2: str) -> float:
        return self.interval(note1, note2) * 100

    # ----------------------------
    # OCTAVE & LISTING
    # ----------------------------
    def list_octave_notes(self, octave: int) -> list:
        notes = [n for n in self.NOTE_NUMS if n.endswith(str(octave))]
        return sorted(notes, key=lambda x: self.NOTE_NUMS[x])

    def sort_notes(self, notes: list) -> list:
        return sorted(notes, key=lambda n: self.note_to_midi(n))

    def __repr__(self):
        return f"<MusicNotes: {len(self.NOTE_NUMS)} notes including microtones>"
