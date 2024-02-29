Feature: Users need to be able to logout of the website

    Scenario Outline: As a user, I should be able to logout of the website
        Given I am on the login page
        When  I enter <username> in the login username field
        When  I enter <password> in the login password field
        When  I click the login button
        When  I click the navbar dropdown toggle
        When  I click the logout button
        Then  I should be on a page with the title <title>

        Examples:
        |username|password|title|
        |'test'|'usernumber1'|'Login'|
