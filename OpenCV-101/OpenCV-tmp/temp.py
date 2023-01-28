
import numpy as np

def rowcol(val):						                                  # va generar los elementos de la matrix axis=1 de 3cols [a+1,a+2,a+3]	  
   return [val+1,val+2,val+3]
  
m = np.array([ rowcol(v)  for v in range(10,100,10) ])      	# creo una matriz de 10..90 9=Rows / 3=Cols
print(m)

print("---------------")
print(m[0:2])
print(m[2:2])
print(m[2:3])


# [[11 12 13]
#  [21 22 23]
#  [31 32 33]
#  [41 42 43]
#  [51 52 53]
#  [61 62 63]
#  [71 72 73]
#  [81 82 83]
#  [91 92 93]]

# matrix 3 D
print("-------------------------")
import pprint

n = 3
matrix3d = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
pprint.pprint(matrix3d)

#-----------------------
print("\n", matrix3d)

# 3D:
# [
#  [[0, 0, 0], [0, 0, 0], [0, 0, 0]],         -------- 0  dentro hay m0, m1, m2
#  [[0, 0, 0], [0, 0, 0], [0, 0, 0]],         -------- 1
#  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]          -------- 2
# ]

# [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

print("------3D----------")
mmm = np.array([  [[1, 2, 3],
                   [4, 5, 6]],

                  [[7, 8, 9],
                   [0, 1, 2]],

                  [[1, 2, 3],
                   [3, 4, 5]],

                  [[6, 7, 8],
                   [9, 0, 1]]
               ])
print(mmm.ndim)                        # 3
print(mmm.shape)                       # (4, 2, 3)
print(mmm[2,1])                        # [3 4 5]

