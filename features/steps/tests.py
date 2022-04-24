from mimetypes import init
from turtle import pos
from behave import when, given, then
from numpy import result_type, sign
import rtde_receive
import rtde_control
import json
from robot import Robot
import time
import rtde_io


f = open("features\Environment.json")
data = json.load(f)





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

# Get input port based on configured name
def getDigitalOutput(name):
    inputs = data["Robot"]["Digital outputs"]
    for index in range(len(inputs)):
        for key in inputs[index]:
            if (name == inputs[index][key]):
                return index

# Get coordinate-location based on configured name
def getLocation(name):
    locations = data["Locations"]
    coordinate = locations[name]

    return coordinate


@given('the position of the robot "{identifier}" is "{location}"')
def step_given(context, identifier : str, location):

    coordinates = getLocation(location)
    if(context.receiver.getActualQ() != coordinates):
        context.controller.moveJ(coordinates, getspeed(), getacceleration())


@given('the signal of the sensor "{identifier}" is "{state}"')
def step_given(context, identifier : str, state : str):
    pass

    '''
    t_end = time.time() + 10
    while time.time() < t_end:
        #TODO: how is it implemented?
        #robot.get_receiver.getActualDigitalInputBits()
    '''
    
@given('the robot "{identifier}" is connected')
def step_given(context, identifier : str):
    controller  = context.controller
    if(controller.isConnected()):
        return True
    else: 
        return False

@given('the output "{identifier}" is {state}')
def step_then(context, identifier : str, state):
    
    signal = (state=="ON")
    output = getDigitalOutput(identifier)
    rtde_io.setStandardDigitalOut(output, signal)
    


@given('the gripper "{identifier}" is {state}')
def step_then(context, identifier : str, state):
    time.sleep(3)
    pass
    

@when('the output "{identifier}" turns {state}')
def step_when(context, identifier : str, state):
    time.sleep(3)
    pass
    '''
    index = getDigitalInput(identifier)
    if(index != -1):
        robot.get_io.setStandardDigital(7, False)
        robot.get_io().setToolDigitalOut(0, False)
        time.sleep(0.01)
        
        
        print("Turned off")
    else:
        print(identifier +" is not connected")
        assert False
    '''

@when('the robot "{identifier}" moves to position "{location}"')
def step_when(context, identifier : str, location):

    coordinates = getLocation(location)
    controller = context.controller
    
    
    time.sleep(2)
    
    controller.moveJ(coordinates, getspeed(), getacceleration())


@when('the robot "{identifier}" linearly moves to position "{location}"')
def step_when(context, identifier : str, location):

    coordinates = getLocation(location)
    controller = context.controller
    
    time.sleep(2)
    
    controller.moveL_FK(coordinates, getspeed(), getacceleration())

@when('the robot "{identifier}" moves to position "{location}" with "{speed}" speed')
def step_when(context, identifier : str, location, speed : str):

    coordinates = getLocation(location)
    controller = context.controller
    
    time.sleep(2)
    
    controller.moveJ(coordinates, getspeed(speed), getacceleration(speed))

@when('the robot "{identifier}" linearly moves to position "{location}" with "{speed}" speed')
def step_when(context, identifier : str, location, speed : str):

    coordinates = getLocation(location)
    controller = context.controller

    time.sleep(2)
    
    controller.moveL_FK(coordinates, getspeed(speed), getacceleration(speed))

@when('the gripper "{identifier}" {action}')
def step_then(context, identifier : str, action):
    time.sleep(3)
    pass

@then('the position of the robot "{identifier}" is "{location}"')
def step_then(context, identifier : str, location):
    time.sleep(1)
    pass

@then('the robot "{identifier}" is moved')
def step_then(context, identifier : str):
    time.sleep(3)
    pass

@then('the signal of the sensor "{identifier}" is "{state}"')
def step_then(context, identifier : str, state):
    time.sleep(3)
    pass

    '''
    t_end = time.time() + 10
    while time.time() < t_end:
        #TODO: how is it implemented?
        #robot.get_receiver.getActualDigitalInputBits()
    '''


@then('the output "{identifier}" is {state}')
def step_then(context, identifier : str, state):
    signal = (state=="ON")
    output = getDigitalOutput(identifier)
    rtde_io.setStandardDigitalOut(output, signal)


@then('the gripper "{identifier}" is {state}')
def step_then(context, identifier : str, state):
    time.sleep(3)
    pass