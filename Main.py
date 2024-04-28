from Matrix import Matrix
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
# 1024 x 768
auto = Image.open("Auto.jpg")
print(auto.getpixel((100,100)))

auto_gray = ImageOps.grayscale(auto)

list =[]

for i in range(1024):
    temp = []
    for j in range(768):
        temp.append(auto_gray.getpixel((i,j)))

    list.append(temp)

auto_grey_matrix = Matrix(list)





sobel_filter_x = Matrix([[-1,0, 1],[-2, 0, 2],[-1, 0,1]])
sobel_filter_y = Matrix([[-1,-2,-1],[0,0,0],[1,2,1]])
#print(auto_grey_matrix)
after_operation = auto_grey_matrix.sobel_operation(sobel_filter_x,sobel_filter_y)


plt.figure()
plt.imshow(after_operation)
plt.show()

#