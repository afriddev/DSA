def solution(string):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    emptyArray = []
    for i in string:
        char = i
        count = 0
        for j in string:
            if(char == j):
                count+=1
        index = 0
        for k in alph:
            
            if(char == k):
                if([char,count,index] not in emptyArray):
                    emptyArray.append([char,count,index])
            else:
                index+=1
    for j in range(0,len(emptyArray)):
        index = j
        for k in range(j+1,len(emptyArray)):
            if(emptyArray[index][2] > emptyArray[k][2]):
                index = k
        emptyArray[j],emptyArray[index] = emptyArray[index],emptyArray[j]
    for i in emptyArray:
        print("{count}{element}".format(count = i[1],element = i[0]),end="")
if __name__ == "__main__":
    string = "afriddev"
    solution(string)
    
