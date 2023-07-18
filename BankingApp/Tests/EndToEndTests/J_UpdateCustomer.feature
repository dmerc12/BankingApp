Feature: Customers need to be able to update their personal information

  Scenario Outline: As a customer, I should not be able to use data not meeting standards when updating my information
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Information navigation button
    When  I click the Update Your Information navigation button
    When  I enter <first_name> in the update first name input
    When  I enter <last_name> in the update last name input
    When  I enter <email_address> in the update email address input
    When  I enter <phone_number> in the update phone number input
    When  I enter <street_address> in the update street address input
    When  I enter <city> in the update city input
    When  I enter <state> in the update state input
    When  I enter <zip_code> in the update zip code input
    When  I click the Update Information button
    Then  I should be on a page with the title Updating Your Information

    Examples:
      | first_name                                                     | last_name                                                      | email_address  | password | phone_number                                                   | street_address                                                 | city | state | zip_code |
      | this is too long and so it will fail and bring a desired error | last                                                           | test@email.com | work     | 1234567890                                                     | 123 T St                                                       | Oats | OH    | 43015    |
      | first                                                          | this is too long and so it will fail and bring a desired error | test@email.com | work     | 1234567890                                                     | 123 T St                                                       | Oats | OH    | 43015    |
      | first                                                          | last                                                           | test@email.com | work     | 1234567890                                                     | 123 T St                                                       | Oats | OH    | 43015    |
      | first                                                          | last                                                           | test@email.com | work     | this is too long and so it will fail and bring a desired error | 123 T St                                                       | Oats | OH    | 43015    |
      | first                                                          | last                                                           | test@email.com | work     | 1234567890                                                     | this is too long and so it will fail and bring a desired error | Oats | OH    | 43015    |
      | first                                                          | last                                                           | test@email.com | work     | 1234567890                                                     | 123 T St                                                       | Oats | OH    | 43015    |


  Scenario Outline: As a new customer, I should be able to update my information with the bank
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Information navigation button
    When  I click the Update Your Information navigation button
    When  I enter <first_name> in the update first name input
    When  I enter <last_name> in the update last name input
    When  I enter <email_address> in the update email address input
    When  I enter <phone_number> in the update phone number input
    When  I enter <street_address> in the update street address input
    When  I enter <city> in the update city input
    When  I enter <state> in the update state input
    When  I enter <zip_code> in the update zip code input
    When  I click the Update Information button
    Then  I should be on a page with the title Managing Your Current Information

    Examples:
      | first_name | last_name | email_address  | password | phone_number | street_address | city | state | zip_code |
      | first      | last      | test@email.com | work     | 1234567890   | 123 T St       | Oats | OH    | 43015    |
