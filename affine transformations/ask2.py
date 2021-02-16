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

# Apothikeuw tis grammes kai tis stiles tis arxikis eikonas sta rows, columns antistoixa
rows = starting_image.shape[0]
columns = starting_image.shape[1]

# Ftiaxnw tin eikona apo ton pinaka starting_image
plt.imshow(starting_image, cmap = "gray")

# Dimiourgw tis first_row kai second_row pou anaparistoun tin prwti kai deuteri grammi
# antistoixa tou pinaka metasximatismou
first_row = []
second_row = []

# Sti first_row vazw tis a1, a2, a3
for i in range(3, 6):
    first_row.append(float(sys.argv[i]))


# Sti second_row vazw tis a4, a5, a6
for j in range(6, 9):
    second_row.append(float(sys.argv[j]))


# Estw transformed_image o pinakas tis eikonas pou tha prokypsei apo ton affiniko metasximatismo,
# arxikopoihmenos me midenika
transformed_image = np.zeros([rows, columns])


for r in range(rows):
    for c in range(columns):
        # Estw (x,y) i thesi tou simeiou arxika
        # Ta rows/2 kai columns/2 yparxoun gia na ginei o metasximatismos ws pros to eikonostoixeio
        # pou vrisketai sto meso tis eikonas
        x = r - rows / 2
        y = c - columns / 2

        # Efarmozw metasximatismo kai paremvoli kontinoterou geitona gia to x
        # To rows/2 yparxei gia na ginei o metasximatismos ws pros to eikonostoixeio
        # pou vrisketai sto meso tis eikonas
        transf_x = first_row[0] * x + first_row[1] * y + first_row[2] * 1 + rows / 2
        # interp_x tha einai i syntetagmeni x tou simeiou meta to metasximatismo
        interp_x = round(transf_x)

        # Efarmozw metasximatismo kai paremvoli kontinoterou geitona gia to y
        # To columns/2 yparxei gia na ginei o metasximatismos ws pros to eikonostoixeio
        # pou vrisketai sto meso tis eikonas
        transf_y = second_row[0] * x + second_row[1] * y + second_row[2] * 1 + columns / 2
        # interp_y tha einai i syntetagmeni y tou simeiou meta to metasximatismo
        interp_y = round(transf_y)


        # Pairnw tin timi apo tin thesi tou simeiou kai ti vazw sti thesi [r][c]
        if(interp_x >= 0 and interp_y >= 0 and interp_x < rows and interp_y < columns):
            transformed_image[r][c] = starting_image[interp_x][interp_y]

# Ftiaxnw tin eikona apo ton pinaka transformed_image
plt.imshow(transformed_image, cmap = "gray")
# Emfanizw tin eikona
plt.show()
# Apothikeuw tin eikona
save_image = Image.fromarray(transformed_image.astype(np.uint8))
save_image.save(output_file)





