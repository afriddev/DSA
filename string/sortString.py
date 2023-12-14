def solution(string):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    emptyArray = []
    for i in string:
        count = 0
        for j in alph:
            if(i == j or i == j.upper()):
                emptyArray.append([i,count])
                count+=1
            else:
                count+=1
    for i in range(0,len(emptyArray)):
        small = emptyArray[i]
        o = i
        for j in range(i+1,len(emptyArray)):
            if(small[1] > emptyArray[j][1]):
                small = emptyArray[j]
                o = j
        emptyArray[i],emptyArray[o] = small,emptyArray[i]
        
    for i in emptyArray:
        print(i[0],end=" ")
if __name__ == "__main__":
    string = 'afrid'
    solution(string)
