from Matrix import Matrix

sobel_filter_x = Matrix([[-1,-0, 1],[-2, 0, 2],[-1, 0,1]])
sobel_filter_y = Matrix([[-1,-2,-1],[0,0,0],[1,2,1]])

print(sobel_filter_x)
print(sobel_filter_y)