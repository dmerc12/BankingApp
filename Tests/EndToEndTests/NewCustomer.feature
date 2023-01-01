Feature: Customers need to create a relationship with the bank

  Scenario: As a new customer I need to create login credentials
    Given I am on the login page
    When  I click the New Customer button
    Then  I should be on a page with the title New Customer

  Scenario Outline: As a new customer, I should not be able to have unreasonably long inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name                                                     | last name | username | password | email address | phone number | address                  |
      | this is too long and so it will fail and bring a desired error | last      | new      | customer | add@email.com | 123-456-7890 | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have unreasonably long inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name                                                      | username | password | email address | phone number | address                  |
      | first      | this is too long and so it will fail and bring a desired error | new      | customer | add@email.com | 123-456-7890 | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have unreasonably long inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username                                                       | password | email address | phone number | address                  |
      | first      | last      | this is too long and so it will fail and bring a desired error | customer | add@email.com | 123-456-7890 | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have unreasonably long inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password                                                       | email address | phone number | address                  |
      | first      | last      | new      | this is too long and so it will fail and bring a desired error | add@email.com | 123-456-7890 | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have unreasonably long inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address                                                  | phone number | address                  |
      | first      | last      | new      | customer | this is too long and so it will fail and bring a desired error | 123-456-7890 | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have unreasonably long inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address | phone number                                                   | address                  |
      | first      | last      | new      | customer | add@email.com | this is too long and so it will fail and bring a desired error | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have unreasonably long inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address | phone number | address                                        |
      | first      | last      | new      | customer | add@email.com | 123-456-7890 | this is too long and so it will fail and bring a desired error|

  Scenario Outline: As a new customer, I should not be able to have a phone number with a format differing from xxx-xxx-xxxx
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address | phone number | address                  |
      | first      | last      | new      | customer | add@email.com | wrong        | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have an address that does not contain a street and city, state, and zip code
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address | phone number | address          |
      | first      | last      | new      | customer | add@email.com | 123-456-7890 | incorrect format |

  Scenario Outline: As a new customer, I should not be able to have an email address differing a format of something@something.something
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address    | phone number | address                  |
      | first      | last      | new      | customer | incorrect format | 123-456-7890 | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have empty inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address | phone number | address                  |
      |            | last      | new      | customer | add@email.com | 123-456-7890 | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have empty inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address | phone number | address                  |
      | first      |           | new      | customer | add@email.com | 123-456-7890 | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have empty inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address | phone number | address                  |
      | first      | last      |          | customer | add@email.com | 123-456-7890 | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have empty inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address | phone number | address                  |
      | first      | last      | new      |          | add@email.com | 123-456-7890 | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have empty inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address | phone number | address                  |
      | first      | last      | new      | customer |               | 123-456-7890 | 123 T St Oats, OH, 78513 |

  Scenario Outline: As a new customer, I should not be able to have empty inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address | phone number | address                  |
      | first      | last      | new      | customer | add@email.com |              | 123 T St Oats, OH, 78513 |

 Scenario Outline: As a new customer, I should not be able to have empty inputs
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title New Customer

    Examples:
      | first name | last name | username | password | email address | phone number | address |
      | first      | last      | new      | customer | add@email.com | 123-456-7890 |         |

 Scenario Outline: As a new customer, I should be able to create a relationship with the bank
    Given I am on the new customer page
    When  I enter <first name> in the first name
    When  I enter <last name> in the last name
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I enter <email address> in the email address
    When  I enter <phone number> in the phone number
    When  I enter <address> in the address
    When  I click the Create New Customer button
    When  I click the Continue button
    Then  I should be on a page with the title Login Page

    Examples:
      | first name | last name | username | password | email address | phone number | address                  |
      | first      | last      | new      | customer | add@email.com | 123-456-7890 | 123 T St Oats, OH, 78513 |









