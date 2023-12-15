def solution(a):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    o = 0
    z = -1
    string = list(a)
    while o < 26:
        if(string[z] == alph[25]):
            z-=1
        
        if(string[z] == alph[o]):
            string[z] = alph[o+1]
            break
        o+=1
    print(''.join(string))
if __name__ == "__main__":
    string = "afriz"
    solution(string)
