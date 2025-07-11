from PIL import Image
import numpy as np
import math

na = np.array(Image.open('result.png'))
nar = np.array(Image.open('result_line.png'))

    

def line_filter_sobel(img,img_result):

    i=1
    j=1

    print("negative")
    print(int(img[i-1][j-1][0]) * -0.25 + int(img[i-1][j][0]) * -0.5 + int(img[i-1][j+1][0]) * -0.25)

    print("positive")
    print(int(img[i+1][j-1][0]) * 0.25 + int(img[i+1][j][0]) * 0.5 + int(img[i+1][j+1][0]) * 0.25)

    offset = 1
    for i in range(offset, len(img)-1):
        for j in range(offset, len(img[i])-1):
            result_pixel = int(img[i-1][j-1][0]) * -0.25 + int(img[i-1][j][0]) * -0.5 + int(img[i-1][j+1][0]) * -0.25  
            result_pixel += int(img[i+1][j-1][0]) * 0.25 + int(img[i+1][j][0]) * 0.5 + int(img[i+1][j+1][0]) * 0.25
            result_pixel = math.floor(abs(result_pixel)/6) * 7
            # if result_pixel > threshhold:
            #     result_pixel = 255
            # else:
            #     result_pixel = 0
            

            img_result[i][j][0] = result_pixel
            img_result[i][j][1] = result_pixel
            img_result[i][j][2] = result_pixel

    
    

def main():
    line_filter_sobel(na,nar)
    
    result = Image.fromarray(nar)
    result.save('result_line.png')
    Image.open('result_line.png').convert('RGB')

main()