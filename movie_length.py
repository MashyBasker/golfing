k, a = input().split(" ")
print(f"{int(k)//60} hour{'' if int(k)//60==1 else 's'} {int(k)%60} minute{'' if int(k)%60==1 else 's'}")
