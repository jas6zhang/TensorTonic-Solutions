import numpy as np

def linear_regression(X, y, lr, epochs):
    """
    Returns: tuple (weights, bias)
    """

    # t. Initialize weights to zeros and bias to 0, then iteratively update using MSE gradients.

    b = 0.0
    X = np.array(X)
    y = np.array(y) 
    n, d = X.shape 
    w = np.zeros(d)

    
    # get transposte

    for _ in range(epochs): 
        # The gradients of MSE with respect to the parameters are:
        y_hat = X @ w + b
        # *Element-wise multiplicationnp.multiply()
        # @Matrix multiplication (Dot product)np.matmul() or np.dot()
        # Update rules at each iteration:
        dw = (2.0 / n) * np.transpose(X) @ (y_hat - y)
        db =  (2.0 / n) * np.sum(y_hat - y)

        # reduce MSE 
        # lr stands for learning rate.

        # If you increase w, the loss increases.
        # So to reduce the loss, you should decrease w.

# It's a small positive number that controls how large of a step gradient descent takes when updating the model parameters.
        w -= lr * dw 
        b -= lr * db 
        pass

    weights = [round(float(v), 4) for v in w]
    bias = round(float(b), 4)
    return (weights, bias)