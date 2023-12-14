def solution(array):
    emptyArray = []
    for i in array:
        if(i ==" "):
            emptyArray.append("%20")
        else:
            emptyArray.append(i)
    print(''.join(emptyArray))
if __name__ == "__main__":
    array = "Mr John Smith"
    solution(array)
