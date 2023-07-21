Feature: Customers need to be able to change their passwords

  Scenario Outline: As a customer, I should not be able to use data not meeting standards when changing my password
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Information navigation button
    When  I click the Change Password navigation button
    When  I enter <updated_password> in the update password input
    When  I enter <confirmation_password> in the update password confirmation input
    When  I click the Change Password button
    Then  I should be on a page with the title Changing Your Password

    Examples:
      | email          | password | updated_password                                               | confirmation_password                                          |
      | test@email.com | work     | this is too long and so it will fail and bring a desired error | this is fine                                                   |
      | test@email.com | work     | this is fine                                                   | this is too long and so it will fail and bring a desired error |
      | test@email.com | work     | this is fine                                                   | this doesn't match                                             |
      | test@email.com | work     | work                                                           | work                                                           |


  Scenario Outline: As a customer, I should be able to change my password
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Information navigation button
    When  I click the Change Password navigation button
    When  I enter <updated_password> in the update password input
    When  I enter <confirmation_password> in the update password confirmation input
    When  I click the Change Password button
    Then  I should be on a page with the title Managing Your Current Information

    Examples:
      | email          | password | updated_password | confirmation_password |
      | test@email.com | work     | test             | test                  |

