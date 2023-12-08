def solution(array):
    emptyArray = []
    for i in range(0,len(array)):
        if(i in array):
            emptyArray.append(i)
        else:
            emptyArray.append(-1)
    return emptyArray
if __name__ == "__main__":
    array = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    result = solution(array)
    print(result)
