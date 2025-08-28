# ============================
# Core theory data, mappings, and genre presets
# ============================

# ----------------------------
# NOTES & ROOTS
# ----------------------------
ROOTS = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
NOTE_NUMS = {
    "C":60,"C#":61,"Db":61,"D":62,"D#":63,"Eb":63,
    "E":64,"F":65,"F#":66,"Gb":66,"G":67,"G#":68,
    "Ab":68,"A":69,"A#":70,"Bb":70,"B":71
}
BASE_NOTE_NUMS = {
    "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3,
    "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8,
    "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11
}


# ----------------------------
# CHORD FORMULAS
# ----------------------------
CHORD_FORMULAS = {
    "major":[0,4,7], "minor":[0,3,7], 
    "major6":[0,4,7,9], "minor6":[0,3,7,9], "minor7":[0,3,7,10], "major7":[0,4,7,11], "minor9":[0,3,7,10,14], "major9":[0,4,7,11,14],
    "dominant":[0,4,7], "dominant7":[0,4,7,10], "dominant9":[0,4,7,10,14], "dominant11":[0,4,7,10,14,17], "dominant13":[0,4,7,10,14,17,21],
    "sus2":[0,2,7], "sus4":[0,5,7], 
    "6":[0,4,7,9],"7":[0,4,7,11], "9":[0,4,7,10,14], "11":[0,4,7,10,14,17], "13":[0,4,7,10,14,17,21],
    "add9":[0,4,7,14],
    "power":[0,7], "power9":[0,7,14], "power11":[0,7,14,17], "power13":[0,7,14,17,21], 
    "augmented":[0,4,8], "diminished":[0,3,6], "half_diminished":[0,3,6],
    "augmented7":[0,4,8,11], "diminished7":[0,3,6,9], "half_diminished7":[0,3,6,10],
    "augmented9":[0,4,8,14], "diminished9":[0,3,6,10,14], "half_diminished9":[0,3,6,10,14],
    "augmented11":[0,4,8,14,17], "diminished11":[0,3,6,10,14,17], "half_diminished11":[0,3,6,10,14,17],
    "augmented13":[0,4,8,14,17,21], "diminished13":[0,3,6,10,14,17,21], "half_diminished13":[0,3,6,10,14,17,21]
}

# ----------------------------
# SCALE INTERVALS
# ----------------------------
SCALE_INTERVALS = {
    "major":[0,2,4,5,7,9,11],
    "minor":[0,2,3,5,7,8,10],
    "harmonic_minor":[0,2,3,5,7,8,11],
    "melodic_minor":[0,2,3,5,7,9,11],
    "pentatonic_major":[0,2,4,7,9],
    "pentatonic_minor":[0,3,5,7,10],
    "whole_tone":[0,2,4,6,8,10],
    "chromatic":list(range(12)),
    "blues":[0,3,5,6,7,10],
    "neapolitan_minor":[0,1,3,5,7,8,11],
    "hungarian_minor":[0,2,3,6,7,8,11],
}

# ----------------------------
# MODES
# ----------------------------
MODES = {
    "ionian": SCALE_INTERVALS["major"],
    "dorian": [0,2,3,5,7,9,10],
    "phrygian": [0,1,3,5,7,8,10],
    "lydian": [0,2,4,6,7,9,11],
    "mixolydian": [0,2,4,5,7,9,10],
    "aeolian": SCALE_INTERVALS["minor"],
    "locrian": [0,1,3,5,6,8,10],
}

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

# ----------------------------
# HARMONIC PROGRESSIONS
# ----------------------------
ROMAN_TO_CHORD = {
    "I":(0,"major"), "ii":(2,"minor"), "iii":(4,"minor"),
    "IV":(5,"major"), "V":(7,"major"), "vi":(9,"minor"),
    "vii°":(11,"diminished"),
    "i":(0,"minor"), "bIII":(3,"major"), "bVII":(10,"major"),
    "III":(4,"major"), "VI":(9,"major"), "VII":(11,"major"),
}

ROMAN_CHORD_QUALITY = {
    "I": "major",      "i": "minor",
    "II": "major",     "ii": "minor",
    "III": "major",    "iii": "minor",
    "IV": "major",     "iv": "minor",
    "V": "major",      "v": "minor",
    "VI": "major",     "vi": "minor",
    "VII": "major",    "vii": "minor",
    
    "vii°": "dim",     "ii°": "dim",    
    "V7": "7",         "I7": "7",      
    "maj7": "maj7",    "min7": "min7",  
    
    "bII": "major",    "bVI": "major", 
    "bVII": "major",
}

