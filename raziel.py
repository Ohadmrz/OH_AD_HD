def functorial(n):
    if n == 1:
        return 1
    return functorial(n-1)*n

print(functorial(600))
tit= 'gog'
print(tit.title())