import math

def cyclic_encoding(values: list, period: float) -> list:
    """
    Returns the sine and cosine encoding of every cyclic value.
    """
    res = [] 
    for value in values: 
        angle = 2 * math.pi * value / period 
        res.append([math.sin(angle), math.cos(angle)])
    return res 

    
    # Write code here
    pass