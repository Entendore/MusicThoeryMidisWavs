# ultimate_music_library.py
# The Definitive Unified Music Theory & MIDI Library Generator
# FIXED: Added directory checks for Microtonal file writing.
# Dependencies: pip install pretty_midi

import os
import random
import pretty_midi
import math

# ==========================================
# 1. GLOBAL CONFIGURATION
# ==========================================
BASE_DIR = "Ultimate_Complete_Library"
ROOTS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
NOTE_NUMS = {note: 60 + i for i, note in enumerate(ROOTS)}  # C4 = 60

def ensure_dir(path):
    """Creates directory if it doesn't exist."""
    if path and not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

# ==========================================
# 2. COMPREHENSIVE THEORY DATA ENGINE
# ==========================================

# -- A. SCALES (Western & Jazz) --
SCALE_INTERVALS = {
    # Basic
    "major": [0, 2, 4, 5, 7, 9, 11],
    "minor": [0, 2, 3, 5, 7, 8, 10], # Natural
    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],
    "melodic_minor": [0, 2, 3, 5, 7, 9, 11],
    
    # Modes
    "dorian": [0, 2, 3, 5, 7, 9, 10],
    "phrygian": [0, 1, 3, 5, 7, 8, 10],
    "lydian": [0, 2, 4, 6, 7, 9, 11],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "locrian": [0, 1, 3, 5, 6, 8, 10],
    
    # Pentatonic & Blues
    "pentatonic_major": [0, 2, 4, 7, 9],
    "pentatonic_minor": [0, 3, 5, 7, 10],
    "blues": [0, 3, 5, 6, 7, 10],
    
    # Jazz / Bebop
    "bebop_dorian": [0, 2, 3, 5, 7, 9, 10, 11],
    "bebop_dominant": [0, 2, 4, 5, 7, 9, 10, 11],
    "bebop_major": [0, 2, 4, 5, 7, 8, 9, 11],
    "altered": [0, 1, 3, 4, 6, 8, 10], # Super Locrian
    "whole_tone": [0, 2, 4, 6, 8, 10],
    "diminished_whole_half": [0, 2, 3, 5, 6, 8, 9, 11],
    "diminished_half_whole": [0, 1, 3, 4, 6, 7, 9, 10],
}

# -- B. MICROTONAL SCALES (Eastern / World) --
# Uses floats: 1.5 = neutral 2nd (quarter tone), 3.5 = neutral 3rd
MICROTONAL_SCALES = {
    "maqam_rast": [0, 1.5, 3, 5, 7, 8.5, 10],          # Neutral 3rd & 7th
    "maqam_bayati": [0, 1.5, 3, 5, 7, 8, 10],          # Neutral 2nd
    "maqam_hijaz": [0, 1, 4, 5, 7, 8, 10],            # Phrygian Dominant (approx)
    "maqam_sikah": [0, 1.5, 3, 5.5, 7, 8.5, 10],       # Neutral 2nd, 4th, 6th
    "maqam_saba": [0, 1.5, 3, 4.5, 7, 8, 10],          # Specific Arabic scale
    "hungarian_minor": [0, 2, 3, 6, 7, 8, 11],         # Double Harmonic
    "persian_dastgah_shur": [0, 1, 3.5, 5, 7, 8, 10.5],
    "japanese_in_sen": [0, 1, 5, 7, 10],               # Sakura scale
    "byzantine": [0, 1, 4, 5, 7, 8, 11],               # Hijaz Kar
}

# -- C. CHORDS --
CHORD_FORMULAS = {
    # Triads
    "major": [0, 4, 7], "minor": [0, 3, 7], 
    "dim": [0, 3, 6], "aug": [0, 4, 8],
    "sus2": [0, 2, 7], "sus4": [0, 5, 7],
    
    # 7ths
    "dom7": [0, 4, 7, 10], "maj7": [0, 4, 7, 11], "min7": [0, 3, 7, 10],
    "minMaj7": [0, 3, 7, 11], "dim7": [0, 3, 6, 9], "half_dim7": [0, 3, 6, 10],
    
    # Extended
    "dom9": [0, 4, 7, 10, 14], "min9": [0, 3, 7, 10, 14], "maj9": [0, 4, 7, 11, 14],
    "dom11": [0, 4, 7, 10, 14, 17], "dom13": [0, 4, 7, 10, 14, 17, 21],
    
    # Altered
    "dom7b5": [0, 4, 6, 10], "dom7b9": [0, 4, 7, 10, 13], 
    "dom7#9": [0, 4, 7, 10, 15], "dom7alt": [0, 4, 6, 10, 14], # 7#5b9
}

