epsilon = 2

#formula for x gradient: 1/(2*epsilon) * ((image[i+1][j+1] - image[i][j+1]) + (image[i+1][j] - image[i][j]))

#formula for y gradient: 1/(2*epsilon) * ((image[i+1][j+1] - image[i+1][j]) + (image[i][j+1] - image[i][j]))