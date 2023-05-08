def a(x,y):
    return x+y

def b(s1):
    return s1**2

def c(x,y):
    result = a(x,y)
    # ניתן להוסיף עוד כברים כמובן לפני הרתורן
    return b(result)

print(c(1,2))



########################################################################################################################
############  nikita example: ##########################################################################################
#
# def main():
#     numbers = (2, 4, 6)
#     result = getMultiplyOfNumbersSequence(numbers)
#     print(result)
#     return 1
# def getMultiplyOfNumbersSequence(numbers: tuple) -> float:
#     if not numbers:  # empty tuple
#         return 0.0
#     result = 1.0
#     for i in numbers:
#         result *= i
#     return float(result)
# if __name__ == '__main__':
#   main()