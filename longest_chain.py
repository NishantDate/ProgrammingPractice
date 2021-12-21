#takes in 2 array with random values
#[1,2],[2,3][4,5] etc and then returns the longest chain that can be formed.

#the longest chain is defined by (a,b),(c,d) forms a chain if c > b
test = [[10,20],[40,50],[20,30], [170,10], [160,9], [1,200]]
def longestChain(arr):
    arr = sorted(arr, key= lambda x:x[1])   
    initial = [arr.pop(0)]
    len_arr = len(arr)
    i = 0
    for i in range(len(arr)):
        print(f"chain is {initial} and arr is {arr}")
        if arr[i][0] > initial[-1][1]:
            initial.append(arr[i])
        
    print(initial)



longestChain(test)