ROMAN_TO_DEGREE = {
    "I": 0, "i": 0,
    "II": 1, "ii": 1,
    "III": 2, "iii": 2,
    "IV": 3, "iv": 3,
    "V": 4, "v": 4,
    "VI": 5, "vi": 5,
    "VII": 6, "vii": 6,
    "bII": 1, "biii": 2, "bVI": 5, "bVII": 6, "bII°": 1  # flats
}

# Humanization ranges (to avoid robotic feel)
HUMANIZATION = {
    "timing_jitter": 0.02,   # up to ±2% offset in rhythm
    "velocity_jitter": 0.05, # up to ±5% change in dynamics
    "swing_strength": 0.15   # push-pull feel for swing
}

# Dynamics levels (MIDI velocity ranges)
DYNAMICS = {
    "ppp": (15,29),   # pianississimo, extremely soft
    "pp":  (30,45),   # pianissimo
    "p":   (46,60),   # piano
    "mp":  (61,75),   # mezzo-piano
    "mf":  (76,90),   # mezzo-forte
    "f":   (91,105),  # forte
    "ff":  (106,120), # fortissimo
    "fff": (121,127), # fortississimo, maximum
}

# Optional expressive dynamics
EXPRESSIVE_DYNAMICS = {
    "sfz": (100,110), # sforzando, sudden accent
    "fp":  (80,95),   # forte-piano, loud then immediately soft
    "crescendo": None, # dynamic change, handled algorithmically
    "decrescendo": None,
}

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


# === Genres ===
GENRES = {
    "Jazz":["jazz_ii-V-I","jazz_turnaround"],
    "Pop":["pop_axis"],
    "Blues":["blues_12bar"],
    "Funk":["funk_jam"],
    "EDM":["edm_drop"],
    "Latin":["latin_salsa"],
    "Orchestral":["film_epic"],
}

# DRUMS
DRUMS = {
    "kick":36,"snare":38,"closed_hat":42,"open_hat":46,
    "ride":51,"crash":49,"tom_low":45,"tom_mid":47,"tom_high":50,
    "clap":39,"rim":37,"cowbell":56,"conga":64,"bongo":60
}

DRUM_GROOVES = {
    "pop":[("kick",0.0),("snare",1.0),("snare",3.0),
           *[("closed_hat",x*0.5) for x in range(8)]],
    "rock":[("kick",0.0),("kick",2.0),("snare",1.0),("snare",3.0),
            *[("closed_hat",x*0.5) for x in range(8)]],
    "jazz":[("ride",i) for i in [0.0,0.5,1.0,2.0,2.5,3.0]],
    "funk":[("kick",0.0),("snare",1.0),("snare",2.5),
            *[("closed_hat",i*0.25) for i in range(16)]],
    "edm":[("kick",i) for i in [0,1,2,3]],
    "latin":[("conga",0.5),("cowbell",1.0),("bongo",2.5)],
    "orchestral":[("kick",0.0),("snare",3.0),("crash",0.0)],
}

# BASS PATTERNS
BASS_PATTERNS = {
    "pop":[0,0,0,0],
    "rock":[0,7,0,7],
    "jazz":[0,4,7,11],   # R-3-5-7
    "funk":[0,7,0,5],
    "edm":[0,0,0,0],
    "latin":[0,7,5,7],
    "orchestral":[0,0,7,0],
    "walking":[0,2,4,5], # stepwise
}

# ----------------------------
# SONG STRUCTURES
# ----------------------------
SONG_STRUCTURES = {
    "pop":["intro","verse","chorus","verse","chorus","bridge","chorus","outro"],
    "jazz":["intro","head","solo","head","outro"],
    "blues":["intro","chorus","chorus","solo","chorus","outro"],
    "edm":["intro","build","drop","break","drop","outro"],
    "film":["intro","theme","variation","climax","resolution"],
}

SECTION_PROGS = {
    "intro":["I","V","vi","IV"],
    "verse":["I","V","vi","IV"],
    "chorus":["vi","IV","I","V"],
    "bridge":["IV","V","iii","vi"],
    "drop":["vi","IV","I","V"],
    "build":["I","ii","IV","V"],
    "outro":["I","I","I","I"]
}

