birthday = [1975, 1997, 2002, 1995, 1985]
ages = map (lambda x:2018-x ,birthday)
print(list(ages))



taun = [1975, 1997, 2002, 1995, 1985]
ages = []
for x in range(0, len(taun)): 
    ages = 2018 - taun[x]   
    print(ages)