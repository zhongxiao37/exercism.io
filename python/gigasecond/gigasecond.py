from datetime import timedelta

def add(start_dt):
    new_dt = start_dt + timedelta(seconds = 10 ** 9)
    return new_dt