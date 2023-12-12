def solution(result,key):
    o = 0
    for i in array:
        if(i == key):
            return o
        else:
            o+=1
    return -1

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8]
    key = 6
    result = solution(array,key)
    if(result == -1):
        print("Not Found")
    else:
        print("Found at :- ",result)
