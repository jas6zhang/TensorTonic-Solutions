def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here

    # precision kj 

    # recommende dis ranked
    top_k = recommended[:k] 
    length_relevant = len(relevant)
    relevant = set(relevant)
    # length_relevant = len(relevant)

    # while recall@k measures what fraction of all relevant items were recommended. 
    total = 0 
    for k_item in top_k:
        if k_item in relevant: 
            total += 1
    print(total, k, length_relevant)
    return [total / k, total / length_relevant]
            
            