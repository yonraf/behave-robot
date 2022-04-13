from mimetypes import init
from turtle import pos
from behave import when, given, then
from numpy import result_type
import rtde_receive
import rtde_control
import json
from robot import Robot
import time

f = open("features\Environment.json")
data = json.load(f)

robot = Robot()



# Get speed based naming (if not set, returns moderately)
def getspeed(identifier = "moderately"):
    speed = data["Speeds"][identifier]["speed"]
    return speed

# Get acceleration based naming (if not set, returns moderately)
def getacceleration(identifier  = "moderately"):
    acceleration = data["Speeds"][identifier]["acceleration"]
    return acceleration

# Get IP-address of robot based on configured name
def getRobotIP(name):
    robotName = data["Robot"]["name"]
    if (robotName == name):
        ip = data["Robot"]["IP"]
        return ip

# Get input port based on configured name
def getDigitalInput(name):
    inputs = data["Robot"]["Digital inputs"]
    for index in range(len(inputs)):
        for key in inputs[index]:
            if (name == inputs[index][key]):
                return index

# Get coordinate-location based on configured name
def getLocation(name):
    locations = data["Locations"]
    coordinate = locations[name]

    return coordinate


@given('the robot "{identifier}" is at position "{location}"')
def step_given(context, identifier : str, location):

    # TODO: Figure out where to place this initialization
    ip = getRobotIP(identifier)
    robot.set_controller(rtde_control.RTDEControlInterface(ip))
    robot.set_receiver(rtde_receive.RTDEReceiveInterface(ip))


@given('the digital-input "{identifier}" is {state}')
def step_given(context, identifier : str, state : str):
    inputIndex = getDigitalInput(identifier)
    input = (state == "ON") # True if state = ON. else False
    
    robot.get_receiver.getDigitalOutState(inputIndex)
    

@when('the robot "{identifier}" moves to position "{location}"')
def step_when(context, identifier : str, location):

    coordinates = getLocation(location)
    controller = robot.get_controller()
    
    time.sleep(2)
    
    controller.moveJ_IK(coordinates, getspeed(), getacceleration())


@when('the robot "{identifier}" linearly moves to position "{location}"')
def step_when(context, identifier : str, location):

    coordinates = getLocation(location)
    controller = robot.get_controller()

    time.sleep(2)
    
    controller.moveL(coordinates, getspeed(), getacceleration())

@when('the robot "{identifier}" moves to position "{location}" with "{speed}" speed')
def step_when(context, identifier : str, location, speed : str):

    coordinates = getLocation(location)
    controller = robot.get_controller()
    
    time.sleep(2)
    
    controller.moveJ_IK(coordinates, getspeed(speed), getacceleration(speed))

@when('the robot "{identifier}" linearly moves to position "{location}" with "{speed}" speed')
def step_when(context, identifier : str, location, speed : str):

    coordinates = getLocation(location)
    controller = robot.get_controller()

    time.sleep(2)
    
    controller.moveL(coordinates, getspeed(speed), getacceleration(speed))

@then('the robot "{identifier}" is moved')
def step_then(context, identifier : str):
    return