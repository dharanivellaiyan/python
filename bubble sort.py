# bubble sort assending and desending order

def bubble(a):
    n=len(a)
    for i in range(n-1):
        for j in range (n-1):
        #    if a[j+1]>a[j]:
        #         a[j+1],a[j]=a[j],a[j+1]
            if a[j+1]<a[j]:
                a[j],a[j+1]=a[j+1],a[j]

                
    print("sorted list:",a)

a=[6,5,8,7,9,4,3]
bubble(a)
