
from behave import when, given, then
from numpy import result_type
import rtde_receive
import rtde_control
import rtde_io

import json
from robot import Robot
import time
import os





f = open("features\Environment.json")
data = json.load(f)

robot = Robot()



# Get speed based naming (if not set, returns moderately)
def getspeed(identifier = "moderate"):
    speed = data["Speeds"][identifier]["speed"]
    return speed

# Get acceleration based naming (if not set, returns moderately)
def getacceleration(identifier  = "moderate"):
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
            else:
                return -1
def getDigitalOutput(name):
    inputs = data["Robot"]["Digital outputs"]
    for index in range(len(inputs)):
        for key in inputs[index]:
            if (name == inputs[index][key]):
                return index
            else:
                return -1


# Get coordinate-location based on configured name
def getLocation(name):
    locations = data["Locations"]
    coordinate = locations[name]

    return coordinate

# test test
def before_all(context, identifier="John Doe"):
    ip = getRobotIP(identifier)
    robot.set_controller(rtde_control.RTDEControlInterface(ip))
    robot.set_receiver(rtde_receive.RTDEReceiveInterface(ip))
    robot.set_io(rtde_io.RTDEIOInterface(ip))



@given('the robot "{identifier}" is at position "{location}"')
def step_given(context, identifier : str, location):
    ip = getRobotIP(identifier)
    robot.set_controller(rtde_control.RTDEControlInterface(ip))
    robot.set_receiver(rtde_receive.RTDEReceiveInterface(ip))
    robot.set_io(rtde_io.RTDEIOInterface(ip))
    receiver = robot.get_receiver()
    loc = getLocation(location)
    if(receiver.getActualTCPPose() == loc):
        print("Robot already in position")
    else:
        speed = getspeed()
        acceleration = getacceleration()
        robot.get_controller().moveJ_IK(loc, speed, acceleration)


@given('the position of the robot "{identifier}" is "{location}"')
def step_given(context, identifier : str, location):
    # TODO: Figure out where to place this initialization
    ip = getRobotIP(identifier)
    robot.set_controller(rtde_control.RTDEControlInterface(ip))
    robot.set_receiver(rtde_receive.RTDEReceiveInterface(ip))
    robot.set_io(rtde_io.RTDEReceiveInterface(ip))
    receiver = robot.get_receiver()
    loc = getLocation(location)
    if(receiver.getActualTCPPose() == loc):
        print("Robot already in position")
    else:
        speed = getspeed()
        acceleration = getacceleration()
        robot.get_controller().moveJ_IK(loc, speed, acceleration)


@given('the digital-input "{identifier}" is {state}')
def step_given(context, identifier : str, state : str):
    inputIndex = getDigitalInput(identifier)
    input = (state == "ON") # True if state = ON. else False
    
    robot.get_receiver.getDigitalOutState(inputIndex)

@given('the port of the digitaloutput "{identifier}" is "{value}"')
def step_given(context, identifier: str, value: str):
    val = int(value)
    ip  = getRobotIP("John Doe")
    #robot.set_io(rtde_io.RTDEIOInterface(ip))

    if val == getDigitalOutput(identifier):
        print(identifier +" is connected")
        robot.get_io().setStandardDigitalOut(val, False)
    else:
        robot.get_io().setStandardDigitalOut(val, False)

        print(identifier +" is not connected")

        

@given('the digitaloutput "{identifier}" is connected')
def step_given(context, identifier):
    index = getDigitalOutput(identifier)
    if(index != -1):
        print(identifier +" is connected")
        robot.get_io().setStandardDigital(7, False)
        robot.get_io().setToolDigitalOut(index, False)

    else:
        assert False

@when('the digitaloutput "{identifier}" turns OFF')
def step_when(context, identifier : str):
    index = getDigitalInput(identifier)
    if(index != -1):
        robot.get_io.setStandardDigital(7, False)
        robot.get_io().setToolDigitalOut(0, False)
        time.sleep(0.01)
        
        
        print("Turned off")
    else:
        print(identifier +" is not connected")
        assert False




@when('the digitaloutput "{identifier}" turns ON')
def step_on(context, identifier : str):
    index = getDigitalInput(identifier)
    if(index != -1):
        robot.get_io().setToolDigitalOut(0, False)
        time.sleep(0.01)




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
    pass

@then('the signal of the digitaloutput "{identifier}" is "{value}"')
def step_then(context, identifier: str, value: str):
    pass