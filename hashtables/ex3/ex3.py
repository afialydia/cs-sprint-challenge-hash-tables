def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []

    allnums = {}

    for array in arrays:
        allnums[array] = array
        for i in array:
            if i in allnums.keys():
                allnums[i] +=1
            else:
                allnums[i]=1
            
            num = allnums[i]

            # if num > 1:
            #     print(num)


    # print(result)
    print(allnums)




    
    #     result = []

    #     if allnums[i] > 1:
    #         result.append(i)    

    # return result

intersection([[1,2],[1,4,3],[1,6,5]])

# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