# -- D. PROGRESSIONS --
PROGRESSIONS = {
    # Pop
    "pop_I_V_vi_IV": ["I", "V", "vi", "IV"],
    "pop_vi_IV_I_V": ["vi", "IV", "I", "V"],
    
    # Jazz
    "jazz_ii_V_I": ["ii", "V", "I"],
    "jazz_turnaround": ["I", "vi", "ii", "V"],
    "jazz_blues": ["I", "IV", "I", "V", "IV", "I"], # Simplified
    
    # Classical
    "circle_of_fifths": ["I", "IV", "vii", "iii", "vi", "ii", "V"],
    
    # Odd Meters (7/8 and 5/4)
    "progressive_7_8": ["i", "bVI", "bVII"], # Common metal/prog rock
    "take_five_5_4": ["i", "VII", "III", "VII"], # Minor i, bVII, bIII
}

# -- E. MAPPINGS --
ROMAN_TO_CHORD = {
    "I": (0, "major"), "ii": (2, "minor"), "iii": (4, "minor"),
    "IV": (5, "major"), "V": (7, "major"), "vi": (9, "minor"),
    "vii": (11, "dim"),
    "i": (0, "minor"), "bIII": (3, "major"), "bVI": (8, "major"),
    "bVII": (10, "major"), "VII": (11, "major")
}

DRUMS = {"kick": 36, "snare": 38, "hat": 42, "open_hat": 46, "ride": 51, "crash": 49, "tom_hi": 50, "tom_lo": 45}

ODD_METERS = {
    "5_4": [1.0, 1.0, 1.0, 1.0, 1.0],
    "7_8": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
}

# ==========================================
# 3. ADVANCED HELPER FUNCTIONS
# ==========================================

def humanize(notes, swing=False, timing_jitter=0.012, vel_jitter=5):
    """Adds human feel to MIDI data."""
    out = []
    for pitch, start, end, vel in notes:
        # Swing: delay the off-beat eighth notes
        if swing:
            pos_in_bar = start % 1.0
            if 0.45 < pos_in_bar < 0.55:
                start += 0.04
                end += 0.04
        
        # Jitter
        start += random.uniform(-timing_jitter, timing_jitter)
        vel = max(10, min(127, vel + random.randint(-vel_jitter, vel_jitter)))
        
        out.append((pitch, max(0, start), max(0, end), vel))
    return out

def create_drop_voicing(chord_notes, drop_type=2):
    """Creates Drop 2 or Drop 3 voicings for jazz piano."""
    if len(chord_notes) < 4: return chord_notes
    notes = sorted(chord_notes, reverse=True) # High to low
    
    if drop_type == 2:
        notes[1] -= 12 # Drop 2nd highest
    elif drop_type == 3:
        notes[2] -= 12 # Drop 3rd highest
        
    return sorted(notes)

def invert_chord(notes, inversion=0):
    n = notes.copy()
    for _ in range(inversion):
        n[0] += 12
        n = n[1:] + [n[0]]
    return sorted(n)

def get_progression_chords(progression_name, root_midi):
    seq = PROGRESSIONS.get(progression_name, ["I"])
    chords = []
    names = []
    for roman in seq:
        interval, ctype = ROMAN_TO_CHORD.get(roman, (0, "major"))
        formula = CHORD_FORMULAS.get(ctype, [0, 4, 7])
        chords.append([root_midi + interval + n for n in formula])
        names.append(roman)
    return chords, names

# ==========================================
# 4. MIDI WRITERS
# ==========================================

