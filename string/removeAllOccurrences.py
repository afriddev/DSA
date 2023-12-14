def solution(string):
    emptyArray = list(string)
    a = emptyArray[0]
    c = 0
    for i in string:
        char = i
        count = 0
        for j in string:
            if(char == j):
                count+=1
        if(count > c):
            c = count
            a = i
    for i in range(0,c):
        emptyArray.remove(a)
    print(''.join(emptyArray))
if __name__ == "__main__":
    string = 'afriddev'
    solution(string)
