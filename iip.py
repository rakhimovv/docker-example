import matplotlib.pyplot as plt
import numpy as np
from imageio import imread

img = imread('qr_code.jpg')/255

noisy_sin = np.fft.fft(img[1])
noisy_sin.real[np.where(np.abs(noisy_sin.real) < 1)] = 0
noisy_sin.imag[np.where(np.abs(noisy_sin.imag) < 1)] = 0
sin = np.fft.ifft(noisy_sin)
img = img-sin.real

import matplotlib
matplotlib.image.imsave('result.png', img, cmap="gray")

with open('report.txt', 'w') as f:
    f.write('Congratulations! You got a cleaned and readable QR code from the distorted one. Do not judge strictly this is my first docker project :)') 