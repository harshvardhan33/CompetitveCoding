def Merge(arr,left,mid,right):
    i = left
    j = mid+1
    k = left 
    while(i<=mid and j<=right):        
        if arr[i]<arr[j]:
            temp[k]=arr[i]            
            i+=1
            k+=1
        else:
            temp[k]=arr[j]
            j+=1
            k+=1        
    while(i<=mid):
        temp[k]=arr[i]
        i+=1
        k+=1
    while(j<=right):
        temp[k]=arr[j]
        j+=1
        k+=1   
    for i in range(left,right+1):
        arr[i]=temp[i]    

def MergeSort(arr,left,right):
    if right>left:
        mid = (left+right)//2
        MergeSort(arr,left,mid)
        MergeSort(arr,mid+1,right)
        Merge(arr,left,mid,right)    
    
arr =  [40,25,19,12,9,6,2]
temp = [0]*len(arr)
n = len(arr)
MergeSort(arr,0,n-1)   