from pydub import AudioSegment

# Input audio file to be sliced
audio = AudioSegment.from_wav('Song Location')

# Length of the audiofile in milliseconds
n = len(audio)

# Variable to count the number of sliced chunks
counter = 1

start = [1732.5, 1800.6, 1810.3, 5000.0]
end = [1800.5, 1810.2, 1900.7, 15000.0]


for i in range(len(start)):

    chunk = audio[start[i]:end[i]]

    # Filename / Path to store the sliced audio
    filename = 'chunk' + str(counter) + '.wav'

    # Store the sliced audio file to the defined path
    chunk.export(filename, format="wav")
    # Print information about the current chunk
    print("Processing chunk " + str(counter) + ". Start = "
          + str(start) + " end = " + str(end))

    # Increment counter for the next chunk
    counter = counter + 1