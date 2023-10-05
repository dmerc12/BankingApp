Feature: A customer needs to be able to update their current information.

  Scenario Outline: As a customer, I incorrectly update my information
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage information button
    When  I click the update information modal
    When  I input <first_name> in the update first name input
    When  I input <last_name> in the update last name input
    When  I input <updated_email> in the update email input
    When  I input <phone_number> in the update phone number input
    When  I input <street_address> in the update street address input
    When  I input <city> in the update city input
    When  I input <state> in the update state input
    When  I input <zip_code> in the update zip code input
    When  I click the update information button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email            | password | first_name                                                           | last_name                                                            | updated_email                                                        | phone_number                                                         | street_address                                                       | city      | state | zip_code | expected_toast_text                                                     |
      | "test@email.com" | "work"   | ""                                                                   | "last"                                                               | "updated@email.com"                                                  | "9998887777"                                                         | "123 Updated St"                                                     | "Updated" | "OK"  | "73072"  | "The first name field cannot be empty, please try again!"               |
      | "test@email.com" | "work"   | "this is too long and so it should fail and bring the desired error" | "last"                                                               | "updated@email.com"                                                  | "9998887777"                                                         | "123 Updated St"                                                     | "Updated" | "OK"  | "73072"  | "The first name field cannot exceed 36 characters, please try again!"   |
      | "test@email.com" | "work"   | "first"                                                              | ""                                                                   | "updated@email.com"                                                  | "9998887777"                                                         | "123 Updated St"                                                     | "Updated" | "OK"  | "73072"  | "The last name field cannot be empty, please try again!"                |
      | "test@email.com" | "work"   | "first"                                                              | "this is too long and so it should fail and bring the desired error" | "updated@email.com"                                                  | "9998887777"                                                         | "123 Updated St"                                                     | "Updated" | "OK"  | "73072"  | "The last name field cannot exceed 36 characters, please try again!"    |
      | "test@email.com" | "work"   | "first"                                                              | "last"                                                               | ""                                                                   | "9998887777"                                                         | "123 Updated St"                                                     | "Updated" | "OK"  | "73072"  | "The email field cannot be empty, please try again!"                    |
      | "test@email.com" | "work"   | "first"                                                              | "last"                                                               | "this is too long and so it should fail and bring the desired error" | "9998887777"                                                         | "123 Updated St"                                                     | "Updated" | "OK"  | "73072"  | "The email field cannot exceed 60 characters, please try again!"        |
      | "test@email.com" | "work"   | "first"                                                              | "last"                                                               | "updated@email.com"                                                  | ""                                                                   | "123 Updated St"                                                     | "Updated" | "OK"  | "73072"  | "The phone number field cannot be empty, please try again!"             |
      | "test@email.com" | "work"   | "first"                                                              | "last"                                                               | "updated@email.com"                                                  | "this is too long and so it should fail and bring the desired error" | "123 Updated St"                                                     | "Updated" | "OK"  | "73072"  | "The phone number field cannot exceed 12 characters, please try again!" |
      | "test@email.com" | "work"   | "first"                                                              | "last"                                                               | "updated@email.com"                                                  | "9998887777"                                                         | ""                                                                   | ""        | ""    | ""       | "The address field cannot be empty, please try again!"                  |
      | "test@email.com" | "work"   | "first"                                                              | "last"                                                               | "updated@email.com"                                                  | "9998887777"                                                         | "this is too long and so it should fail and bring the desired error" | "Updated" | "OK"  | "73072"  | "The address field cannot exceed 60 characters, please try again!"      |
      | "test@email.com" | "work"   | "test"                                                               | "customer"                                                           | "test@email.com"                                                     | "1234567890"                                                         | "123 This Street"                                                    | "City"    | "OK"  | "73093"  | "No information has changed!"                                           |

  Scenario Outline: As a customer, I correctly update my information
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage information button
    When  I click the update information modal
    When  I input <first_name> in the update first name input
    When  I input <last_name> in the update last name input
    When  I input <updated_email> in the update email input
    When  I input <phone_number> in the update phone number input
    When  I input <street_address> in the update street address input
    When  I input <city> in the update city input
    When  I input <state> in the update state input
    When  I input <zip_code> in the update zip code input
    When  I click the update information button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email            | password | first_name | last_name | updated_email       | phone_number | street_address   | city      | state | zip_code | expected_toast_text                |
      | "test@email.com" | "work"   | "first"    | "last"    | "updated@email.com" | "9998887777" | "123 Updated St" | "Updated" | "OK"  | "73072"  | "Information successfully updated" |
