from music21 import converter, instrument, note, stream
import os
import random

notes = []

print("Files inside dataset:", os.listdir("dataset"))

# Read MIDI files
for file in os.listdir("dataset"):
    if file.endswith(".mid"):
        print("Reading:", file)
        midi = converter.parse("dataset/" + file)

        for element in midi.flatten().notes:   # fixed .flat
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))

print("Total notes extracted:", len(notes))

# Generate random music
generated_notes = []

for i in range(100):
    generated_notes.append(random.choice(notes))

# Convert to MIDI
offset = 0
output_notes = []

for pattern in generated_notes:
    new_note = note.Note(pattern)
    new_note.offset = offset
    output_notes.append(new_note)
    offset += 0.5

# Save output file
midi_stream = stream.Stream(output_notes)
midi_stream.write('midi', fp='output.mid')

print("🎵 Music generated successfully! Check output.mid")