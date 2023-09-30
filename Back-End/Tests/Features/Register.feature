Feature: As a new customer I need to register a profile with the banking system.

  Scenario Outline: As a new customer, I input the needed information incorrectly to register a profile.
    Given I am on the login page
    When  I click the register tab in the nav bar
    When  I input <first_name> in the register first name input
    When  I input <last_name> in the register last name input
    When  I input <email> in the register email input
    When  I input <password> in the register password input
    When  I input <confirmation_password> in the register confirmation password input
    When  I input <phone_number> in the register phone number input
    When  I input <street_address> in the register street address input
    When  I input <city> in the register city input
    When  I input <state> in the register state input
    When  I input <zip_code> in the register zip code input
    When  I click the register button
    Then  I remain on the register page

    Examples:
      | first_name                                                                   | last_name                                                                    | email                                                                        | password                                                                     | confirmation_password                                                        | phone_number                                                                 | street_address                                                               | city    | state | zip_code  |
      | 123                                                                          | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | ""                                                                           | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "this is too long and so it should fail and raise the desired error message" | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | 123                                                                          | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | ""                                                                           | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "this is too long and so it should fail and raise the desired error message" | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | 123                                                                          | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | ""                                                                           | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "this is too long and so it should fail and raise the desired error message" | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | 123                                                                          | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | ""                                                                           | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | "this is too long and so it should fail and raise the desired error message" | "first"                                                                      | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | 123                                                                          | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | ""                                                                           | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | "this is too long and so it should fail and raise the desired error message" | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | "incorrect"                                                                  | "123-456-7890"                                                               | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | 123                                                                          | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | ""                                                                           | "123 First St"                                                               | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | "this is too long and so it should fail and raise the desired error message" | ""123 First St""                                                             | "First" | "OK"  | ""73072"" |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | "this is too long and so it should fail and raise the desired error message" | "First" | "OK"  | "73072"   |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | 123                                                                          | 1       | 22    | 73072     |
      | "first"                                                                      | "last"                                                                       | "first@email.com"                                                            | "first"                                                                      | "first"                                                                      | "123-456-7890"                                                               | ""                                                                           | ""      | ""    | ""        |
      | "test"                                                                       | "customer"                                                                   | "test@email.com"                                                             | "work"                                                                       | "work"                                                                       | "123-456-7890"                                                               | "123 This Street"                                                            | "City"  | "OK"  | "73093"   |

  Scenario Outline: As a new customer, I successfully input the needed information to register a profile.
    Given I am on the login page
    When  I click the register tab in the nav bar
    When  I input <first_name> in the register first name input
    When  I input <last_name> in the register last name input
    When  I input <email> in the register email input
    When  I input <password> in the register password input
    When  I input <confirmation_password> in the register confirmation password input
    When  I input <phone_number> in the register phone number input
    When  I input <street_address> in the register street address input
    When  I input <city> in the register city input
    When  I input <state> in the register state input
    When  I input <zip_code> in the register zip code input
    When  I click the register button
    Then  I am routed back to the login page

    Examples:
      | first_name | last_name | email             | password | confirmation_password | phone_number   | street_address | city    | state | zip_code |
      | "first"    | "last"    | "first@email.com" | "first"  | "first"               | "123-456-7890" | "123 First St" | "First" | "OK"  | "73072"  |
