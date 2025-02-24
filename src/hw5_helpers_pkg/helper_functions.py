import matplotlib.pyplot as plt
import mglearn
import mglearn.datasets
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def plot_linreg(X, y, X_train=None, lr=None):
    xvec = X.T[0, :]
    plt.plot(xvec, y, "o")
    if X_train is not None and lr is not None:
        slope = lr.coef_
        intercept = lr.intercept_
        xline = np.linspace(min(X_train), max(X_train), 100)
        y_fit = intercept + slope * xline
        plt.plot(xline, y_fit, "--")
    plt.show()


def train_linreg(n_samples=60):
    X, y = mglearn.datasets.make_wave(n_samples=n_samples)
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    lr = LinearRegression().fit(X_train, y_train)
    return X, y, X_train, X_test, y_train, y_test, lr
