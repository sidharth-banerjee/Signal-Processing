'''
Name: Sidharth Banerjee
ID  : 1001622703
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import feature

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def findImage(mainImage, template):
    main = rgb2gray(mpimg.imread(mainImage))
    template = rgb2gray(mpimg.imread(template))
    plt.figure('Main Image')
    plt.imshow(main)
    plt.figure('Template Image')
    plt.imshow(template)
    plt.show()

    array = feature.match_template(main, template)
    r = np.argmax(np.max(array, axis=1))
    c = np.argmax(np.max(array, axis=0))
    l, w = np.shape(template)

    for i in range (r, r+l, 1):
        for j in range (c, c+w, 1):
            main[i][j] = 0

    plt.figure('Template Match')
    plt.imshow(main)
    plt.show()
    return r, c

if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"
    r, c = findImage(mainImage, template)

    print("coordinates of match = (%d, %d)" % (r, c))
