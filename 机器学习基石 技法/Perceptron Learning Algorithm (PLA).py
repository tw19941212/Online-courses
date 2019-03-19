import numpy as np


def pla(X, y, iteration=50):
    '''
    Perceptrons Learning Alogrithm for binary classification

    :X: one data per line and one feature per column
    :y: {+1,-1} the true label of data
    '''
    y = np.ravel(y)
    X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)
    w = np.zeros((X.shape[1], 1))
    for i in range(iteration):
        err = 0
        for idx in range(len(y)):
            y_hat = 1 if np.dot(X[idx], w) > 0 else -1
            if y_hat != y[idx]:
                err += 1
                w += (y[idx]*X[idx]).reshape((w.shape))
        if err == 0:
            break
    return w


# 当数据线性不可分时,Pocket Algorithm迭代有限次数,随机地寻找分错的数据

def evaluate_err(w, X, y):
    y_pred = np.dot(X, w)
    y_pred[y_pred > 0] = 1
    y_pred[y_pred != 1] = -1
    err_num = sum(y_pred.ravel() != y.ravel())
    return err_num/len(y)


def pocket_pla(X, y, num_updates=50):
    '''
    Pocket perceptrons Learning Alogrithm for binary classification

    :X: one data per line and one feature per column
    :y: {+1,-1} the true label of data
    :num_updates: total number of updates
    '''
    y = np.ravel(y)
    X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)
    w = np.zeros((X.shape[1], 1))
    err_min = evaluate_err(w, X, y)
    w_min = w.copy()
    
    update = 0
    while update < num_updates:
        idx = np.random.randint(0, len(y))
        y_hat = 1 if np.dot(X[idx], w) > 0 else -1
        if y_hat != y[idx]:
            w = w + (y[idx]*X[idx]).reshape((w.shape))

            error = evaluate_err(w, X, y)
            update += 1

            if error < err_min:
                err_min = error
                w_min = w
    return w_min
