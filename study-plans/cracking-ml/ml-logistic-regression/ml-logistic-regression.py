import numpy as np

def logistic_regression(X, y, lr=0.01, n_iters=1000):
    """
    Returns:
        tuple: (weights, bias) where weights is a list and bias is a float
    """

    b = 0.0 
    X = np.array(X)
    y = np.array(y)
    n, d = X.shape
    w = np.zeros(d)
        
    z = X @ w + b 

    for _ in range(n_iters):
        
        z = X @ w + b 
        y_hat = 1.0 / (1.0 + np.exp(-z))
        
        dw = (1.0 /n) * np.transpose(X) @ (y_hat - y)
        db = (1.0 /n) * np.sum(y_hat - y)

        w -= lr * dw 
        b -= lr * db 

    
    return (w.tolist(), float(b))
    pass