# INSTRUMENTS
GENRE_INSTRUMENTS = {
    "pop":{"piano":0,"bass":33,"melody":81},
    "rock":{"guitar":29,"bass":34,"drums":0},
    "jazz":{"piano":0,"bass":32,"melody":65},
    "blues":{"guitar":26,"bass":34,"melody":27},
    "funk":{"epiano":4,"bass":33,"melody":81},
    "edm":{"lead":81,"bass":38,"pad":89},
    "latin":{"piano":0,"bass":33,"melody":73,"perc":12},
    "orchestral":{"strings":48,"bass":43,"melody":40,"brass":61,"woodwinds":73},
    "film":{"strings":48,"brass":61,"choir":52,"perc":117},
}

# ============================
# EXPRESSIVE PLAYING LAYERS
# ============================

# Articulation styles (velocity multipliers and note length multipliers)
ARTICULATIONS = {
    "legato": {"length":1.1, "velocity":1.0},   # smooth, connected
    "staccato": {"length":0.5, "velocity":0.9}, # short, detached
    "accent": {"length":1.0, "velocity":1.3},   # strong emphasis
    "tenuto": {"length":1.0, "velocity":1.1},   # held, slightly emphasized
    "ghost": {"length":0.7, "velocity":0.5},    # soft/hidden note
    "marcato": {"length":0.9, "velocity":1.4},  # sharp attack
    "swell": {"length":1.5, "velocity":[0.6,0.8,1.2]}, # gradual crescendo
}



# Orchestration layers (per genre / style)
ORCHESTRATION = {
    "orchestral": {
        "strings":["violins","violas","cellos","basses"],
        "brass":["trumpets","horns","trombones","tuba"],
        "woodwinds":["flutes","clarinets","oboes","bassoons"],
        "percussion":["timpani","cymbals","snare"]
    },
    "jazz_bigband": {
        "saxes":["alto sax","tenor sax","baritone sax"],
        "brass":["trumpets","trombones"],
        "rhythm":["piano","bass","drums","guitar"]
    },
    "edm_layers": {
        "lead":["supersaw","plucked synth"],
        "bass":["sub","growl"],
        "pads":["strings pad","choir pad"],
        "fx":["risers","impacts"]
    }
}

# Ornamentation (extra notes between chords/melody)
ORNAMENTS = {
    "grace": {"offset":-0.1, "length":0.2}, # short before note
    "mordent": {"pattern":[0,-1,0]},        # note → below → note
    "trill": {"pattern":[0,1,0,1,0]},       # fast alternation
    "turn": {"pattern":[1,0,-1,0]},         # above → note → below → note
    "slide": {"pattern":"gliss"},           # continuous slide
}

# Instrument articulations (per instrument family)
INSTRUMENT_TECHNIQUES = {
    "strings": ["pizzicato","legato","spiccato","tremolo"],
    "brass": ["staccato","legato","sforzando","mute"],
    "woodwinds": ["flutter","slur","staccato","breathy"],
    "guitar": ["palm_mute","slide","bend","harmonics"],
    "drums": ["rimshot","roll","flam","ghost"],
    "synth": ["filter_sweep","lfo_vibrato","arp","glide"]
}



# ============================
# GENRE PERFORMANCE PROFILES
# ============================

GENRE_EXPRESSIONS = {
    "pop": {
        "articulations": ["legato","accent"],
        "dynamics": "mf",
        "swing": False,
        "humanization": {"timing_jitter":0.01,"velocity_jitter":0.03},
        "ornaments": []
    },
    "rock": {
        "articulations": ["staccato","accent"],
        "dynamics": "f",
        "swing": False,
        "humanization": {"timing_jitter":0.02,"velocity_jitter":0.05},
        "ornaments": ["slide","grace"]
    },
    "jazz": {
        "articulations": ["swing","ghost","accent"],
        "dynamics": "mp",
        "swing": True,
        "humanization": {"timing_jitter":0.03,"velocity_jitter":0.07},
        "ornaments": ["grace","mordent","trill"]
    },
    "blues": {
        "articulations": ["slide","ghost","accent"],
        "dynamics": "mf",
        "swing": True,
        "humanization": {"timing_jitter":0.025,"velocity_jitter":0.06},
        "ornaments": ["bend","grace"]
    },
    "funk": {
        "articulations": ["staccato","accent","ghost"],
        "dynamics": "mf",
        "swing": True,
        "humanization": {"timing_jitter":0.02,"velocity_jitter":0.08},
        "ornaments": ["grace","mordent"]
    },
    "edm": {
        "articulations": ["staccato","accent"],
        "dynamics": "ff",
        "swing": False,
        "humanization": {"timing_jitter":0.005,"velocity_jitter":0.02},
        "ornaments": ["filter_sweep","arp"]
    },
    "latin": {
        "articulations": ["accent","legato"],
        "dynamics": "f",
        "swing": False,
        "humanization": {"timing_jitter":0.02,"velocity_jitter":0.05},
        "ornaments": ["grace","trill","turn"]
    },
    "orchestral": {
        "articulations": ["legato","tenuto","marcato"],
        "dynamics": "mf",
        "swing": False,
        "humanization": {"timing_jitter":0.015,"velocity_jitter":0.04},
        "ornaments": ["trill","turn","swell"]
    },
    "film": {
        "articulations": ["legato","swell","marcato"],
        "dynamics": "f",
        "swing": False,
        "humanization": {"timing_jitter":0.02,"velocity_jitter":0.05},
        "ornaments": ["swell","trill","gliss"]
    }
}

