



Feature: Moving product from conveyor 1 to conveyor 2

	Scenario: Given the item "lego" is assembled
        Given the output "active light" is OFF
        And the signal of the input "ready" is "ON"
        And the gripper "two-finger" is opened
        When the output "active light" turns ON
        And the robot "Assembler" moves to position "above point 2"
        And the robot "Assembler" linearly moves to position "point 2"
        And the gripper "two-finger" closes
        And the robot "Assembler" moves to position "point 1" with "fast" speed
        Then the gripper "two-finger" is opened

	Scenario: When the assembler #1 inserts the item "block"
        Given the position of the robot "Assembler" is "above point 3"
        And the gripper "two-finger" is opened
        When the robot "Assembler" linearly moves to position "point 3" with "slow" speed
        And the gripper "Two-finger" closes
        And the robot "Assembler" moves to position "above point 1" with "fast" speed
        Then the gripper "two-finger" is opened

	Scenario: Then the item assembling is done
        Given the signal of the input "done" is "ON"
        When the robot "Assembler" moves to position "default" with "fast" speed
        Then the output "active light" is OFF