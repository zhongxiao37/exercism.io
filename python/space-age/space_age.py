class SpaceAge(object):
    planets = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }
    
    def __init__(self, seconds):
        self.seconds = seconds
        for pl, v in self.planets.items():
            setattr(self, 'on_' + pl, self._make_age(v))
        pass
    
    def _make_age(self, period):
        return lambda: round(self.seconds / (period * 31557600), 2)



