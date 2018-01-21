import csv

# dest97 = []
# orig97 = []
# with open("1997.csv", "rb") as csv97:
#     read97 = csv.DictReader(csv97)
#     for row3 in read97:
#         dest97.append(row3["Dest"])
#         orig97.append(row3["Origin"])
# csv97.close()

# for i in dest97:
#     if i in orig97:
#         pass
#     else:
#         print i


dest07 = []
orig07 = []
with open("2007.csv", "rb") as csv07:
    read07 = csv.DictReader(csv07)
    for row4 in read07:
        dest07.append(row4["Dest"])
        orig07.append(row4["Origin"])
csv07.close()

for y in dest07:
    if y in orig07:
        pass
    else:
        print y