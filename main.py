import mido
from mido import MidiFile, MidiTrack, Message
import random

def create_chord_progression():
    chords = [
        [48, 52, 55],  # C Major
        [45, 48, 52],  # A Minor
        [43, 47, 50],  # G Major
        [41, 45, 48],  # E Minor
    ]
    progression = random.sample(chords, len(chords))
    return progression

def create_melody(chord):
    return random.choice(chord)

def create_midi_file(filename, tempo=80):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=26, time=0))  # Synth pad
    ticks_per_beat = mid.ticks_per_beat
    ticks_per_measure = ticks_per_beat * 4
    ticks_per_chord = ticks_per_measure // len(create_chord_progression())

    for chord in create_chord_progression():
        for note in chord:
            track.append(Message('note_on', note=note, velocity=64, time=0))
            track.append(Message('note_off', note=note, velocity=64, time=ticks_per_chord))

    track.append(Message('program_change', program=1, time=0))  # Acoustic grand piano
    for chord in create_chord_progression():
        melody_note = create_melody(chord)
        track.append(Message('note_on', note=melody_note, velocity=64, time=0))
        track.append(Message('note_off', note=melody_note, velocity=64, time=ticks_per_chord))

    track.append(Message('control_change', channel=0, control=64, value=127, time=0))  # Sustain pedal on
    track.append(Message('control_change', channel=0, control=64, value=0, time=ticks_per_measure))  # Sustain pedal off

    mid.save(filename)

if __name__ == "__main__":
    filename = "Pete_Namlook_Style.mid"
    create_midi_file(filename)
    print(f"MIDI file '{filename}' has been created.")
