from PIL import Image
import numpy as np

R_COEF = 0.299
B_COEF = 0.114
G_COEF = 0.587

# na =  np.array([[[255,   0,   0],                      # Red
#         [  0, 255,   0],                      # Green
#         [  0,   0, 255]],                     # Blue

#        [[  0,   0,   0],                      # Black
#         [255, 255, 255],                      # White
#         [126, 126, 126]]], dtype=np.uint8)                     # Mid gray
about:blank#blocked
na = np.array(Image.open('pngtree-the-cocky-dog-lay-quietly-on-the-lawn-in-the-background-image_914867.png'))

def convert_to_grayscale(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            r=None
            g=None
            b=None
            for k in range(3):
                if r == None:
                    r=img[i][j][k]
                elif g == None:
                    g=img[i][j][k]
                elif b == None:
                    b=img[i][j][k]
            grayscale = (r*R_COEF)+(g*G_COEF)+(b*B_COEF)
            for k in range(3):
                img[i][j][k] = grayscale



def main():
    convert_to_grayscale(na)
    print(na)
    result = Image.fromarray(na)
    result.save('result.png')
    Image.open('result.png').convert('RGB')

main()