def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here

    
    rated_scores = [(score, index) for index, score in enumerate(scores) if index not in rated_indices]

    rated_scores.sort(key=lambda x: x[0], reverse=True)


    return [index for score, index in rated_scores[:k]]
    

    

    