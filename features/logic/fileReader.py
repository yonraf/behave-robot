
with open('features\logic\scenarios.bdd') as f:

    fileWriter = open("features\logic\scenarios.feature","w")
    content = f.readlines()

    inAWhichMeans = False

    featureString = "Feature: Test\n"

    fileWriter.write(featureString)

    for i in range(0,len(content)):
        line = content[i]
        if("which means" in line):
            print()
        elif(line.startswith('Scenario:')):
            line = "    "+line
            fileWriter.write(line)
            print(line)
        elif(line.startswith('Given')):
            # insert pass
            print()
        elif(line.startswith('When')):
            # insert pass
            print()
        elif(line.startswith('Then')):
            # insert pass

            print()
        elif(line.startswith('//')):
            print()
            # insert pass
        else:
            fileWriter.write(line)
            print(line)
    fileWriter.close()

            
            
            
        
                
#if ((line.startswith("Given") | line.startswith("When") | line.startswith("Then") | line.startswith("And")) & inAWhichMeans):
#print(line)