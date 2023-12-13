def solution(array):
    emptyArray = []
    for i in range(1,len(array)-1):
        if(array[i]>= array[i-1] and array[i]>= array[i+1]):
            emptyArray.append(array[i])
    return emptyArray
if __name__ == "__main__":
    array = [10, 20, 15, 2, 23, 90, 67]
    result = solution(array)
    print(result)
     