def write_standard_midi(track_data, filename, chord_markers=None, tempo=120):
    """
    Writes standard MIDI with humanization and optional chord lyrics.
    track_data: [("Instrument Name", [(pitch, start, end, vel), ...], is_drum), ...]
    """
    ensure_dir(os.path.dirname(filename))
    pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)
    
    is_swing = 'swing' in filename.lower() or 'jazz' in filename.lower()
    
    for name, notes, is_drum in track_data:
        inst = pretty_midi.Instrument(
            program=0 if is_drum else pretty_midi.instrument_name_to_program("Acoustic Grand Piano"),
            name=name, is_drum=is_drum
        )
        for p, s, e, v in humanize(notes, swing=is_swing):
            inst.notes.append(pretty_midi.Note(pitch=p, start=s, end=e, velocity=v))
        pm.instruments.append(inst)
    
    # Add chord names as lyrics (visible in DAW)
    if chord_markers:
        for time, text in chord_markers:
            pm.lyrics.append(pretty_midi.Lyric(text=text, time=time))
            
    pm.write(filename)

def write_microtonal_midi(filename, root_midi, scale_name, intervals):
    """
    Writes MIDI using Pitch Bend for quarter tones.
    Pitch Bend Range assumed: +/- 2 semitones (Standard GM default).
    1 semitone = 4096 bend units. Quarter tone = 2048.
    """
    # FIX: Ensure directory exists before writing
    ensure_dir(os.path.dirname(filename))
    
    pm = pretty_midi.PrettyMIDI()
    inst = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Violin"))
    
    time = 0.0
    for interval in intervals:
        base_note = root_midi + int(interval)
        cents = (interval % 1)
        pitch_bend_val = int(cents * 4096 * 2) # Convert fraction to bend units
        
        # Apply bend slightly before note
        inst.pitch_bends.append(pretty_midi.PitchBend(pitch_bend_val, max(0, time - 0.01)))
        inst.notes.append(pretty_midi.Note(velocity=90, pitch=base_note, start=time, end=time+1.0))
        # Reset bend after note
        inst.pitch_bends.append(pretty_midi.PitchBend(0, time + 1.1))
        
        time += 1.5
        
    pm.instruments.append(inst)
    pm.write(filename)

# ==========================================
# 5. GENERATION MODULES
# ==========================================

def generate_all_scales():
    print("1. Generating Scales (Western & Jazz)...")
    for scale_name, intervals in SCALE_INTERVALS.items():
        for root_name, root_midi in NOTE_NUMS.items():
            # Ascending and Descending
            notes_up = [(root_midi + i, i*0.5, i*0.5 + 0.4, 100) for i in intervals]
            notes_down = notes_up[::-1] # Reverse
            
            # Write file
            path = os.path.join(BASE_DIR, "01_Scales", "Western", scale_name, f"{root_name}_{scale_name}.mid")
            write_standard_midi([("Piano", notes_up + notes_down, False)], path)

    print("   + Generating Microtonal Scales (Eastern)...")
    for scale_name, intervals in MICROTONAL_SCALES.items():
        for root_name, root_midi in NOTE_NUMS.items():
            path = os.path.join(BASE_DIR, "01_Scales", "Eastern_Microtonal", scale_name, f"{root_name}_{scale_name}.mid")
            write_microtonal_midi(path, root_midi, scale_name, intervals)

def generate_all_chords():
    print("2. Generating Chords (Standard, Inversions, Jazz Voicings)...")
    for root_name, root_midi in NOTE_NUMS.items():
        for chord_name, formula in CHORD_FORMULAS.items():
            notes = [root_midi + i for i in formula]
            
            # --- Standard Block Chord ---
            path_std = os.path.join(BASE_DIR, "02_Chords", "Standard", chord_name, f"{root_name}_{chord_name}.mid")
            write_standard_midi([("Piano", [(n, 0, 2, 90) for n in notes], False)], path_std)
            
            # --- Inversions (for triads and 7ths) ---
            if len(notes) <= 4:
                for inv in range(len(notes)):
                    inv_notes = invert_chord(notes, inv)
                    # LH: Root, RH: Chord
                    lh = [(inv_notes[0]-12, 0, 2, 85)]
                    rh = [(n, 0, 2, 100) for n in inv_notes]
                    path_inv = os.path.join(BASE_DIR, "02_Chords", "Inversions", chord_name, f"{root_name}_{chord_name}_inv{inv}.mid")
                    write_standard_midi([("Left", lh, False), ("Right", rh, False)], path_inv)
            
            # --- Jazz Voicings (Drop 2 & Drop 3) ---
            if len(notes) >= 4:
                d2 = create_drop_voicing(notes, 2)
                d3 = create_drop_voicing(notes, 3)
                
                path_d2 = os.path.join(BASE_DIR, "02_Chords", "Jazz_Voicings_Drop2", chord_name, f"{root_name}_{chord_name}_drop2.mid")
                write_standard_midi([("Piano", [(n, 0, 2, 90) for n in d2], False)], path_d2)
                
                path_d3 = os.path.join(BASE_DIR, "02_Chords", "Jazz_Voicings_Drop3", chord_name, f"{root_name}_{chord_name}_drop3.mid")
                write_standard_midi([("Piano", [(n, 0, 2, 90) for n in d3], False)], path_d3)

