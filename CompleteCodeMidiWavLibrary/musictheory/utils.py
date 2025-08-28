import os, random
import pretty_midi

from config import RHYTHMS, RHYTHM_PATTERNS, HUMANIZATION, ROMAN_TO_DEGREE, ROMAN_CHORD_QUALITY, ROMAN_TO_CHORD, DEGREE_TO_ROMAN, CHORD_INTERVALS, BASE_NOTE_NUMS, SCALE_INTERVALS, MODES, CHORD_FORMULAS, NOTE_NUMS, SONG_STRUCTURES, SECTION_PROGS, GENRE_INSTRUMENTS, GENRE_EXPRESSIONS, GENRE_TEMPOS, GENRES, PROGRESSIONS

def note_to_midi(note):
    import re
    match = re.match(r'^([A-Ga-g][#b]?)(-?\d+)$', note)
    if not match:
        raise ValueError(f"Invalid note format: {note}")
    
    name, octave = match.groups()
    octave = int(octave)
    if name not in BASE_NOTE_NUMS:
        raise ValueError(f"Unknown note: {name}")
    
    midi_num = 12 * (octave + 1) + BASE_NOTE_NUMS[name]
    return midi_num

def midi_to_note(midi_num, prefer_sharps=True):
    octave = (midi_num // 12) - 1
    note_index = midi_num % 12
    
    # Create reverse mapping
    reverse_map = {}
    for k, v in BASE_NOTE_NUMS.items():
        if prefer_sharps and "#" in k:
            reverse_map[v] = k
        elif not prefer_sharps and "b" in k:
            reverse_map[v] = k
        elif v not in reverse_map:
            reverse_map[v] = k
    
    note_name = reverse_map[note_index]
    return f"{note_name}{octave}"


def transpose(note, semitones):
    midi_num = note_to_midi(note)
    transposed_midi = midi_num + semitones
    return midi_to_note(transposed_midi)

def generate_scale(root, scale_type="major"):
    if scale_type not in SCALE_INTERVALS:
        raise ValueError(f"Unknown scale type: {scale_type}")
    
    root_midi = note_to_midi(root)
    intervals = SCALE_INTERVALS[scale_type]
    
    return [midi_to_note(root_midi + i) for i in intervals]

def generate_chord(root, chord_type="major"):
    if chord_type not in CHORD_INTERVALS:
        raise ValueError(f"Unknown chord type: {chord_type}")
    
    root_midi = note_to_midi(root)
    intervals = CHORD_INTERVALS[chord_type]
    
    return [midi_to_note(root_midi + i) for i in intervals]

def chord_inversion(chord_notes, inversion=0):
    if inversion == 0:
        return chord_notes.copy()
    
    notes_midi = [note_to_midi(n) for n in chord_notes]
    
    for i in range(inversion):
        # Move the lowest note up one octave
        notes_midi[i] += 12
    
    # Sort ascending
    notes_midi.sort()
    
    return [midi_to_note(n) for n in notes_midi]

def all_inversions(chord_notes):
    num_notes = len(chord_notes)
    inversions = []
    
    for i in range(num_notes):
        inversions.append(chord_inversion(chord_notes, i))
    
    return inversions


def generate_mode(root, mode_name="ionian"):
    if mode_name not in MODES:
        raise ValueError(f"Unknown mode: {mode_name}")
    
    root_midi = note_to_midi(root)
    intervals = MODES[mode_name]
    
    return [midi_to_note(root_midi + i) for i in intervals]

def degree_to_chord_name(scale_notes, degree):
    degree = degree % len(scale_notes)
    return scale_notes[degree]

def roman_to_int(roman):
    if roman not in ROMAN_TO_DEGREE:
        raise ValueError(f"Unknown Roman numeral: {roman}")
    return ROMAN_TO_DEGREE[roman]

def int_to_roman(degree):
    if degree not in DEGREE_TO_ROMAN:
        raise ValueError(f"Invalid degree: {degree}")
    return DEGREE_TO_ROMAN[degree]

def roman_to_degree(roman):
    base = roman.replace("°","").replace("7","").replace("maj","").replace("min","")
    if base not in ROMAN_TO_DEGREE:
        raise ValueError(f"Unknown Roman numeral: {roman}")
    return ROMAN_TO_DEGREE[base]

def degree_to_roman(degree, chord_type=None):
    roman = DEGREE_TO_ROMAN[degree % 7]
    if chord_type:
        if chord_type == "dim":
            roman += "°"
        elif chord_type == "7":
            roman += "7"
        elif chord_type == "maj7":
            roman += "maj7"
        elif chord_type == "min7":
            roman += "min7"
    return roman

def roman_to_chord_name(root_note, roman, scale_type="major"):
    scale_notes = generate_scale(root_note, scale_type) if scale_type in SCALE_INTERVALS else generate_mode(root_note, scale_type)
    degree = roman_to_degree(roman)
    
    # Determine chord quality
    chord_type = ROMAN_CHORD_QUALITY.get(roman, "major")
    
    # Build the chord
    root = scale_notes[degree % len(scale_notes)]
    
    if chord_type in ["major","minor","dim","aug"]:
        chord = generate_chord(root, chord_type)
    elif chord_type in ["7","maj7","min7"]:
        # 7th chords: root + 3rd + 5th + 7th
        intervals = CHORD_INTERVALS.get(chord_type, [0,4,7,10])
        root_midi = note_to_midi(root)
        chord = [midi_to_note(root_midi + i) for i in intervals]
    else:
        chord = generate_chord(root, "major")
    
    return chord


def generate_rhythm(total_beats, allowed_rhythms=None, allow_fractional=True):
    if allowed_rhythms is None:
        allowed_rhythms = list(RHYTHMS.keys())
    
    # Flatten the allowed rhythms into individual beat durations
    beat_options = []
    for r in allowed_rhythms:
        beat_options.extend(RHYTHMS[r])
    
    if not beat_options:
        raise ValueError("No valid rhythm options available.")
    
    sequence = []
    remaining = total_beats
    
    while remaining > 0:
        # Filter beats that don't exceed remaining (unless fractional allowed)
        valid_beats = [b for b in beat_options if b <= remaining] or beat_options
        
        chosen = random.choice(valid_beats)
        
        # If fractional allowed and chosen exceeds remaining, adjust it
        if allow_fractional and chosen > remaining:
            chosen = remaining
        
        sequence.append(round(chosen, 5))
        remaining -= chosen
    
    return sequence

def generate_polyrhythm(total_beats, instruments, allowed_rhythms=None, allow_fractional=True):
    polyrhythm = {}
    
    for inst in instruments:
        sequence = []
        remaining = total_beats
        
        # Flatten allowed rhythms
        beat_options = []
        rhythms_to_use = allowed_rhythms or list(RHYTHMS.keys())
        for r in rhythms_to_use:
            beat_options.extend(RHYTHMS[r])
        
        while remaining > 0:
            valid_beats = [b for b in beat_options if b <= remaining] or beat_options
            chosen = random.choice(valid_beats)
            
            if allow_fractional and chosen > remaining:
                chosen = remaining
            
            sequence.append(round(chosen, 5))
            remaining -= chosen
        
        polyrhythm[inst] = sequence
    
    return polyrhythm

def generate_exact_rhythm(total_length=1.0, allowed_rhythms=None, style_patterns=None):
    if allowed_rhythms is None:
        allowed_rhythms = RHYTHMS
    if style_patterns is None:
        style_patterns = RHYTHM_PATTERNS

    sequence = []
    remaining = total_length
    single_notes = sorted([v[0] for v in allowed_rhythms.values()], reverse=True)  # largest first

    while remaining > 1e-6:  # small epsilon to avoid floating-point issues
        use_pattern = style_patterns and random.random() < 0.5

        if use_pattern:
            pattern_name = random.choice(list(style_patterns.keys()))
            pattern = style_patterns[pattern_name]
            pattern_sum = sum(pattern)

            if pattern_sum <= remaining + 1e-6:
                sequence.extend(pattern)
                remaining -= pattern_sum
                continue

        # Fallback to single-note fitting
        for note in single_notes:
            if note <= remaining + 1e-6:
                sequence.append(note)
                remaining -= note
                break
        else:
            # If no standard note fits, append the remaining time as a custom tiny note
            sequence.append(remaining)
            remaining = 0

    return sequence


def generate_multi_measure_rhythm(
    measures=4,
    beats_per_measure=1.0,
    allowed_rhythms=None,
    style_patterns=None,
    style_sequence=None
):
    full_sequence = []

    for i in range(measures):
        style = None
        if style_sequence and i < len(style_sequence):
            style = style_sequence[i]

        if style and style_patterns and style in style_patterns:
            # Force use of this style for the measure
            measure_sequence = []
            remaining = beats_per_measure
            pattern = style_patterns[style]
            while remaining > 1e-6:
                pattern_sum = sum(pattern)
                if pattern_sum <= remaining + 1e-6:
                    measure_sequence.extend(pattern)
                    remaining -= pattern_sum
                else:
                    # Fit leftover with single notes
                    single_notes = sorted([v[0] for v in allowed_rhythms.values()], reverse=True)
                    for note in single_notes:
                        if note <= remaining + 1e-6:
                            measure_sequence.append(note)
                            remaining -= note
                            break
                    else:
                        measure_sequence.append(remaining)
                        remaining = 0
            full_sequence.extend(measure_sequence)
        else:
            # Generate measure freely
            full_sequence.extend(generate_exact_rhythm(
                total_length=beats_per_measure,
                allowed_rhythms=allowed_rhythms,
                style_patterns=style_patterns
            ))

    return full_sequence


def humanize_note(duration, velocity, dynamics_range=None, apply_swing=False, index_in_beat=0):
    # Timing jitter
    jitter = duration * HUMANIZATION["timing_jitter"]
    duration_human = duration + random.uniform(-jitter, jitter)

    # Swing adjustment
    if apply_swing:
        swing = HUMANIZATION["swing_strength"]
        if index_in_beat % 2 == 0:  # downbeat
            duration_human *= 1 + swing
        else:                       # upbeat
            duration_human *= 1 - swing

    # Velocity jitter
    if dynamics_range:
        min_vel, max_vel = dynamics_range
    else:
        min_vel, max_vel = 30, 127  # default MIDI range

    velocity_human = velocity + int(random.uniform(-velocity*HUMANIZATION["velocity_jitter"],
                                                    velocity*HUMANIZATION["velocity_jitter"]))
    velocity_human = max(min_vel, min(max_vel, velocity_human))  # clamp to valid MIDI range

    return duration_human, velocity_human