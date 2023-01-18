Feature: Customers need to create a relationship with the bank

  Scenario: As a new customer I need to create login credentials
    Given I am on the login page
    When  I click the New Customer button
    Then  I should be on a page with the title New Customer

  Scenario Outline: As a new customer, I should not be able to use data not meeting standards
    Given I am on the new customer page
    When  I enter <first_name> in the first name
    When  I enter <last_name> in the last name
    When  I enter <username> in the create username
    When  I enter <password> in the create password
    When  I enter <email_address> in the email address
    When  I enter <phone_number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click ok on the alert
    Then  I should be on a page with the title New Customer

    Examples:
      | first_name                                                     | last_name                                                      | username                                                       | password                                                       | email_address                                                  | phone_number                                                   | address                                                        |
      | this is too long and so it will fail and bring a desired error | last                                                           | new                                                            | customer                                                       | add@email.com                                                  | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |
      | first                                                          | this is too long and so it will fail and bring a desired error | new                                                            | customer                                                       | add@email.com                                                  | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | this is too long and so it will fail and bring a desired error | customer                                                       | add@email.com                                                  | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | new                                                            | this is too long and so it will fail and bring a desired error | add@email.com                                                  | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | new                                                            | customer                                                       | this is too long and so it will fail and bring a desired error | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | new                                                            | customer                                                       | add@email.com                                                  | this is too long and so it will fail and bring a desired error | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | new                                                            | customer                                                       | add@email.com                                                  | 123-456-7890                                                   | this is too long and so it will fail and bring a desired error |
      | first                                                          | last                                                           | new                                                            | customer                                                       | add@email.com                                                  | wrong                                                          | 123 T St Oats, OH, 78513                                       |
      | first                                                          | last                                                           | new                                                            | customer                                                       | add@email.com                                                  | 123-456-7890                                                   | incorrect format                                               |
      | first                                                          | last                                                           | new                                                            | customer                                                       | incorrect format                                               | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       |

  Scenario Outline: As a new customer, I should be able to create a relationship with the bank
    Given I am on the new customer page
    When  I enter <first_name> in the first name
    When  I enter <last_name> in the last name
    When  I enter <username> in the create username
    When  I enter <password> in the create password
    When  I enter <email_address> in the email address
    When  I enter <phone_number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

    Examples:
      | first_name | last_name | username | password | email_address | phone_number | address                  |
      | first      | last      | new      | customer | add@email.com | 123-456-7890 | 123 T St Oats, OH, 78513 |

