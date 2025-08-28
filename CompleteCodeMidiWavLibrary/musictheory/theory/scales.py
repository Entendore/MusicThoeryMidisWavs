class MusicScales:
    INTERVAL_NAMES = {0:"unison",1:"minor 2nd",2:"major 2nd",3:"minor 3rd",4:"major 3rd",
                      5:"perfect 4th",6:"tritone",7:"perfect 5th",8:"minor 6th",9:"major 6th",
                      10:"minor 7th",11:"major 7th",12:"octave"}

    ROMAN_NUMERALS = {"I":0,"II":2,"III":4,"IV":5,"V":7,"VI":9,"VII":11}

    WESTERN_SCALES = {
        "major":[0,2,4,5,7,9,11],
        "minor":[0,2,3,5,7,8,10],
        "harmonic_minor":[0,2,3,5,7,8,11],
        "melodic_minor":[0,2,3,5,7,9,11],
        "pentatonic_major":[0,2,4,7,9],
        "pentatonic_minor":[0,3,5,7,10],
        "whole_tone":[0,2,4,6,8,10],
        "chromatic":list(range(12)),
        "blues":[0,3,5,6,7,10]
    }

    EASTERN_SCALES = {
        "arabic_scale":[0,1,4,5,7,8,11],
        "egyptian_scale":[0,2,5,7,9],
        "persian_scale":[0,1,4,5,6,8,11],
        "indian_raga":[0,2,3,5,7,9,10.5]
    }

    MICROTONAL_SCALES = {
        "quarter_tone_major":[0,1,2,3,4,5.5,6.5,7,8,9,10,11]
    }

    MODES = {
        "ionian":WESTERN_SCALES["major"],
        "dorian":[0,2,3,5,7,9,10],
        "phrygian":[0,1,3,5,7,8,10],
        "lydian":[0,2,4,6,7,9,11],
        "mixolydian":[0,2,4,5,7,9,10],
        "aeolian":WESTERN_SCALES["minor"],
        "locrian":[0,1,3,5,6,8,10],
        "harmonic_minor_mode":[0,2,3,5,7,8,11],
        "melodic_minor_mode":[0,2,3,5,7,9,11]
    }

    def __init__(self, notes:"MusicNotes"):
        self.notes = notes

    def get_scale_notes(self, root:str, scale_name:str) -> list:
        if scale_name in self.WESTERN_SCALES:
            intervals = self.WESTERN_SCALES[scale_name]
        elif scale_name in self.EASTERN_SCALES:
            intervals = self.EASTERN_SCALES[scale_name]
        elif scale_name in self.MICROTONAL_SCALES:
            intervals = self.MICROTONAL_SCALES[scale_name]
        elif scale_name in self.MODES:
            intervals = self.MODES[scale_name]
        else:
            raise ValueError(f"Unknown scale or mode: {scale_name}")
        root_midi = self.notes.note_to_midi(root)
        return [self.notes.midi_to_note(root_midi + i) for i in intervals]

    def list_octave_scale_notes(self, root:str, scale_name:str, octave:int) -> list:
        return [n for n in self.get_scale_notes(root, scale_name) if n.endswith(str(octave))]

    def transpose_note(self, note:str, semitones:float) -> str:
        return self.notes.transpose(note, semitones)

    def interval_between(self, note1:str, note2:str) -> tuple[float,str]:
        semitones = self.notes.interval(note1, note2)
        semitone_mod = round(semitones)%12
        name = self.INTERVAL_NAMES.get(semitone_mod,f"{semitones} semitones")
        return semitones,name

    def interval_cents(self, note1:str, note2:str) -> float:
        return self.notes.interval(note1,note2)*100

    def roman_to_note(self, roman:str, key_root:str="C4") -> str:
        key_midi = self.notes.note_to_midi(key_root)
        numeral = roman.upper()
        if numeral not in self.ROMAN_NUMERALS:
            raise ValueError(f"Unknown Roman numeral: {roman}")
        return self.notes.midi_to_note(key_midi + self.ROMAN_NUMERALS[numeral])

    def note_to_roman(self, note:str, key_root:str="C4") -> str:
        key_midi = self.notes.note_to_midi(key_root)
        note_midi = self.notes.note_to_midi(note)
        semitones = round(note_midi - key_midi)%12
        for numeral,interval in self.ROMAN_NUMERALS.items():
            if interval==semitones:
                return numeral
        return f"{semitones} semitones"

    def transpose_roman(self, roman:str, semitones:float, key_root:str="C4") -> str:
        note = self.roman_to_note(roman,key_root)
        transposed_note = self.transpose_note(note,semitones)
        try:
            return self.note_to_roman(transposed_note,key_root)
        except ValueError:
            return transposed_note

    def get_mode_notes(self, root:str, mode_name:str) -> list:
        if mode_name not in self.MODES:
            raise ValueError(f"Unknown mode: {mode_name}")
        root_midi = self.notes.note_to_midi(root)
        return [self.notes.midi_to_note(root_midi + i) for i in self.MODES[mode_name]]

    def transpose_scale(self, root:str, scale_name:str, semitones:float) -> list:
        return [self.transpose_note(n,semitones) for n in self.get_scale_notes(root,scale_name)]

    def get_chord_from_scale(self, root:str, scale_name:str, degrees:list[int]) -> list:
        scale_notes = self.get_scale_notes(root,scale_name)
        return [scale_notes[d%len(scale_notes)] for d in degrees]

    def list_all_octaves(self, root:str, scale_name:str, min_oct:int=-1, max_oct:int=9) -> list:
        all_notes=[]
        for octave in range(min_oct,max_oct+1):
            all_notes.extend(self.list_octave_scale_notes(root,scale_name,octave))
        return all_notes

    def get_chord_progression(self, root:str, scale_name:str, roman_progression:list[str]) -> list[list[str]]:
        progression=[]
        for roman in roman_progression:
            chord_root = self.roman_to_note(roman,root)
            chord = self.get_chord_from_scale(chord_root,scale_name,[0,2,4])
            progression.append(chord)
        return progression

    def get_all_scales(self) -> dict:
        return {"western":list(self.WESTERN_SCALES.keys()),
                "eastern":list(self.EASTERN_SCALES.keys()),
                "microtonal":list(self.MICROTONAL_SCALES.keys()),
                "modes":list(self.MODES.keys())}