def generate_arpeggios():
    print("3. Generating Arpeggios (Exercises)...")
    for root_name, root_midi in NOTE_NUMS.items():
        for chord_name, formula in CHORD_FORMULAS.items():
            # 1-3-5-7-5-3-1 style pattern
            notes_degrees = [formula[0], formula[1], formula[2]]
            if len(formula) > 3: notes_degrees.append(formula[3])
            
            # Create sequence
            seq = []
            time = 0.0
            pattern = notes_degrees + notes_degrees[-2::-1] # Up and Down
            
            for interval in pattern:
                seq.append((root_midi + interval, time, time+0.5, 100))
                time += 0.5
                
            path = os.path.join(BASE_DIR, "03_Arpeggios", chord_name, f"{root_name}_{chord_name}_arp.mid")
            write_standard_midi([("Piano", seq, False)], path)

def generate_progressions_backing():
    print("4. Generating Progressions & Backing Tracks...")
    
    # --- A. Standard 4/4 Progressions ---
    for prog_name, roman_seq in PROGRESSIONS.items():
        # Skip odd meters in this block
        if prog_name in ODD_METERS: continue
        
        for root_name, root_midi in NOTE_NUMS.items():
            chords, names = get_progression_chords(prog_name, root_midi)
            
            piano_notes = []
            bass_notes = []
            drum_notes = []
            markers = []
            time = 0.0
            
            # Determine Genre for Drums
            groove = "pop_rock"
            if "jazz" in prog_name: groove = "jazz_swing"
            
            for i, chord in enumerate(chords):
                markers.append((time, names[i])) # Metadata
                
                # Piano: Stride or Block
                for n in chord:
                    piano_notes.append((n, time, time+1.9, 80))
                
                # Bass: Root
                bass_notes.append((chord[0]-12, time, time+0.9, 90))
                
                # Drums: Simple Beat
                if groove == "pop_rock":
                    drum_notes.append((DRUMS["kick"], time, time+0.1, 100))
                    drum_notes.append((DRUMS["snare"], time+1.0, time+1.1, 100))
                    drum_notes.append((DRUMS["hat"], time, time+0.1, 80))
                    drum_notes.append((DRUMS["hat"], time+0.5, time+0.6, 80))
                    drum_notes.append((DRUMS["hat"], time+1.0, time+1.1, 80))
                    drum_notes.append((DRUMS["hat"], time+1.5, time+1.6, 80))
                else: # Jazz
                    drum_notes.append((DRUMS["ride"], time, time+0.1, 90))
                    drum_notes.append((DRUMS["ride"], time+0.66, time+0.76, 80))
                
                time += 2.0 # 2 beats per chord

            filename = os.path.join(BASE_DIR, "04_Progressions", "Standard_4_4", prog_name, f"{root_name}_{prog_name}.mid")
            write_standard_midi([("Piano", piano_notes, False), ("Bass", bass_notes, False), ("Drums", drum_notes, True)], 
                               filename, chord_markers=markers)

    # --- B. Odd Meter Progressions ---
    for meter_name, durations in ODD_METERS.items():
        # Use a fixed progression for odd meters
        # Attempt to find the specific progression name, else default to first
        prog_key_name = f"progressive_{meter_name}"
        if prog_key_name not in PROGRESSIONS:
            prog_key_name = list(PROGRESSIONS.keys())[0] # Fallback
            
        chords, names = get_progression_chords(prog_key_name, NOTE_NUMS["C"])
        
        piano, bass, drums = [], [], []
        time = 0.0
        bar_len = sum(durations)
        
        for i, chord in enumerate(chords):
            # Piano
            for n in chord: piano.append((n, time, time+bar_len-0.1, 80))
            # Bass
            bass.append((chord[0]-12, time, time+1.0, 90))
            
            # Drums for Odd Meter
            t = 0.0
            for dur in durations:
                if t == 0.0: drums.append((DRUMS["kick"], time+t, time+t+0.1, 100))
                if t >= 1.0: drums.append((DRUMS["snare"], time+t, time+t+0.1, 80)) # Simplified
                drums.append((DRUMS["hat"], time+t, time+t+0.1, 70))
                t += dur
            
            time += bar_len
            
        filename = os.path.join(BASE_DIR, "04_Progressions", "Odd_Meters", f"C_{meter_name}_Track.mid")
        write_standard_midi([("Piano", piano, False), ("Bass", bass, False), ("Drums", drums, True)], filename)

