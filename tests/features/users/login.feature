Feature: Users need to be able to login to the website

    Scenario Outline: As a user, I should not be able to login with incorrect login credentials
        Given I am on the login page
        When  I enter <username> in the login username field
        When  I enter <password> in the login password field
        When  I click the login button
        Then  I should be on a page with the title <title>

        Examples:
        |username|password|title|
        |''|''|'Login'|
        |'test'|'incorrect'|'Login'|
        |'incorrect'|'incorrect'|'Login'|

    Scenario Outline: As a user, I should be able to login with correct login credentials
        Given I am on the login page
        When  I enter <username> in the login username field
        When  I enter <password> in the login password field
        When  I click the login button
        Then  I should be on a page with the title <title>

        Examples:
        |username|password|title|
        |'test'|'usernumber1'|'Dashboard'|
