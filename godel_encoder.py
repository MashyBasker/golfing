# a=int(input().split(" "))
pr=lambda n:sum([1 for i in range(2,int(n**.5)+1) if n%i==0])
