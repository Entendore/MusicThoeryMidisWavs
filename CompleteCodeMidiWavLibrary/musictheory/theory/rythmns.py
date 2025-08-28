
# ----------------------------
# RHYTHM PATTERNS
# ----------------------------
RHYTHM_PATTERNS = {
    "whole": [1],
    "half": [0.5]*2,
    "quarter": [0.25]*4,
    "eighth": [0.125]*8,
    "sixteenth": [0.0625]*16,
    "32nd": [0.03125]*32,
    "straight":[1,1,1,1],
    "triplet": [1/3]*3, 
    "quintuplet": [1/5]*5,
    "syncopated": [0.5, 0.25, 0.25, 0.5, 0.5],
    "rock_backbeat": [0.25, 0.25, 0.5, 0.25, 0.25, 0.5],
    "bossa_nova": [0.25, 0.125, 0.125, 0.25, 0.25, 0.125, 0.125],
    "swing":[0.66,0.34,0.66,0.34],
    "clave_3-2":[1,0.5,0.5,1,1],
    "clave_2-3":[0.5,1,0.5,1,1],
    "polyrhythm_3_over_4":[1/3,1/3,1/3,0.5,0.5,0.5,0.5],
}

RHYTHMS = {
    "whole": [1],
    "half": [0.5],
    "quarter": [0.25],
    "eighth": [0.125],
    "sixteenth": [0.0625],
    "32nd": [0.03125],
    "triplet": [1/3], 
    "quintuplet": [1/5],
}


# music_rhythms.py
from typing import List, Union
import random

class MusicRhythms:
    def __init__(self, bpm: int = 120, time_signature: str = "4/4"):
        self.bpm = bpm
        self.time_signature = time_signature
        self.beats_per_measure, self.beat_unit = map(int, time_signature.split("/"))

    def set_bpm(self, bpm: int):
        self.bpm = bpm

    def set_time_signature(self, time_signature: str):
        self.time_signature = time_signature
        self.beats_per_measure, self.beat_unit = map(int, time_signature.split("/"))

    def note_duration_seconds(self, note_type: str = "quarter") -> float:
        quarter_note_sec = 60 / self.bpm
        durations = {
            "whole": 4 * quarter_note_sec,
            "half": 2 * quarter_note_sec,
            "quarter": quarter_note_sec,
            "eighth": quarter_note_sec / 2,
            "sixteenth": quarter_note_sec / 4,
            "thirty_second": quarter_note_sec / 8,
        }
        return durations.get(note_type, quarter_note_sec)

    def generate_rhythm_pattern(self, pattern_length: int, note_types: List[str] = None) -> List[str]:
        if note_types is None:
            note_types = ["quarter", "eighth", "sixteenth"]
        pattern = [random.choice(note_types) for _ in range(pattern_length)]
        return pattern

    def generate_polyrhythm(self, beats_a: int, beats_b: int, measures: int = 1) -> List[List[str]]:
        pattern = []
        for m in range(measures):
            measure_pattern = []
            for i in range(max(beats_a, beats_b)):
                step = []
                if i % (max(beats_a, beats_b) // beats_a) == 0:
                    step.append("A")
                if i % (max(beats_a, beats_b) // beats_b) == 0:
                    step.append("B")
                measure_pattern.append(step)
            pattern.append(measure_pattern)
        return pattern

    def apply_swing(self, pattern: List[str], swing_ratio: float = 0.6) -> List[float]:
        swung_pattern = []
        for note in pattern:
            duration = self.note_duration_seconds(note)
            if note in ["eighth", "sixteenth"]:
                swung_pattern.append(duration * swing_ratio)
                swung_pattern.append(duration * (1 - swing_ratio))
            else:
                swung_pattern.append(duration)
        return swung_pattern
