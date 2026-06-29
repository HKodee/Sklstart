from sklearn.preprocessing import Binarizer
import numpy as np

binary = Binarizer(threshold=5)

a = np.array([[13,10,21],
              [21,2,1],
              [3,5,5]])

binary1 = binary.transform(a)
binary1