import csv

INPUT_FILE = "clockmodule.csv"
OUTPUT_FILE = "partslist.md"
countedItems = {}


def read():
    with open(INPUT_FILE, 'r') as data:
        for line in csv.DictReader(data):

            # save the fields we need to our own list 

            addToList(str({"value" : line["Value"], "footprint" :  line["Footprint"], "libpart" : line["LibPart"]}))



def addToList(element):
    # check if the element is already in the list
    try:
        countedItems[element]
        pass

    except Exception as err: # if not throw exception        
        countedItems[element] = 0
    
    # when we want to add another instance increment the value with one
    newAmount = int(countedItems[element]) + 1
    countedItems[element] = newAmount


def getItems():
    output = ""
    for item in countedItems:

        amount = str(countedItems[item])

        splitItems = item.split("'")

        # for i in range(0, len(splitItems)):
            # print(str(i) + splitItems[i])


        index_value = 3
        index_footprint = 7
        index_libpart = 11

        libpart = splitItems[index_libpart].split(":")[1]

        line = "- " + amount  + "x " + splitItems[index_value] + ", " + libpart
        # print(line)
        output += line + "\n"
    
    return output



def writeFile():
    with open(OUTPUT_FILE, "w") as output:
        output.writelines(getItems())




if __name__ == "__main__":
    read()
    writeFile()
    # print(getItems())
