def leftRotation(array,fromPosition):
    k = array.index(fromPosition)
    emptyList = []
    emptyList = array[k+1:] + array[0:k+1]
    return emptyList
if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8]
    fromPosition = 3
    result = leftRotation(array,fromPosition)
    print(result)
