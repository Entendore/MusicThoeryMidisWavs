
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

# Ornamentation (extra notes between chords/melody)
ORNAMENTS = {
    "grace": {"offset":-0.1, "length":0.2}, # short before note
    "mordent": {"pattern":[0,-1,0]},        # note → below → note
    "trill": {"pattern":[0,1,0,1,0]},       # fast alternation
    "turn": {"pattern":[1,0,-1,0]},         # above → note → below → note
    "slide": {"pattern":"gliss"},           # continuous slide
}
