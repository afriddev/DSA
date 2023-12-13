def solution(array,key):
    for i in array:
        for j in array:
            if(i+j== key):
                return [i,j]
    return 0
if __name__ == "__main__":
    array = [2, 3, 5, 8, 9, 10, 11]
    key = 18
    result = solution(array,key)
    print(result)
    
