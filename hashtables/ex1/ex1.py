def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    
    dictonary = {}

    for i in range(length):
        weight = weights[i]
        dictonary[weight]= i

    for x in range(length):
        key = limit - weights[x]
        if key in dictonary:
            return(dictonary[key],x)


    # Your code here

    # return None