def generate_piano_etudes():
    print("5. Generating Piano Etudes (Walking Bass, Counterpoint)...")
    
    for root_name, root_midi in NOTE_NUMS.items():
        # --- Jazz Walking Bass Etude ---
        chords, _ = get_progression_chords("jazz_ii_V_I", root_midi)
        rh, lh = [], []
        time = 0.0
        
        for chord in chords * 2: # 2 choruses
            # RH: Comping (Stabs on beats 2 and 4)
            voiced = create_drop_voicing(chord, 2)
            rh.extend([(n, time+1.0, time+1.9, 80) for n in voiced]) # Beat 2
            rh.extend([(n, time+3.0, time+3.9, 80) for n in voiced]) # Beat 4
            
            # LH: Walking Bass (Randomized)
            walk_pattern = [chord[0]-12, chord[0]-12+4, chord[0]-12+7, chord[0]-12+random.choice([2,9,11])]
            for i, note in enumerate(walk_pattern):
                lh.append((note, time+i, time+i+0.9, 85))
            
            time += 4.0
            
        path_jazz = os.path.join(BASE_DIR, "05_Piano_Etudes", "Jazz_Walking", f"{root_name}_ii_V_I.mid")
        write_standard_midi([("Right_Hand", rh, False), ("Left_Hand", lh, False)], path_jazz)
        
        # --- Classical Counterpoint Etude ---
        scale = SCALE_INTERVALS["major"]
        notes_scale = [root_midi + i for i in scale]
        
        rh_cp, lh_cp = [], []
        time = 0.0
        for i in range(8): # 8 bars
            # LH: Bass line
            lh_cp.append((notes_scale[0]-12, time, time+2.0, 80))
            lh_cp.append((notes_scale[4]-12, time+2.0, time+4.0, 80))
            
            # RH: Melody (Contrary motion)
            rh_cp.append((notes_scale[i % 7], time, time+1.0, 100))
            rh_cp.append((notes_scale[(i+2) % 7], time+1.0, time+2.0, 100))
            rh_cp.append((notes_scale[(i+4) % 7], time+2.0, time+3.0, 100))
            
            time += 4.0
            
        path_cp = os.path.join(BASE_DIR, "05_Piano_Etudes", "Classical_Counterpoint", f"{root_name}_Counterpoint.mid")
        write_standard_midi([("Right_Hand", rh_cp, False), ("Left_Hand", lh_cp, False)], path_cp)

# ==========================================
# 6. MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    print("====================================================")
    print("  ULTIMATE MUSIC LIBRARY GENERATOR")
    print("  Western | Eastern | Jazz | Classical | Odd Meters")
    print("====================================================")
    
    # Run all modules
    generate_all_scales()
    generate_all_chords()
    generate_arpeggios()
    generate_progressions_backing()
    generate_piano_etudes()
    
    print("\n✅ GENERATION COMPLETE.")
    print(f"Library Location: {os.path.abspath(BASE_DIR)}")
    print("----------------------------------------------------")
    print("Folder Structure:")
    print("  01_Scales/")
    print("    -> Western (Modes, Jazz, Pentatonic)")
    print("    -> Eastern_Microtonal (Maqam, Ragas with Pitch Bend)")
    print("  02_Chords/")
    print("    -> Standard, Inversions, Jazz_Voicings (Drop 2/3)")
    print("  03_Arpeggios/")
    print("  04_Progressions/")
    print("    -> Standard_4_4 (Pop, Jazz, Blues)")
    print("    -> Odd_Meters (5/4, 7/8)")
    print("  05_Piano_Etudes/")
    print("    -> Jazz_Walking, Classical_Counterpoint")