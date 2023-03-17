Feature: Customers need to create a relationship with the bank

  Scenario: As a new customer I need to create login credentials
    Given I am on the login page
    When  I click the Register button
    Then  I should be on a page with the title Register

  Scenario Outline: As a new customer, I should not be able to use data not meeting standards
    Given I am on the new customer page
    When  I enter <first_name> in the first name
    When  I enter <last_name> in the last name
    When  I enter <email_address> in the email address
    When  I enter <password> in the create password
    When  I enter <confirmation_password> in the confirmation password
    When  I enter <phone_number> in the phone number
    When  I enter <address> in the address
    When  I click the Register button
    Then  I should be on a page with the title Register

    Examples:
      | first_name                                                     | last_name                                                      | email_address                                                  | password                                                       | confirmation_password                                          | phone_number                                                   | address                                                        |
      | this is too long and so it will fail and bring a desired error | last                                                           | add@email.com                                                  | customer                                                       | customer                                                       | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |
      | first                                                          | this is too long and so it will fail and bring a desired error | add@email.com                                                  | customer                                                       | customer                                                       | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | this is too long and so it will fail and bring a desired error | customer                                                       | customer                                                       | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | add@email.com                                                  | this is too long and so it will fail and bring a desired error | customer                                                       | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | add@email.com                                                  | customer                                                       | this is too long and so it will fail and bring a desired error | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | add@email.com                                                  | customer                                                       | customer                                                       | this is too long and so it will fail and bring a desired error | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | add@email.com                                                  | customer                                                       | customer                                                       | 123-456-7890                                                   | this is too long and so it will fail and bring a desired error |
      | first                                                          | last                                                           | add@email.com                                                  | customer                                                       | customer                                                       | wrong                                                          | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | add@email.com                                                  | customer                                                       | wrong                                                          | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |


  Scenario Outline: As a new customer, I should be able to create a relationship with the bank
    Given I am on the new customer page
    When  I enter <first_name> in the first name
    When  I enter <last_name> in the last name
    When  I enter <email_address> in the email address
    When  I enter <password> in the create password
    When  I enter <confirmation_password> in the confirmation password
    When  I enter <phone_number> in the phone number
    When  I enter <address> in the address
    When  I click the Register button
    Then  I should be on a page with the title Login

    Examples:
      | first_name | last_name | email_address | password | confirmation_password | phone_number | address                  |
      | first      | last      | add@email.com | customer | customer              | 123-456-7890 | 123 T St Oats, OH, 78513 |

