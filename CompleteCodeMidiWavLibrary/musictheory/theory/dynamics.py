
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