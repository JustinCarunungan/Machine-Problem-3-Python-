import numpy as np

def coeff(c):
        a = c[0,:]
        b = c[1,:]
        print(a)
        print(b)
        if len(a)>=11:
                l = 10
        else:
                l = len(a)-1
        n = np.zeros((l,1))
        print(n)
        
        for i in range(1,l):
                pf = np.polyfit(a,b,i)
                pv = np.polyval(pf,a)
                n[i-1,0] = np.linalg.norm(b-pv)
                j = n.argmin()
                coeff = np.polyfit(a,b,j+1)
                print('Best Fit Coefficient: ')
                print()
                print(coeff)
                

arr = np.array([(1,2,3,4,5),(6,7,8,9,10)])
coeff(arr)
input()


    
    