import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here

    # pad tehm to get seuqences of equal lkenght 

    if not max_len:
        max_len = max(len(seq) for seq in seqs)

    res = []
    for s in seqs:
        # if longer than sequneces
        if len(s) >= max_len:
            res.append(list(s[:max_len])) # only up top max len
        else:
            # need ot convert seqnece to anotehr array? 
            res.append(list(s) + [pad_value] * (max_len - len(s))) 
    return np.array(res, dtype=float)
