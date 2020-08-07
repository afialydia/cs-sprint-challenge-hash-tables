#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []
    cache={}

    for indi_tick in tickets: # <- for each instance of the Ticket class in the tickets array I'm going to do the following
        cache[indi_tick.source] = indi_tick.destination # <- mapping their source and destination as the key and value pairs in the dictionary/hash table

    route.append(cache['NONE']) # <- finding departure point and adding it to the beginning of list.. so the key is none here but the value will be appended to my route array?
    key = cache['NONE'] # <-- I now set the position of none as my new key.. NONE is not the key here but the value of the position of NONE is, the function will use the destination/value that is attached to the 'none' as the new key?

    while key != 'NONE': # <- so while the key is not the actual string 'NONE', do this loop.. this is kind of like a base case right, because in this problem we will eventually get to the key being the string NONE again when we reach the final destination.
        route.append(cache[key]) # yeah so we're just going to append the hashed value to the route and then in the next line make it our new key. this loop will continue until the base base is fufilled
        key = cache[key] 

    return route # <- returning the array with proper loop
