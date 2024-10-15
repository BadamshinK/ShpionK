def test(result):
    result = result * 1000
    result = int(result)
    print(result)

if __name__ ==("__main__"): 
    inp1 = input("частота: ")
    test(float(inp1))