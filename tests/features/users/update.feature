Feature: Users need to be able to update their profile with the website

    Scenario Outline: As a user, I should not be able to update my profile with the website when not meeting requirements
        Given I am on the login page
        When  I enter <username> in the login username field
        When  I enter <password> in the login password field
        When  I click the login button
        When  I click the navbar dropdown toggle
        When  I click the update user dropdown button
        When  I enter <first_name> in the update first name field
        When  I ender <last_name> in the update last name field
        When  I enter <new_username> in the update username field
        When  I enter <email> in the update email field
        When  I enter <phone_number> in the update phone number field
        When  I click the update user button
        Then  I should be on a page with the title <title>

        Examples:
        |username|password|first_name|last_name|new_username|email|phone_number|title|
        |'test'|'usernumber1'|''|''|''|''|''|'Update Profile'|
        |'test'|'usernumber1'|'this is too long and so it should fail validation checks that are put onto the register form, and so once it fails it will cause the test to pass and be successful and again the test will pass but this has to be super long so that it fails the validation check on the form'|'this is too long and so it should fail validation checks that are put onto the register form, and so once it fails it will cause the test to pass and be successful and again the test will pass but this has to be super long so that it fails the validation check on the form'|'this is too long and so it should fail validation checks that are put onto the register form, and so once it fails it will cause the test to pass and be successful and again the test will pass but this has to be super long so that it fails the validation check on the form'|'thisfieldwillraiseanexceptionifthisfieldisover150characterssoithastobeverylongbutstillbeinanemailtypeformatasthatischeckedfirstbutithastobeextremelylongtocausethevalidationcheckjustincasesomeonejusthasalongemail@example.com'|'this is too long and so it will fail the validation check'|'Update Profile'|
        |'test'|'usernumber1'|'updated'|'updated'|'updated'|'updated example dot com'|'91-324-567-3432'|'Update Profile'|
        |'test'|'usernumber1'|'updated'|'updated'|'updated'|'updated@example.com'|'91-324-567-3432'|'Update Profile'|
        |'test'|'usernumber1'|'updated'|'updated'|'updated'|'updated@example.com'|'91-324-567-3432'|'Update Profile'|

    Scenario Outline: As a user, I should be able to update my profile with the website when meeting requirements
        Given I am on the login page
        When  I enter <username> in the login username field
        When  I enter <password> in the login password field
        When  I click the login button
        When  I click the navbar dropdown toggle
        When  I click the update user dropdown button
        When  I enter <first_name> in the update first name field
        When  I ender <last_name> in the update last name field
        When  I enter <new_username> in the update username field
        When  I enter <email> in the update email field
        When  I enter <phone_number> in the update phone number field
        When  I click the update user button
        Then  I should be on a page with the title <title>

        Examples:
        |username|password|first_name|last_name|new_username|email|phone_number|title|
        |'test'|'usernumber1'|'changed'|'info'|'changedinfo'|'changed@email.com'|'21-333-555-2222'|'Dashboard'|
