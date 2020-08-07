def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = [] # <- created array for answer
    numbs = {} #<- created a dictionary or hashtable to store my values

    for num in a: 
        if num < 0: #<- if the number is less than zero, so like any of the negative numbers I'm going to do the following
            numbs[-num] = num # <-  recording the keys of negative numbers as opposite when storing in our dictionary/hashtable 
            #this is only adding the neg numbers to the numbs array
    
    print("negg",numbs.keys())
    
    for num in a: #looping through array from the param again
        if num in numbs: #<- basically if when looping I come upon  any of the same numbers as keys I'm appending it to the result array
            print("db",num)
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
