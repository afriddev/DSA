def findAppearOnce(array):
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if(array[i] == array[j]):
                count+=1
        if(count == 1):
            return array[i]
    return -1
if __name__ == "__main__":
    array = [2,31,2,2,1,31]
    result = findAppearOnce(array)
    print(result)
    
"""
 ------------ TIME - O(N) ---------
def findAppearOnce(array):
    result = array[0]
    for i in range(1,len(array)):
        result = result ^ array[i]
    return result
if __name__ == "__main__":
    array =  [2,31,2,2,1,31]
    result = findAppearOnce(array)
    print(result)
    """
