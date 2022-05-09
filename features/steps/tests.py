from behave import when, given, then
import time
from features import environment as env

@then('the position {prep} the robot "{identifier}" is "{position}"')
@given('the position {prep} the robot "{identifier}" is "{position}"')
def step_given(context, identifier : str, position):

    joint_positions = env.get_position(position)
    if(context.receiver.getActualQ() != joint_positions):
        context.controller.moveJ(joint_positions, env.get_speed(), env.get_acceleration())

@then('the signal {prep} the input "{identifier}" is "{state}"')
@given('the signal {prep} the input "{identifier}" is "{state}"')
def step_given(context, identifier : str, state : str):
    input_state = (state == "ON")
    detected = False

    t_end = time.time() + 10
    while time.time() < t_end:

        input_bits  = context.receiver.getActualDigitalInputBits()
        actual_state = env.get_digital_input_state(env.get_digital_input(identifier), input_bits)

        if actual_state == input_state :
            detected = True
            assert True
            break
    
    #post_input_bits  = context.receiver.getActualDigitalInputBits()
    #post_state = env.get_digital_input_state(env.get_digital_input(identifier), input_bits)

    if not detected:        
        assert False
    
    
@then('the output "{identifier}" is {state}')
@given('the output "{identifier}" is {state}')
def step_then(context, identifier : str, state):
   signal = (state=="ON")  # True if state is ON, else False
   output = env.get_digital_output(identifier)
   context.io.setStandardDigitalOut(output, signal)



@then('the gripper "{identifier}" is {state}')
@given('the gripper "{identifier}" is {state}')
def step_then(context, identifier : str, state):
    desired_state_open = (state=="opened")
    if (desired_state_open):
        context.gripper.open()
    else:
        context.gripper.close()
    
    
@when('the output "{identifier}" {state}')
def step_when(context, identifier : str, state):
    signal = (state=="activates")  # True if state is activates, else False
    output = env.get_digital_output(identifier)
    context.io.setStandardDigitalOut(output, signal)


@when('the robot "{identifier}" moves to position "{position}"')
def step_when(context, identifier : str, position):

    joint_position = env.get_position(position)
    controller = context.controller
    
    controller.moveJ(joint_position, env.get_speed(), env.get_acceleration())


@when('the robot "{identifier}" linearly moves to position "{position}"')
def step_when(context, identifier : str, position):

    joint_positions = env.get_position(position)
    controller = context.controller
    
    controller.moveL_FK(joint_positions, env.get_speed(), env.get_acceleration())

@when('the robot "{identifier}" moves to position "{position}" with "{speed}" speed')
def step_when(context, identifier : str, position, speed : str):

    joint_positions = env.get_position(position)
    controller = context.controller
    
    controller.moveJ(joint_positions, env.get_speed(speed), env.get_acceleration(speed))

@when('the robot "{identifier}" linearly moves to position "{position}" with "{speed}" speed')
def step_when(context, identifier : str, position, speed : str):

    joint_positions = env.get_position(position)
    controller = context.controller
    
    controller.moveL_FK(joint_positions, env.get_speed(speed), env.get_acceleration(speed))


@when('the gripper "{identifier}" {action}')
def step_then(context, identifier : str, action):
    desired_action_open = (action=="opens")
    if (desired_action_open):
        context.gripper.open()
    else:
        context.gripper.close()
    

'''

@then('the position of the robot "{identifier}" is "{position}"')
def step_then(context, identifier : str, position):
    pass

@then('the signal of the sensor "{identifier}" is "{state}"')
def step_then(context, identifier : str, state):
    pass
    ''
    sensor_state = (state == "ON")

    t_end = time.time() + 10
    while time.time() < t_end:

        input_bits  = context.reciever.getActualDigitalInputBits()
        actual_state = env.get_digital_input_state(env.get_digital_input(identifier), input_bits)

        if actual_state == sensor_state :
            assert True
            break
    
    post_input_bits  = context.reciever.getActualDigitalInputBits()
    post_state = env.get_digital_input_state(env.get_digital_input(identifier), input_bits)

    if post_state != sensor_state :        
        assert False
    ''

@then('the output "{identifier}" is {state}')
def step_then(context, identifier : str, state):
    signal = (state=="ON")
    output = env.getDigitalOutput(identifier)
    context.io.setStandardDigitalOut(output, signal)

@then('the gripper "{identifier}" is {state}')
def step_then(context, identifier : str, state):
    pass
    ''
    desired_state_open = (state=="opened")
    if (desired_state_open):
        context.gripper.open()
    else:
        context.gripper.close()
    ''
'''