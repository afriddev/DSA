def rotateNoOfStepsToLeft(array,steps):
    emptyList = []
    emptyList = array[((len(array)-1)-steps+1):(len(array))] + array[0:((len(array)-1)-steps+1)]
    return emptyList
if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8]
    result = rotateNoOfStepsToLeft(array,3)
    print(result)
