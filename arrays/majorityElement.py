def solution(array):
    elementResult = array[0]
    times = 1
    for i in range(0,len(array)):
        count = 0
        element = array[i]
        for j in array:
            if(element == j):
                count+=1
        if(count > times):
            times = count
            elementResult = array[i]
    print(elementResult)
if __name__ == "__main__":
    array = [1,2,3,4,5,5]
    solution(array)
