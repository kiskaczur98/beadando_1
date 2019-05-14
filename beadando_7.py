import numpy as np

x=np.random.randint(1,2,(3,4))

def bead7(be_matrix):
    matrixok=[]
    matrix=[]
    final_list=[]
    for i in range(0,len(be_matrix)-1):
        for j in range(0,len(be_matrix[0])-1):
            matrix.append(be_matrix[i][j])
            matrix.append(be_matrix[i+1][j])
            matrix.append(be_matrix[i][j+1])
            matrix.append(be_matrix[i+1][j+1])
            matrixok.append(matrix)
            matrix=[]

    for num in matrixok:
        if num not in final_list:
            final_list.append(num)
    return (len(final_list))

print(bead7(x))