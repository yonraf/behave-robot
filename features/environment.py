from behave import fixture
import rtde_receive
import rtde_control
import rtde_io
import json
from steps.robot import Robot

f = open("features\Environment.json")
data = json.load(f)


# Get IP-address of robot based on configured name
def getRobotIP(name):
    robotName = data["Robot"]["name"]
    if (robotName == name):
        ip = data["Robot"]["IP"]
        return ip
        

def before_feature(context, feature): 
    
    ip = getRobotIP("John Doe")
    
    context.controller = rtde_control.RTDEControlInterface(ip)
    context.receiver = rtde_receive.RTDEReceiveInterface(ip)
    context.io = rtde_io.RTDEIOInterface(ip)

def after_feature(context, feature): 
    print("Run After Each Feature")

def before_scenario(context, scenario): 
    print("Run Before Each Scenario")

def after_scenario(context, scenario): 
    print("Run After Each Scenario")