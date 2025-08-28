import unittest
import math

class TestMusicNotes(unittest.TestCase):
    def setUp(self):
        self.music = MusicNotes()

    def test_note_to_midi(self):
        self.assertEqual(self.music.note_to_midi("C4"), 60.0)
        self.assertEqual(self.music.note_to_midi("C+4"), 60.5)
        self.assertEqual(self.music.note_to_midi("A4"), 69.0)
        with self.assertRaises(ValueError):
            self.music.note_to_midi("X4")  # Invalid note

    def test_midi_to_note(self):
        self.assertEqual(self.music.midi_to_note(60), "C")
        self.assertEqual(self.music.midi_to_note(61, prefer_flats=True), "Db")
        self.assertEqual(self.music.midi_to_note(61, prefer_sharps=True), "C#")
        self.assertEqual(self.music.midi_to_note(60, prefer_natural=True), "C")
        self.assertEqual(self.music.midi_to_note(60.5), "C+")

    def test_midi_to_note_with_cents(self):
        note, cents = self.music.midi_to_note_with_cents(60.25)
        self.assertEqual(note, "C")
        self.assertAlmostEqual(cents, 25.0)  # 0.25 semitones = 25 cents

    def test_note_to_freq(self):
        self.assertAlmostEqual(self.music.note_to_freq("A4"), 440.0)
        self.assertAlmostEqual(self.music.note_to_freq("C4"), 261.6255653005986)
        self.assertAlmostEqual(self.music.note_to_freq("C+4", a4_freq=432), 256.8687833188579)

    def test_freq_to_note(self):
        self.assertEqual(self.music.freq_to_note(440.0), "A")
        self.assertEqual(self.music.freq_to_note(261.6255653005986), "C")
        self.assertEqual(self.music.freq_to_note(440.0, a4_freq=432, prefer_sharps=True), "A#")

    def test_transpose(self):
        self.assertEqual(self.music.transpose("C4", 2), "D")
        self.assertEqual(self.music.transpose("C4", 0.5), "C+")
        self.assertEqual(self.music.transpose("G#4", -1, prefer_flats=True), "Ab")

    def test_interval(self):
        self.assertEqual(self.music.interval("C4", "E4"), 4.0)
        self.assertEqual(self.music.interval("C4", "C+4"), 0.5)
        self.assertEqual(self.music.interval_cents("C4", "E4"), 400.0)

    def test_list_octave_notes(self):
        notes = self.music.list_octave_notes(4)
        self.assertIn("C4", notes)
        self.assertIn("C+4", notes)
        self.assertEqual(len(notes), 22)  # 12 standard + 10 microtones
        self.assertEqual(notes[0], "C4")  # First note
        self.assertEqual(notes[-1], "B4")  # Last note

    def test_sort_notes(self):
        notes = ["E4", "C4", "G4"]
        sorted_notes = self.music.sort_notes(notes)
        self.assertEqual(sorted_notes, ["C4", "E4", "G4"])

if __name__ == "__main__":
    unittest.main()