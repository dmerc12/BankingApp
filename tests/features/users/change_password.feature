Feature: Users need to be able to change their password with the website

    Scenario Outline: As a user, I should not be able to change their password with the website when not meeting requirements
        Given I am on the login page
        When  I enter <username> in the login username field
        When  I enter <password> in the login password field
        When  I click the login button
        When  I click the navbar dropdown toggle
        When  I click the change password dropdown button
        When  I enter <new_password1> in the new password1 field
        When  I ender <new_password2> in the new password2 field
        When  I click the change password button
        Then  I should be on a page with the title <title>

        Examples:
        |username|password|password1|password2|title|
        |'test'|'usernumber1'|''|''|'Change Password'|
        |'test'|'usernumber1'|'testusernumber1'|'testuser1'|'Change Password'|
        |'test'|'usernumber1'|'updatedpassword'|'changepassword'|'Change Password'|

    Scenario Outline: As a user, I should be able to change their password with the website when meeting requirements
        Given I am on the login page
        When  I enter <username> in the login username field
        When  I enter <password> in the login password field
        When  I click the login button
        When  I click the navbar dropdown toggle
        When  I click the change password dropdown button
        When  I enter <new_password1> in the new password1 field
        When  I ender <new_password2> in the new password2 field
        When  I click the change password button
        Then  I should be on a page with the title <title>

        Examples:
        |username|password|password1|password2|title|
        |'test'|'usernumber1'|'updatedpassword'|'updatedpassword'|'Dashboard'|
