def solution(string,array):
    emptyArray = []
    o = 0
    for i in string:
        for j in array:
            if(o == j):
                emptyArray.append("*")
                array.remove(o)
        emptyArray.append(i)
        o+=1
    print(''.join(emptyArray))
if __name__ == "__main__":
    string ='afrid'
    array = [2,3,4]
    solution(string,array)
