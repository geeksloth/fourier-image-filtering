import numpy as np
import matplotlib.pyplot as plt
import PIL
import cmath


def DFT_2d(image):
	#data = np.asarray(image)
	data = image
	M, N = image.shape # (img x, img y)
	dft2d = np.zeros((M,N),dtype=complex)
	for k in range(M):
		for l in range(N):
			sum_matrix = 0.0
			for m in range(M):
				for n in range(N):
					e = cmath.exp(- 2j * np.pi * ((k * m) / M + (l * n) / N))
					sum_matrix +=  data[m,n] * e
			dft2d[k,l] = sum_matrix
	return dft2d

def iDFT_2d(image):
	#data = np.asarray(image)
	data = image
	#M, N = image.size # (img x, img y)
	M, N = image.shape
	dft2d = np.zeros((M,N),dtype=complex)
	for k in range(M):
		for l in range(N):
			sum_matrix = 0.0
			for m in range(M):
				for n in range(N):
					e = cmath.exp(2j * np.pi * ((k * m) / M + (l * n) / N))
					sum_matrix +=  data[m,n] * e
			dft2d[k,l] = sum_matrix
	return dft2d

img2 = PIL.Image.open("data/x-27-y32.png").convert('L')
#img2 = img.resize((50,50))
img_np = np.asarray(img2)

#transform to frequency domain
dft = DFT_2d(img_np)
dft_centered = np.fft.fftshift(dft)

#try to cutout some range of frequencies
cut_f_signal = dft_centered.copy()
cut_f_signal[(img_np<85)] = 0
#cut_f_signal[(img_np>300)] = 0

#f = np.fft.ifft2(dft_centered)
img_spatial = iDFT_2d(np.fft.ifftshift(cut_f_signal))

f, axarr = plt.subplots(2,2)
axarr[0,0].imshow(img2, interpolation='none', cmap='gray', vmin=0, vmax=255)
axarr[0,1].imshow(dft_centered.real, interpolation='none', cmap='gray')
axarr[1,0].imshow(cut_f_signal.real, interpolation='none', cmap='gray')
axarr[1,1].imshow(img_spatial.real, interpolation='none', cmap='gray')
plt.show()