def solution(array):
    for i in range(1,len(array)-1):
        left = 0
        right = 0
        for j in range(0,i):
            left =array[j]+left
        for k in range(i+1,len(array)):
            right= right + array[k]
        if(left == right):
           return i
    return 0
if __name__ == "__main__":
    array = [-7, 1, 5, 2, -4, 3, 0]
    result= solution(array)
    print(result)
