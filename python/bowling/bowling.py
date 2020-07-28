from functools import reduce

class BowlingGame(object):
    def __init__(self):
        self.frames = []

    def roll(self, pins):
        if pins > 10 or pins < 0:
            raise ValueError('invalid pins')
        if len(self.frames) > 10:
            if len(self.frames[9]) == 2 and len(self.frames[10]) >= 1:
                raise IndexError('Spare should not have two bonus')
            elif len(self.frames[9]) == 1 and len(self.frames[10]) >= 2:
                raise IndexError('Strike should not have more than two bonus')

        if len(self.frames) == 0 or len(self.frames[-1]) == 2 or sum(self.frames[-1]) == 10:
            # last frame was finished
            self.frames.append([pins])
        else:
            self.frames[-1].append(pins)
        
        if any(sum(frame) > 10 for frame in self.frames):
            raise ValueError('invalid score')
        if len(self.frames) > 10:
            if sum(self.frames[9]) != 10:
                raise IndexError('Frame 10 is not a Strike or Spare')

    def score(self):
        if len(self.frames) < 10:
            raise IndexError('frame length is less than 10')
        
        if sum(self.frames[9]) == 10:
            if len(self.frames) <= 10 or len([e for frame in self.frames[9:] for e in frame]) != 3:
                raise IndexError('Bonus frame is invalid')

        frame_scores = []
        for i in range(10):
            frame = self.frames[i]
            if sum(frame) == 10:
                if len(frame) == 1:
                    frame_scores.append(10 + sum([e for frame in self.frames[i+1:] for e in frame][:2]))
                else:
                    frame_scores.append(10 + self.frames[i+1][0])
            else:
                frame_scores.append(sum(frame))
        
        return sum(frame_scores)
