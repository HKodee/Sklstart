from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

x,y=make_regression(n_features=1,noise=5,n_samples=5000,random_state=0)
print(x)
print(y)
plt.scatter(x,y,s=5)
plt.show()