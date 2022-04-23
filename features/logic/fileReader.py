
from re import S


with open('features\logic\scenarios.bdd') as f:

    fileWriter = open("features/tests.feature","w")
    content = f.readlines()

    inAWhichMeans = False

    featureString = "Feature: Test\n"


    for i in range(0,len(content)):
        line = content[i]
        if("which means" in line):
            pass
        elif(line.startswith('Scenario:')):
            scenario = line.replace('"',"").replace("Scenario: ","")
            s = "Feature: " + scenario
            fileWriter.write(s)
        elif(line.startswith('Given')):
            line = '\tScenario: '+line
            fileWriter.write(line)
        elif(line.startswith('When')):
            s = '\tScenario: '+ line             
            fileWriter.write(s)
        elif(line.startswith('Then')):
            s = '\tScenario: '+ line 
            fileWriter.write(s)
        elif(line.startswith('//')):
            pass
        elif(line.startswith('entity')):
            pass
        elif(line.startswith('model')):
            pass
        elif('actions' in line):
            pass
        elif('states' in line):
            pass
        elif('properties' in line):
            pass
        elif('}' in line):
            pass
        elif('/*' in line):
            pass
        elif('*/' in line):
            pass
        else:
            fileWriter.write(line)
    fileWriter.close()

            
            
            
        
                
#if ((line.startswith("Given") | line.startswith("When") | line.startswith("Then") | line.startswith("And")) & inAWhichMeans):
#print(line)