from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

x,y= make_classification(n_features=5,n_classes=4,n_informative=3,n_samples=50000)
plt.scatter(x[:,0],x[:,1],c=y)