def solution(array,n,m):
    smallest = 0
    for i in range(0,m):
        if i not in array:
            smallest = i
            break
    print(smallest)
if __name__ == "__main__":
    array = [0,1,2,6,9]
    n= 5
    m = 10
    solution(array,n,m)
