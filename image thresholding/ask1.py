# Spyridonos Vasileios

import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from PIL import Image


try:
    # Pairnw tin arxiki eikona pou einai to prwto orisma kai tin apothikeuw ws pinaka sto starting_image
    starting_image = np.array(Image.open(sys.argv[1]))

# Se periptwsi pou den dothei swsta i entoli
except (FileNotFoundError, ValueError, IndexError):
    print("There was an error! Usage: python3 ask1.py <input filename> <output filename> <threshold k>")
    exit(1)

# Pairnw to onoma tou output file pou einai to deutero orisma
# kai to apothikeuw sto output_file
output_file = sys.argv[2]

# Pairnw to katwfli pou einai to trito orisma kai to apothikeuw sto threshold
threshold = int(sys.argv[3])

# Apothikeuw tis grammes kai tis stiles tis arxikis eikonas sta rows, columns antistoixa
rows = starting_image.shape[0]
columns = starting_image.shape[1]

# Ftiaxnw tin eikona apo ton pinaka starting_image
plt.imshow(starting_image, cmap = "gray")

# Se periptwsi pou exoume egxrwmi eikona, ftiaxnw kainourgio adeio disdiastato pinaka colored_image
colored_image = np.empty([rows, columns])

# Autos tha einai o pinakas tis katwfliwmenis eikonas, arxikopoihmenos me midenika
thresholded_image = np.zeros([rows, columns])


# An i eikona einai egxrwmi
if len(starting_image.shape) == 3:
    starting_image = double(starting_image)
    for r in range(rows):
        for c in range(columns):
            # Athroisma kanaliwn Red, Green, Blue
            RGB = starting_image[r][c][0] + starting_image[r][c][1] + starting_image[r][c][2]
            # Pairnw to meso oro tous
            colored_image[r][c] = RGB / 3

    # Katwfliwsi
    for r in range(rows):
        for c in range(columns):
            if colored_image[r][c] <= threshold:
                # O,ti einai mikrotero apo to threshold to kanw mauro
                thresholded_image[r][c] = 0
            else:
                # O,ti einai megalytero i iso apo to threshold to kanw aspro
                thresholded_image[r][c] = 255


# An i eikona einai grayscale
else:
    # Katwfliwsi
    for r in range(rows):
        for c in range(columns):
            # O,ti einai mikrotero apo to threshold to kanw mauro
            if starting_image[r][c] <= threshold:
                thresholded_image[r][c] = 0
            else:
                # O,ti einai megalytero i iso apo to threshold to kanw aspro
                thresholded_image[r][c] = 255


# Ftiaxnw tin katwfliwmeni eikona apo ton pinaka thresholded_image
plt.imshow(thresholded_image, cmap = "gray")
# Vazw ws titlo to katwfli (threshold) stin katwfliwmeni eikona
plt.title("Threshold = " + str(threshold))
# Emfanizw tin katwfliwmeni eikona
plt.show()
# Apothikeuw tin katwfliwmeni eikona
save_image = Image.fromarray(thresholded_image.astype(np.uint8))
save_image.save(output_file)
