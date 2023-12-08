def subArrayWithSum(array,sumToFind):
    for i in range(len(array)):
        sumGot = array[i]
        fromIndex = i
        toIndex = i
        for j in range(i+1,len(array)):
            if((sumGot+array[j]) == sumToFind):
                toIndex = j
                return [fromIndex,toIndex]
            else:
                sumGot = sumGot + array[j]
                toIndex = j
    return [None,None]
if __name__ == "__main__":
    array = [1, 4, 0, 0, 4, 10, 5]
    sumToFind = 7
    result = subArrayWithSum(array,sumToFind)
    for i in result:
        print(i,end = " ")
