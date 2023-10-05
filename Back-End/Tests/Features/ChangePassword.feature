Feature: A customer needs to be able to change their current password.

  Scenario Outline: As a customer, I incorrectly change my password
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage information button
    When  I click the change password modal
    When  I input <updated_password> in the change password input
    When  I input <confirmation_password> in the change password confirmation input
    When  I click the change password button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email            | password | updated_password                                                   | confirmation_password                                              | expected_toast_text                                                              |
      | "test@email.com" | "work"   | ""                                                                 | "test"                                                             | "The password field cannot be left empty, please try again!"                     |
      | "test@email.com" | "work"   | "this is too long and so it will fail and raise the desired error" | "test"                                                             | "The password field cannot exceed 36 characters, please try again!"              |
      | "test@email.com" | "work"   | "test"                                                             | ""                                                                 | "The confirmation password cannot be left empty, please try again!"              |
      | "test@email.com" | "work"   | "test"                                                             | "this is too long and so it will fail and raise the desired error" | "The confirmation password field cannot exceed 36 characters, please try again!" |
      | "test@email.com" | "work"   | "don't"                                                            | "match"                                                            | "The passwords don't match, please try again!"                                   |
      | "test@email.com" | "work"   | "work"                                                             | "work"                                                             | "Nothing has changed, please try again!"                                         |

  Scenario Outline: As a customer, I correctly change my password
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage information button
    When  I click the change password modal
    When  I input <updated_password> in the change password input
    When  I input <confirmation_password> in the change password confirmation input
    When  I click the change password button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email            | password | updated_password | confirmation_password | expected_toast_text              |
      | "test@email.com" | "work"   | "test"           | "test"                | "Password successfully changed!" |
