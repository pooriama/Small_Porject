


def search_first_of_k(A,k):

    l,u=0,len(A)-1

    while l<=u:
        mid=l+(u-l)//2
        if A[mid]==k:
            result=mid
            u=mid-1
        elif A[mid]<k:
            l=mid+1
        else:
            u=mid-1

    return result

A=[1,2,3,3,4,4,5,6,7,8,11,14]
print(search_first_of_k(A,4))
