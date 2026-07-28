import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler

data = np.array([10,11,12,13,14,15,100]).reshape(-1,1)

rob_scaled= RobustScaler().fit_transform(data)

