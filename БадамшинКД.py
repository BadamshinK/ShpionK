import math

def Kiber18 (bait, pages, lines, symbols ):
    allSymbols = int (pages) * ( int (lines) * int (symbols))
    bit = int(bait) * 8
    oneSymbolsBit = int(bit) /int(allSymbols)
    N = 2 ** oneSymbolsBit
    print ("{} символов в алфавите".format(int(N)))

def Kiber19(firstAlphavit, secondAlphavit):
    N_first = math.log2(firstAlphavit)
    N_second = math.log2(secondAlphavit)
    times = N_second / N_first 
    print ("{}, Именно во столько раз отличаеться".format(times))

def Kiber20 (alphavit, bit):
    oneSymbolBit = math.log2(alphavit)
    symbols = bit / oneSymbolBit
    print ("{} символов в сообщении".format(int(symbols)))

def Entropy19(bit):
    floors = 2 ** bit
    print ("{} этажей всего".format(int(floors)))

def Entropy20(bit):
    builds = 2 ** bit
    print ("{} подьездов".format(int(builds)))
if __name__ =="__main__":
    #Чтобы коментировать блоки кода, нужно использовать ''' с двух стророн
    # Ссылка на репозитория GitHub: https://github.com/BadamshinK/ShpionK

    Kiber18_1 = input("Количество байт: ")
    Kiber18_2 = input("Количество страниц: ")
    Kiber18_3 = input("Количество строк: ")
    Kiber18_4 = input("Количество символов: ")
    Kiber18(Kiber18_1, Kiber18_2, Kiber18_3, Kiber18_4)
    
    Kiber19_1 = input("Мощность первого алфавита: ")
    Kiber19_2 = input("Мощность втрого алфавита: ")
    Kiber19(int(Kiber19_1), int(Kiber19_2))
    
    Kiber20_1 = input("Мощность алфавита: ")
    Kiber20_2 = input("Количество бит в сообщении: ")
    Kiber20(int(Kiber20_1), int(Kiber20_2))
    
    Entropy19_1 = input("Кол-во битов информации о этаже: ")
    Entropy19(int(Entropy19_1))
    
    Entropy20_1 = input("Кол-во битов информации о подьезде: ")
    Entropy20(int(Entropy20_1))