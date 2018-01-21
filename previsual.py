
import csv


def cleaner(csvfile):
    for x in csvfile:
        x["CarrierName"] = carrnames[x["UniqueCarrier"]]
        x["OriginName"] = airnames[x["Origin"]]
        x["DestName"] = airnames[x["Dest"]]
    return csvfile

carrnames = {}
with open("carriers.csv", "rb") as carrcsv:
    read1 = csv.reader(carrcsv)
    for row1 in read1:
        carrnames[row1[0]] = row1[1]
carrcsv.close()
        
airnames = {}
with open("airports.csv", "rb") as aircsv:
    read2 = csv.reader(aircsv)
    for row2 in read2:
        airnames[row2[0]] = row2[1]
aircsv.close()

c87list = []
with open("1987.csv", "rb") as csv87:
    read87 = csv.DictReader(csv87)
    for row3 in read87:
        c87list.append(row3)
csv87.close()

c97list = []
with open("1997.csv", "rb") as csv97:
    read97 = csv.DictReader(csv97)
    for row4 in read97:
        c97list.append(row4)
csv97.close()

c07list = []
with open("2007.csv", "rb") as csv07:
    read07 = csv.DictReader(csv07)
    for row5 in read07:
        c07list.append(row5)
csv07.close()

tx87 = cleaner(c87list)
tx97 = cleaner(c97list)
tx07 = cleaner(c07list)
        
fieldnames = ["Year", "Month", "DayofMonth", "DayOfWeek", "DepTime", "CRSDepTime",
              "ArrTime", "CRSArrTime", "UniqueCarrier", "CarrierName", "FlightNum", "TailNum",
              "ActualElapsedTime", "CRSElapsedTime", "AirTime", "ArrDelay", "DepDelay",
              "Origin", "OriginName", "Dest", "DestName", "Distance",	"TaxiIn", "TaxiOut", "Cancelled", "CancellationCode",
              "Diverted", "CarrierDelay", "WeatherDelay", "NASDelay", "SecurityDelay", "LateAircraftDelay"]


with open("1987.csv", "wb") as te87csv:
    testwriter1 = csv.DictWriter(te87csv, fieldnames)
    testwriter1.writeheader()
    for y in tx87:
        testwriter1.writerow(y)
te87csv.close()

with open("1997.csv", "wb") as te97csv:
    testwriter2 = csv.DictWriter(te97csv, fieldnames)
    testwriter2.writeheader()
    for j in tx97:
        testwriter2.writerow(j)
te97csv.close()

with open("2007.csv", "wb") as te07csv:
    testwriter3 = csv.DictWriter(te07csv, fieldnames)
    testwriter3.writeheader()
    for l in tx07:
        testwriter3.writerow(l)
te07csv.close()