# ============================
# TEMPO RANGES (by genre)
# ============================
GENRE_TEMPOS = {
    "pop": (90,120),
    "rock": (100,140),
    "jazz": (60,160),
    "blues": (70,110),
    "funk": (90,120),
    "edm": (120,140),
    "latin": (90,130),
    "orchestral": (60,100),
    "film": (60,120),
}

# ============================
# AUTOMATIC DYNAMICS CURVES
# ============================
DYNAMIC_CURVES = {
    "crescendo":[0.6,0.7,0.85,1.0],
    "diminuendo":[1.0,0.85,0.7,0.6],
    "swell":[0.6,0.9,1.1,0.9],
    "pulse":[0.8,1.0,0.8,1.0]
}

# ============================
# GENRE → DEFAULT LAYERS
# (structure + instruments + expressions)
# ============================
GENRE_DEFAULTS = {
    "pop": {
        "structure": SONG_STRUCTURES["pop"],
        "instruments": GENRE_INSTRUMENTS["pop"],
        "expressions": GENRE_EXPRESSIONS["pop"]
    },
    "jazz": {
        "structure": SONG_STRUCTURES["jazz"],
        "instruments": GENRE_INSTRUMENTS["jazz"],
        "expressions": GENRE_EXPRESSIONS["jazz"]
    },
    "blues": {
        "structure": SONG_STRUCTURES["blues"],
        "instruments": GENRE_INSTRUMENTS["blues"],
        "expressions": GENRE_EXPRESSIONS["blues"]
    },
    "funk": {
        "structure": SONG_STRUCTURES["pop"],  # similar verse/chorus
        "instruments": GENRE_INSTRUMENTS["funk"],
        "expressions": GENRE_EXPRESSIONS["funk"]
    },
    "edm": {
        "structure": SONG_STRUCTURES["edm"],
        "instruments": GENRE_INSTRUMENTS["edm"],
        "expressions": GENRE_EXPRESSIONS["edm"]
    },
    "latin": {
        "structure": SONG_STRUCTURES["pop"], # verse/chorus with percussive breaks
        "instruments": GENRE_INSTRUMENTS["latin"],
        "expressions": GENRE_EXPRESSIONS["latin"]
    },
    "orchestral": {
        "structure": SONG_STRUCTURES["film"],
        "instruments": GENRE_INSTRUMENTS["orchestral"],
        "expressions": GENRE_EXPRESSIONS["orchestral"]
    },
    "film": {
        "structure": SONG_STRUCTURES["film"],
        "instruments": GENRE_INSTRUMENTS["film"],
        "expressions": GENRE_EXPRESSIONS["film"]
    }
}


# ============================
# MODULATION & KEY CHANGE PRESETS
# ============================

# Common modulation types
MODULATIONS = {
    "relative_minor": {"from":"major","to":"minor","shift":-3},   # C major → A minor
    "relative_major": {"from":"minor","to":"major","shift":+3},   # A minor → C major
    "parallel_minor": {"from":"major","to":"minor","shift":0},    # C major → C minor
    "parallel_major": {"from":"minor","to":"major","shift":0},    # C minor → C major
    "dominant_pivot": {"from":"any","to":"any","shift":+7},       # tonic → V of new key
    "subdominant_pivot": {"from":"any","to":"any","shift":+5},    # tonic → IV of new key
    "chromatic_mediant": {"from":"any","to":"any","shift":+4},    # C → E major/minor
    "tritone_sub": {"from":"jazz","to":"jazz","shift":+6},        # Jazz V7 → bII7
    "picardy_third": {"from":"minor","to":"major","shift":0},     # minor → major final chord
    "key_lift": {"from":"pop","to":"pop","shift":+2},             # + whole step for excitement
    "film_dramatic": {"from":"minor","to":"major","shift":+3},    # minor → relative major → up whole step
}

