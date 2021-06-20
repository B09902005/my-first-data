def distance(n,i0,j0):
    a=[[99999]*n for i in range (n)]
    a[i0][j0]=0
    count=123
    dis=0
    while (count!=0):
        count=0
        for i in range (n):
            for j in range (n):
                if (a[i][j]==dis):
                    if (0<=i-1<n)&(0<=j-2<n):
                        if (a[i-1][j-2]>dis+1):
                            a[i-1][j-2]=dis+1
                            count+=1
                    if (0<=i+1<n)&(0<=j-2<n):
                        if (a[i+1][j-2]>dis+1):
                            a[i+1][j-2]=dis+1
                            count+=1
                    if (0<=i-1<n)&(0<=j+2<n):
                        if (a[i-1][j+2]>dis+1):
                            a[i-1][j+2]=dis+1
                            count+=1
                    if (0<=i+1<n)&(0<=j+2<n):
                        if (a[i+1][j+2]>dis+1):
                            a[i+1][j+2]=dis+1
                            count+=1
                    if (0<=i-2<n)&(0<=j-1<n):
                        if (a[i-2][j-1]>dis+1):
                            a[i-2][j-1]=dis+1
                            count+=1
                    if (0<=i+2<n)&(0<=j-1<n):
                        if (a[i+2][j-1]>dis+1):
                            a[i+2][j-1]=dis+1
                            count+=1
                    if (0<=i-2<n)&(0<=j+1<n):
                        if (a[i-2][j+1]>dis+1):
                            a[i-2][j+1]=dis+1
                            count+=1
                    if (0<=i+2<n)&(0<=j+1<n):
                        if (a[i+2][j+1]>dis+1):
                            a[i+2][j+1]=dis+1
                            count+=1
        dis+=1
    return a

def short(n,i0,j0,i1,j1):
    x=distance(n,i0,j0)
    if (x[i1][j1]!=99999):
        return x[i1][j1]
    else:
        return -1

def long(n,i0,j0,i1,j1):
    if (short(n,i0,j0,i1,j1)==-1):
        return -1
    else:
        return n*n-i0

def x(n):
    print ('wuwuboss is so stupid')
    
def y(n):
    print ('I am a loser!!!!!')

def i(n):
    print ('i')
