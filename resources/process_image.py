import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image1 = np.load('image1.npy')
image2 = np.load('image2.npy')

fig,(ax1,ax2) = plt.subplots(nrows=1, ncols=2)
ax1.imshow(image1)
ax1.set_title('input image')
ax2.imshow(image2)
ax2.set_title('label')
fig.savefig('images.png')
