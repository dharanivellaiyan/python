#binary search
def binarysearch(list1,key):
    low=0
    high=len(list1)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if key>list1[mid]:
            low=mid+1
        elif key<list1[mid]:
            high=mid-1
        else:
            return mid
    return-1
    
    
list1=[1,3,4,8,5,6,7]
list1.sort()
print(list1)
key=int(input("enter the key:"))
result=binarysearch(list1,key)
if result!=-1:
    print("element is present at index",str(result))
else:
    print("element is not present")




