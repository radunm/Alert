# Created by Radu at 12.03.2020
Feature: Tests for alerts

  Scenario: Create page with alerts
    Given Open https://www.amazon.com/ main page
#    Given Open https://www.bestbuy.com/ main page
    When Alert is open
    Then We can close Alert
    When Confirm is open
    Then We can close confirm
    When Prompt is open
    Then We can close Prompt