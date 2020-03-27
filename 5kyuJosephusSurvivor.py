def josephus_survivor(n,k):
    #your code here
    if n == 1:
        return 1
    else:
        nbs = [i for i in range(n + 1)]
        nbs.pop(0)
        print(len(nbs), "hello")
        print(nbs[0], "hello")
        
        while len(nbs) > 1 and k < len(nbs):
            print(nbs[k - 1])
            nbs = nbs[0:k] + nbs[k+1:]
        while len(nbs) > 1 and k >= len(nbs):
            print(len(nbs), "hi", nbs[k % len(nbs)])
            nbs = nbs[0:(k % len(nbs))] + nbs[(k % len(nbs)) + 1:]
            
        return nbs
        

print(josephus_survivor(521,4328)) #16

