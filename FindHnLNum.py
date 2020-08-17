
storage = list()
GreatesNum = None
SmallestNum = None
while True:
    number = input("Enter the number: ")
    storage.append(number)
    if number == "done":
        break
    try:
        num = int(number)
    except:
        print("Enter the int value")
    if GreatesNum is None:
        GreatesNum = num
    elif num > GreatesNum:
        GreatesNum = num
    if SmallestNum is None:
        SmallestNum = num
    elif num < SmallestNum:
        SmallestNum = num
print("Greates number is :",GreatesNum)
print("Smallest number is :",SmallestNum)
print(storage[:4])


