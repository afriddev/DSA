def removeRepeating(array):
    emptyArray = []
    for i in array:
        if i not in emptyArray:
            if(len(emptyArray) >= 1):
                emptyArray.append(i)
                for j in range(0,len(emptyArray)-1):
                    o = j
                    for k in range(j+1,len(emptyArray)-1):
                        if emptyArray[k] < emptyArray[o]:
                            o = k
                    emptyArray[j],emptyArray[o] = emptyArray[o],emptyArray[j]
            else:
                emptyArray.append(i)
    return emptyArray
if __name__ == "__main__":
    array = [2,3,4,2,7,3,5,8,4,7,4,7]
    result = removeRepeating(array)
    print(result)
