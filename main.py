import time
print("welcom 2 blin maker  anyways lets start making some blins")
minEggs = 1
milkMin = 500
flourMin = 1000
eggamnt = int(input("how many egg?"))
milkamnt = int(input("how much milk?"))
flouramnt = int(input("how much flour?"))

# calculations
if eggamnt < minEggs and milkamnt < milkMin and flouramnt < flourMin:
    print("no blins today comrade wait for babushka :(")


# smallest of 3
if eggamnt <= milkamnt and milkamnt <= flouramnt:
    smallest = eggamnt 
elif milkamnt <= flouramnt and milkamnt <= eggamnt:
    smallest = eggamnt
else:
    smallest = flouramnt

print("wait im calculating")
time.sleep(2)
print(f"i have concluded u can make {smallest*4} blins")
print("blin maker shutting down")            