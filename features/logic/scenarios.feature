



Feature: Scenario: "Robot move to a specific position"
    Scenario: Given the product "Box" is present
		Given the robot "1.23.42.22" is connected
		And the digitaloutput #1 is connected
		When the digitaloutput #1 turns ON
		Then the object "object" is available
    Scenario: When the packager #1 pick up the product "Box"
		Given the position of the object "Box" is [3,5,1]
		And the gripper "1.23.42.22" is connected
		And the gripper "1.23.42.22" is active
		When the robot "1.23.42.22" moves to pose [1,2.3,1,7.0323,9,1] with "moderate" speed 
		And the robot "1.23.42.22" linearly moves to pose [1,2,3,4,5,6]
		And the gripper "1.23.42.22" close
		And the robot "1.23.42.22" moves to pose [0.9,2,1.7,1.0323,3,1] with "high" speed
		Then the robot "1.23.42.22" is ready
    Scenario: Then the conveyor #1 is clear
		Given the digitaloutput #1 is connected
		When the digitaloutput #1 turns OFF
		Then the object "Box" is not detected


Feature: Scenario: "Robot move to a specific position"
    Scenario: Given the product "Box" is present
		Given the robot "1.23.42.22" is not connected
		And the digitaloutput #1 is not connected
		When the robot "1.23.42.22" connects
		And the digitaloutput #1 connects
		And the digitaloutput #1 turns ON
		Then the object "object" is available
		And the robot "1.23.42.22" is connected
    Scenario: When the packager #1 pick up the product "Box"
		Given the gripper "1.23.42.22" is connected
		When the robot "1.23.42.22" moves to pose [1,2.3,1,7.0323,9,1] with "moderate" speed 
		And the robot "1.23.42.22" linearly moves to pose [1,2,3,4,5,6]
		And the gripper "1.23.42.22" close
		And the robot "1.23.42.22" moves to pose [0.9,2,1.7,1.03,3,1] with "high" speed
		Then the robot "1.23.42.22" is ready
    Scenario: Then the conveyor #1 is clear
		Given the digitaloutput #1 is connected
		When the digitaloutput #1 turns OFF
		Then the object "Box" is not detected


Feature: Scenario: "Liked songs should appear in the liked-playlist"
    Scenario: Given the song "Solskin" is not liked And the playlist "Liked songs" is available   // "and" has to be caps
		Given the BrowserWindow "Song - Solskin" is displayed
		And the TabBar "Playlists" is available
		When I click on "Show details" for BrowserWindow "Song - Solskin"
		And click on TabBar "Playlists"
		Then the RadioButton "Liked" is not selected
		And the MenuItem "Liked songs" is displayed And the BrowserWindow "Playlists" is displayed 
    Scenario: When I like the song "Solskin"
		Given the RadioButton "Liked" is displayed
		When I click the RadioButton "Liked"
		Then the RadioButton "Liked" is selected
    Scenario: Then "the song Solskin is available in playlist Liked songs"
		Given the BrowserWindow "Playlists" is displayed
		When I click the Button "Liked songs"
		Then the Button "Solskin" is shown

Feature: Scenario: "Delete song from Playlist"
    Scenario: Given the song "Billie Jean" is available
		Given the BrowserWindow "Playlist" is displayed
		When I type "Billie Jean" into the SearchBox "Song search" 
		Then the BrowserWindow "Billie Jean" is displayed
    Scenario: When I delete the song "Billie Jean"
		Given the BrowserWindow "Edit : Billie Jean" is displayed
		When I click "Delete song"
		Then the Notification "Song has been deleted" is displayed
    Scenario: Then the song "Billie Jean" is removed
		Given the BrowserWindow "Playlist" is displayed
		When I type "Billie Jean" into the SearchBox "Song search"
		Then the Notification "No results found" is displayed


Feature: Scenario: Withdrawing money - transaction succeeded
    Scenario: Given the balance for the account "1787461" is 1000
		Given the BrowserWindow "Account Balance" is displayed
		When I click on "See the balance"
		Then the value for the TextField "Balance" is "1000"
    Scenario: When I transfer 1000 from the account "1787461"
		Given the BrowserWindow "SEPA Transfer" is displayed
		When I type "1000" into the field "Amount"
		Then the Notification "Your transfer has been successfully processed" is displayed
    Scenario: Then the account "1787461" is void
		Given the BrowserWindow "Account Balance" is displayed
		When I click on "See the balance"
		Then the value for the TextField "Balance" is "0"
		
		
Feature: Scenario: Withdrawing money - transaction failed
    Scenario: Given the balance for the account "1532531" is 200
		Given the BrowserWindow "Account Balance" is displayed
		When I click on "See the balance"
		Then the value for the TextField "Balance" is "200"
    Scenario: When I transfer 400 from the account "1532531"
		Given the BrowserWindow "SEPA Transfer" is displayed
		When I type "300" into the field "Amount"
		Then the Notification "Your transfer has been successfully processed" is not displayed
		And the Notification "Transaction failed - too big transfer" is displayed
    Scenario: Then the account "1532531" is void
		Given the BrowserWindow "Account Balance" is displayed
		When I click on "See the balance"
		Then the value for the TextField "Balance" is "200"