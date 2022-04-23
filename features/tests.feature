Feature: Moving product from conveyor 1 to conveyor 2

	Scenario: Given the product "Box" is present
        Given the signal of the sensor "sensor 1" is "OFF"
        When the output "conveyor 1" turns ON
        Then the signal of the sensor "sensor 1" is "ON"


	Scenario: When the packager #1 pick up the product "Box"

        Given the position of the robot "John Doe" is "above conveyor 1"
        When the robot "John Doe" linearly moves to position "conveyor 1" with "slow" speed
        And the gripper "Two-finger" closes
        And the robot "John Doe" moves to position "above conveyor 2"
        Then the signal of the sensor "sensor 1" is "OFF"


	Scenario: Then the conveyor 2 is loaded
        
        Given the position of the robot "John Doe" is "above conveyor 2"
        And the output "conveyor 2" is OFF
        And the signal of the sensor "sensor 2" is "OFF"
        When the robot "John Doe" linearly moves to position "conveyor 2" with "slow" speed
        And the gripper "Two-finger" opens
        Then the signal of the sensor "conveyor 2" is "ON"