Feature: Customers need to be able to update their personal information

  Scenario Outline: As a new customer, I should not be able to use data not meeting standards
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    When  I click the Manage Customer Information button
    When  I click "Update Customer Information"
    When  I enter <first_name> in the update first name
    When  I enter <last_name> in the update last name
    When  I enter <new_username> in the update username
    When  I enter <new_password> in the update password
    When  I enter <email_address> in the update email address
    When  I enter <phone_number> in the update phone number
    When  I enter <address> in the update address
    When  I click the Update Customer button
    When  I click ok on the alert
    Then  I should be on a page with the title Managing Customer

    Examples:
      | first_name                                                     | last_name                                                      | new_username                                                   | new_password                                                   | email_address                                                  | phone_number                                                   | address                                                        | username | password |
      | this is too long and so it will fail and bring a desired error | last                                                           | new                                                            | customer                                                           | add@email.com                                                  | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       | new      | customer |
      | first                                                          | this is too long and so it will fail and bring a desired error | new                                                            | customer                                                           | add@email.com                                                  | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       | new      | customer |
      | first                                                          | last                                                           | this is too long and so it will fail and bring a desired error | customer                                                       | add@email.com                                                  | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       | new      | customer |
      | first                                                          | last                                                           | new                                                            | this is too long and so it will fail and bring a desired error | add@email.com                                                  | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       | new      | customer |
      | first                                                          | last                                                           | new                                                            | customer                                                           | this is too long and so it will fail and bring a desired error | 123-456-7890                                                   | 123 T St Oats, OH, 78513                                       | new      | customer |
      | first                                                          | last                                                           | new                                                            | customer                                                           | add@email.com                                                  | this is too long and so it will fail and bring a desired error | 123 T St Oats, OH, 78513                                       | new      | customer |
      | first                                                          | last                                                           | new                                                            | customer                                                           | add@email.com                                                  | 123-456-7890                                                   | this is too long and so it will fail and bring a desired error | new      | customer |
      | first                                                          | last                                                           | new                                                            | customer                                                           | add@email.com                                                  | wrong                                                          | 123 T St Oats, OH, 78513                                       | new      | customer |

  Scenario Outline: As a new customer, I should be able to create a relationship with the bank
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    When  I click the Manage Customer Information button
    When  I click "Update Customer Information"
    When  I enter <first_name> in the update first name
    When  I enter <last_name> in the update last name
    When  I enter <new_username> in the update username
    When  I enter <new_password> in the update password
    When  I enter <email_address> in the update email address
    When  I enter <phone_number> in the update phone number
    When  I enter <address> in the update address
    When  I click the Update Customer button
    When  I click ok on the alert
    Then  I should be on a page with the title Managing Customer

    Examples:
      | first_name | last_name | new_username | new_password | email_address | phone_number | address                  | username | password |
      | first      | last      | new          | customer     | add@email.com | 123-456-7890 | 123 T St Oats, OH, 78513 | new      | customer |

