
with open('features\logic\scenarios.txt') as f:
    content = f.readlines()

    inAWhichMeans = False

    for i in range(len(content)):
        line = content[i]
        if (line.startswith("Scenario:")):
            print(line)

        if (line.startswith("which means")):
            for x in range(len(content)-(i+1)):
                line = x
                

        #if ((line.startswith("Given") | line.startswith("When") | line.startswith("Then") | line.startswith("And")) & inAWhichMeans):
            #print(line)