Feature: Test navigation between pages
  Make sure homepage can go to blog, and
  blog can go to homepage

  Scenario: Homepage can go to Blog
    Given I am on the homepage
    When I click on the link with id "Go to blog"
    Then I am on the blog page

  Scenario: Blog page can go to homepage
    Given I am on the blog page
    When I click on the link with id "Go to home"
    Then I am on the homepage
