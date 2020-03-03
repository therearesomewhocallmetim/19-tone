import numpy
import scipy.signal
import time


import pygame, pygame.sndarray

pygame.init()

def play(sample_wave, ms):
    """Play the given NumPy array, as a sound, for ms milliseconds."""
    sample_wave = numpy.resize(sample_wave, (sample_wave.shape[0], 2))
    sound = pygame.sndarray.make_sound(sample_wave)
    sound.play(-1)
    pygame.time.delay(ms)
    sound.stop()

sample_rate = 44100

def sine_wave(hz, peak, n_samples=sample_rate):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    length = sample_rate / float(hz)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(length)) * omega
    onecycle = peak * numpy.sin(xvalues)
    x = numpy.resize(onecycle, (n_samples,)).astype(numpy.int16)
    return x


start_freq = 440


def note(n):
    factor = 2 ** (n / 19)
    return sine_wave(440 * factor, 4096)



# for i in range(0, 19):
#     play(note, 1000)



def chord(*args):
    ret = sum((note(arg) for arg in args))
    return ret

play(chord(0, 3, 6), 1000)
time.sleep(0.3)
play(chord(0, 3, 7), 1000)
time.sleep(0.3)
play(chord(0, 4, 11), 1000)
time.sleep(0.3)
play(chord(0, 5, 11), 1000)
time.sleep(0.3)
play(chord(0, 6, 11), 1000)
# time.sleep(0.3)
# play(chord(0, 3, 11), 1000)
# time.sleep(0.3)
# play(chord(0, 4, 10), 1000)

exit(0)

from collections import Counter, defaultdict

niceness = defaultdict(list)

for i in range(19):
    print(f"Playing 0, {i}")
    play(chord(0, 11, i), 1000)
    time.sleep(0.3)
    # evaluation = input('Ha?')
    # c = Counter(evaluation)
    # niceness[c['+']].append(i)

for x, y in niceness.items():
    print(f'{x}, {y}')


















# dude
