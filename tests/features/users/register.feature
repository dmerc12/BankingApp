Feature: Users need to be able to register with the website

    Scenario Outline: As a user, I should not be able to register with invalid information
        Given I am on the register page
        When  I enter <username> in the register username field
        When  I enter <first_name> in the register first name field
        When  I enter <last_name> in the register last name field
        When  I enter <email> in the register email field
        When  I enter <phone_number> in the register phone number field
        When  I enter <password1> in the register password1 field
        When  I enter <password2> in the register password2 field
        When  I click the register button
        Then  I should be on a page with the title <title>

        Examples:
        |username|first_name|last_name|email|phone_number|password1|password2|title|
        |''|''|''|''|''|''|''|'Register'|
        |'this is too long and so it should fail validation checks that are put onto the register form, and so once it fails it will cause the test to pass and be successful and again the test will pass but this has to be super long so that it fails the validation check on the form'|'this is too long and so it should fail validation checks that are put onto the register form, and so once it fails it will cause the test to pass and be successful and again the test will pass but this has to be super long so that it fails the validation check on the form'|'this is too long and so it should fail validation checks that are put onto the register form, and so once it fails it will cause the test to pass and be successful and again the test will pass but this has to be super long so that it fails the validation check on the form'|'thisfieldwillraiseanexceptionifthisfieldisover150characterssoithastobeverylongbutstillbeinanemailtypeformatasthatischeckedfirstbutithastobeextremelylongtocausethevalidationcheckjustincasesomeonejusthasalongemail@example.com'|'this is too long and so it will fail the validation check'|'this field won't raise a too long exception'|'this field won't raise a too long exception'|'Register'|
        |'test'|'test'|'test'|'test example dot com'|'91-324-567-3432'|'usernumber1'|'usernumber1'|'Dashboard'|
        |'test'|'test'|'test'|'test@example.com'|'91-324-567-3432'|'testtest'|'testtest'|'Dashboard'|
        |'test'|'test'|'test'|'test@example.com'|'91-324-567-3432'|'password1'|'password2'|'Dashboard'|

    Scenario Outline: As a user, I should be able to register with valid information
        Given I am on the register page
        When  I enter <username> in the register username field
        When  I enter <first_name> in the register first name field
        When  I enter <last_name> in the register last name field
        When  I enter <email> in the register email field
        When  I enter <phone_number> in the register phone number field
        When  I enter <password1> in the register password1 field
        When  I enter <password2> in the register password2 field
        When  I click the register button
        Then  I should be on a page with the title <title>

        Examples:
        |username|first_name|last_name|email|phone_number|password1|password2|title|
        |'test'|'test'|'test'|'test@example.com'|'91-324-567-3432'|'usernumber1'|'usernumber1'|'Dashboard'|
        