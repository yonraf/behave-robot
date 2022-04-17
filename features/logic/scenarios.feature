Feature: Test
    Scenario: "Robot move to a specific position"
		Given the robot "1.23.42.22" is connected
		And the digitaloutput #1 is connected
		When the digitaloutput #1 turns ON
		Then the object "object" is available
		Given the position of the object "Box" is [3,5,1]
		And the gripper "1.23.42.22" is connected
		And the gripper "1.23.42.22" is active
		When the robot "1.23.42.22" moves to position [1,2.3,1,7.0323,9,1] with "moderate" speed 
		And the robot "1.23.42.22" moves along path [[1,2,3,4,5,6],[1,2,3,4,5,6]]
		And the gripper "1.23.42.22" close
		And the robot "1.23.42.22" moves to position [0.9,2,1.7,1.0323,3,1] with "high" speed
		Then the robot "1.23.42.22" is ready
		Given the digitaloutput #1 is connected
		When the digitaloutput #1 turns OFF
		Then the object "Box" is not detected