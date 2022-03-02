print("input a num ")
n = input()

match int(n): 
    case 1:
        print("first call")
    case 2:
        print("second call")
    case _: 
        print("nop")