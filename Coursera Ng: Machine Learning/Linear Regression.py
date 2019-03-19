import numpy as np


def featureNormalize(X):
    '''
    归一滑特征值
    
    :X: 每行一个样本,每列一个特征(不需归一化偏差项系数,此时X无偏差项系数)
    '''
    X_mean = np.mean(X, axis=0)
    X_std = np.std(X, axis=0)
    X_norm = (X - X_mean) / X_std

    return X_norm, X_mean, X_std


def computeCost(X, y, theta):
    '''
    计算线性回归的损失
    
    :X: 每行一个样本,每列一个特征(第一列为全1为偏差项系数)
    :y: 样本真实连续值
    :theta: 回归系数,shape (X.shape[-1],1)
    '''
    m = len(y)
    pred = np.dot(X, theta)
    J = 1/(2*m) * np.sum(np.square(pred-y))
    return J


def gradientDescent(X, y, theta, alpha, iterations):
    '''
    梯度下降实现
    
    :X: 每行一个样本,每列一个特征(第一列为全1为偏差项系数)
    :y: 样本真实连续值
    :theta: 回归系数,shape (X.shape[-1],1)
    :alpha: 学习率
    :iterations: 迭代次数(梯度下降更新次数)
    '''
    m = len(y)
    J_history = np.zeros((iterations, 1))

    for i in range(iterations):
        pred = np.dot(X, theta)
        errors = pred - y
        delta = 1 / m * np.dot(np.transpose(X), errors)

        theta = theta - alpha * delta
        J_history[i] = computeCost(X, y, theta)

    return theta, J_history