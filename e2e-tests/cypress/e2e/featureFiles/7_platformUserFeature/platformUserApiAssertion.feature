Feature: User Management API asssertions
    Background:Navigates to the application platform
        Given Admin navigates to the user management tab and gets the platform user data from fixtures

    Scenario: Api assertion post landing on user management tab
        When Admin lands on the user management tab
        Then Api response post landing on user management tab should have message "Platform user fetched successfully" and status code 200
    @focus
    Scenario: Api assertion post user management search
        When Admin clicks on the user management table search button and Enters the valid data
        Then Api response post search should have message "Platform user fetched successfully" total records should be 1 and status code 200 in platform user table

    Scenario: Api assertion for deactivating the user management
        When Admin clicks on the user management table search button and Enters the valid data
        And Admin clicks on the deactivate user management button under the three dots menu
        And Api response post platform user update should have message "Platform user updated successfully." and status code 200
        Then Post deactivation platform user should get deactivated

    Scenario: Api assertion for activating the user management
        When Admin clicks on the user management table search button and Enters the valid data
        And Admin clicks on the activate user management button under the three dots menu
        And Api response post platform user update should have message "Platform user updated successfully." and status code 200
        Then Post activation platform user should get activated
    Scenario: Admin wants to update the user management and also assert the api response
        When Admin clicks on the user management table search button and Enters the valid data
        And Admin clicks on the edit user management button under the three dots menu
        And Admin updates the platform user form with the valid data
        Then Api response post platform user update should have message "Platform user updated successfully." and status code 200