# Example modulation chains by genre
GENRE_MODULATIONS = {
    "pop": [
        ["I","V","vi","IV"],    # main
        "key_lift",             # up a whole step
        ["I","V","vi","IV"]     # repeat in new key
    ],
    "jazz": [
        ["ii","V","I"],         # base
        "tritone_sub",          # ii → V (sub)
        ["ii","V","I"]          # resolution in new key
    ],
    "film": [
        ["i","VI","III","VII"], # dark intro
        "film_dramatic",        # modulation
        ["I","V","vi","IV"]     # brighter resolution
    ],
    "blues": [
        ["I","IV","I","V"],     # basic
        "parallel_minor",       # bluesy minor modulation
        ["i","bVII","IV","i"]
    ],
    "orchestral": [
        ["I","V","vi","iii"],   # theme
        "dominant_pivot",       # modulate to new tonic
        ["I","IV","V","I"]
    ]
}

# ============================
# CADENCES
# ============================
CADENCES = {
    "perfect":["V","I"],          # strong resolution
    "plagal":["IV","I"],          # church "Amen"
    "deceptive":["V","vi"],       # surprise
    "half":["I","V"],             # unresolved
    "phrygian":["iv","V"],        # minor, Spanish flavor
    "blues_turnaround":["I","vi","ii","V"], # 12-bar loop close
}

# ============================
# EXTENDED GENRE DEFAULTS (with modulation & cadences)
# ============================
for g in GENRE_DEFAULTS:
    GENRE_DEFAULTS[g]["modulations"] = GENRE_MODULATIONS.get(g, [])
    GENRE_DEFAULTS[g]["cadences"] = ["perfect","deceptive"] if g in ["pop","rock","edm"] else ["perfect","plagal"]


# ============================
# TEXTURE & DENSITY LAYERS
# ============================

# Arrangement density levels
TEXTURE_LEVELS = {
    "sparse": {
        "instruments": 1,        # solo / minimal
        "register_spread": 1,    # very narrow range
        "rhythmic_density": 0.3, # fewer notes
        "articulation": "legato",
        "dynamics": "p"
    },
    "light": {
        "instruments": 2-3,
        "register_spread": 2,
        "rhythmic_density": 0.5,
        "articulation": "tenuto",
        "dynamics": "mp"
    },
    "medium": {
        "instruments": 4-6,
        "register_spread": 3,
        "rhythmic_density": 0.7,
        "articulation": "mixed",
        "dynamics": "mf"
    },
    "thick": {
        "instruments": 6-10,
        "register_spread": 4,
        "rhythmic_density": 0.9,
        "articulation": "accent",
        "dynamics": "f"
    },
    "wall_of_sound": {
        "instruments": 10+,
        "register_spread": 5,   # huge (low bass to high strings/brass)
        "rhythmic_density": 1.0,
        "articulation": "marcato",
        "dynamics": "ff"
    }
}

# Genre → default texture curve (verse → chorus → bridge → climax)
GENRE_TEXTURE_CURVES = {
    "pop": ["sparse","light","medium","thick","wall_of_sound"],
    "rock": ["light","medium","thick","wall_of_sound"],
    "jazz": ["sparse","light","medium"], # jazz rarely goes wall-of-sound
    "edm": ["sparse","medium","wall_of_sound"], # build-up → drop
    "film": ["sparse","light","medium","thick","wall_of_sound"], # full arc
    "orchestral": ["light","medium","thick","wall_of_sound"],    # always layered
    "blues": ["sparse","light","medium"], # intimate texture
}

# Register spread presets (octave ranges for instruments)
REGISTER_SPREADS = {
    1: {"low":(60,72), "high":(60,72)},   # same octave
    2: {"low":(48,60), "high":(72,84)},   # ~2 octave split
    3: {"low":(36,60), "high":(72,96)},   # ~3-4 octaves
    4: {"low":(28,55), "high":(80,100)},  # very wide
    5: {"low":(21,48), "high":(84,108)},  # max orchestral span
}

# Rhythmic density meaning (probability of subdivision use)
RHYTHM_DENSITY = {
    0.3: {"allowed_subdivisions":["quarter","half"]},
    0.5: {"allowed_subdivisions":["quarter","eighth"]},
    0.7: {"allowed_subdivisions":["eighth","sixteenth"]},
    0.9: {"allowed_subdivisions":["eighth","sixteenth","triplets"]},
    1.0: {"allowed_subdivisions":["sixteenth","32nd","syncopation"]}
}