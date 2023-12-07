
def insertionSort(a):
  for i in range(1,len(a)):
	  key = a[i]
	  j = i-1
	  while j>=0 and key < a[j]:
		  a[j+1] = a[j]
		  j-=1
	  a[j+1] =key
  

if __name__ = "__main__":
  a  = [4,7,3,1,97,67]
  insertionSort(a)
  print(a)
  
