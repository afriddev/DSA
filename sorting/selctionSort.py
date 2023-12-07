def selectionSort(a):
  for i in range(len(a)):
    z = i
	  for k in range(i+1,len(a)):
		  if(a[k]<a[z]):
			  z = k
	  a[i],a[z] = a[z],a[i]
if __name__ == "__main__":
  a  = [4,7,3,1,97,67]
  selectionSort(a)
  print(a)
  
