import numpy
import scipy.signal


import pygame, pygame.sndarray

pygame.init()

def play_for(sample_wave, ms):
    """Play the given NumPy array, as a sound, for ms milliseconds."""
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
    x = numpy.resize(onecycle, (n_samples, 2,)).astype(numpy.int16)
    return x

def square_wave(hz, peak, duty_cycle=.5, n_samples=sample_rate):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    t = numpy.linspace(0, 1, 500 * 440/hz, endpoint=False)
    wave = scipy.signal.square(2 * numpy.pi * 5 * t, duty=duty_cycle)
    wave = numpy.resize(wave, (n_samples,))
    return (peak / 2 * wave.astype(numpy.int16))

print('play 1')

# Play A (440Hz) for 1 second as a sine wave:

start_freq = 440

for i in range(0, 19):
    factor = 2 ** (i / 19)
    play_for(sine_wave(440 * factor, 4096), 1000)



def make_chord(*args):
    ret =
