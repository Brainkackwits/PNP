import glob

full = "C:\\Users\\tobias\\Desktop\\PNP\\DandD\\Geschichten\\Die Dragons slayers\\charaktere\\NPC\\"
for file in glob.glob("*.csv"):
    filename = full+file
    print(file)
    import csv
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        list = {}
        z=0
        for row in reader:

            for raw in row:

                list[z] = row

            z=z+1
        for a in list:
            global name
            new = list[a]
            name = new[1]+" "+new[0]

        #    print(name)
        #    print(new)
            print(f"{a+1}.", str(name))
