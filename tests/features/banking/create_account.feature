Feature: Users need to be able to create an account

    Scenario Outline: As a user, I should not be able to create an account when not meeting requirements
        Given I am on the login page
        When  I enter <username> in the login username field
        When  I enter <password> in the login password field
        When  I click the login button
        When  I click the create account navigation button
        When  I input <account_number> in the create account account number field
        When  I input <bank_name> in the create account bank name field
        When  I input <location> in the create account location field
        When  I input <timestamp> in the create account timestamp field
        When  I input <opening_balance> in the create account opening balance field
        When  I input <opening_notes> in the create account opening notes field
        When  I click the create account button
        Then  I should be on a page with the title <title>

        Examples:
        |username|password|account_number|bank_name|location|timestamp|opening_balance|opening_notes|title|
        |'test'|'usernumber1'|0|''|''|''|0.00|'testing notes'|'Create Account'|
        |'test'|'usernumber1'|16294302|'test'|'test'|'2024-2-1'|-63.45|'testing notes'|'Create Account'|
        |'test'|'usernumber1'|16294302|'this is way too long and so it should fail and then my test will pass and I will not be mad that it did not pass the validation for creating an account because the notes should not be allowed to be this long or it will take up too much space in the database and cause too much overhead cost so this test should catch that for me'|'this is way too long and so it should fail and then my test will pass and I will not be mad that it did not pass the validation for creating an account because the notes should not be allowed to be this long or it will take up too much space in the database and cause too much overhead cost so this test should catch that for me'|'2024-2-1'|-63.45|'this is way too long and so it should fail and then my test will pass and I will not be mad that it did not pass the validation for creating an account because the notes should not be allowed to be this long or it will take up too much space in the database and cause too much overhead cost so this test should catch that for me'|'Create Account'|
        |'test'|'usernumber1'|16294302|'test'|'test'|'invalid format'|63.45|'testing notes'|'Create Account'|

    Scenario Outline: As a user, I should be able to create an account when meeting requirements
        Given I am on the login page
        When  I enter <username> in the login username field
        When  I enter <password> in the login password field
        When  I click the login button
        When  I click the create account navigation button
        When  I input <account_number> in the create account account number field
        When  I input <bank_name> in the create account bank name field
        When  I input <location> in the create account location field
        When  I input <timestamp> in the create account timestamp field
        When  I input <opening_balance> in the create account opening balance field
        When  I input <opening_notes> in the create account opening notes field
        When  I click the create account button
        Then  I should be on a page with the title <title>

        Examples:
        |username|password|account_number|bank_name|location|timestamp|opening_balance|opening_notes|title|
        |'test'|'usernumber1'|392034793|'test bank'|'location'|'2024-2-22'|50.35|'testing notes'|'Dashboard'|
