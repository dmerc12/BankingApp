Feature: A customer needs to be able to use the navigation bar.

  Scenario Outline: As a customer, I click the register button in the navigation bar
    Given I am on the login page
    When  I click the register button in the navigation bar
    Then  I am on a page with the title <title>

    Examples:
      | title       |
      | Registering |

  Scenario Outline: As a customer, I click the login button in the navigation bar
    Given I am on the login page
    When  I click the register button in the navigation bar
    When  I click the login button in the navigation bar
    Then  I am on a page with the title <title>

    Examples:
      | title      |
      | Logging In |

  Scenario Outline: As a customer, I click the manage information button in the navigation bar
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage information button in the navigation bar
    Then  I am on a page with the title <title>

    Examples:
      | email          | password | title            |
      | test@email.com | work     | Managing Current Information|

  Scenario Outline: As a customer, I click the manage accounts button in the navigation bar
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage accounts button in the navigation bar
    Then  I am on a page with the title <title>

    Examples:
      | email          | password | title             |
      | test@email.com | work     | Managing Accounts |

  Scenario Outline: As a customer, I click the home button in the navigation bar
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage accounts button in the navigation bar
    When  I click the home button in the navigation bar
    Then  I am on a page with the title <title>

    Examples:
      | email          | password | title |
      | test@email.com | work     | Home  |
