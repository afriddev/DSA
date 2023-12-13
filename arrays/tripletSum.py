
def solution(array,key):
    for i in array:
        for j in array:
            for k in array:
                if(i+j+k == key):
                    return [i,j,k]
    return 0
if __name__ == "__main__":
    array = [12, 3, 4, 1, 6, 9]
    key = 24
    result = solution(array,key)
    print(result)
    
