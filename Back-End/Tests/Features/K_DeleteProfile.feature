Feature: A customer needs to be able to close all accounts and delete their profile with the bank.

  Scenario Outline: As a customer, I correctly delete my profile
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage information button
    When  I click the delete profile modal
    When  I click the delete profile button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email             | password | expected_toast_text                    |
      | updated@email.com | test     | Profile successfully deleted, goodbye! |
