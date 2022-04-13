Feature: Connect robot

	Scenario: "Robot move to a specific position"
		Given the robot "John Doe" is at position "middle"
		When the robot "John Doe" linearly moves to position "right corner"
		And the robot "John Doe" moves to position "left corner"
		Then the robot "John Doe" is moved

