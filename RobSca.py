import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler

data = np.array([10,11,12,13,14,15,100]).reshape(-1,1)

rob_scaled= RobustScaler().fit_transform(data)

plt.figure(figsize=(12,5))
plt.subplot(1,3,1)
plt.scatter(range(len(data)),data,color="blue")
plt.title("Original Data")
plt.ylabel("Value")


plt.subplot(1,3,2)
plt.scatter(range(len(rob_scaled)),rob_scaled,color="green")
plt.title("After Robust")
plt.show()