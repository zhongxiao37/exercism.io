
CHROMATIC_SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
CHROMATIC_FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

class Scale(object):
    def __init__(self, tonic):
        self.tonic = tonic
        self.use_flat = self.tonic in ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb']

    def chromatic(self):
        if self.use_flat:
            tonic_index = CHROMATIC_FLATS.index(str.capitalize(self.tonic))
            raw_pitches = CHROMATIC_FLATS[tonic_index:] + CHROMATIC_FLATS[0:tonic_index]
        else:
            tonic_index = CHROMATIC_SHARPS.index(str.capitalize(self.tonic))
            raw_pitches = CHROMATIC_SHARPS[tonic_index:] + CHROMATIC_SHARPS[0:tonic_index]
        
        return raw_pitches
    

    def interval(self, intervals):
        raw_pitches = self.chromatic()
        offset_index = {'m': 1, 'M': 2, 'A': 3}
        offset = 0
        pitches_ = []
        for i in intervals:
            pitches_.append(raw_pitches[offset])
            offset += offset_index[i]

        return pitches_
