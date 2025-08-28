
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


