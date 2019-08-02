from behave import *
from selenium import webdriver

from tests.acceptance.pages.base_page import BasePage
from tests.acceptance.pages.blog_page import BlogPage
from tests.acceptance.pages.home_page import HomePage
from tests.acceptance.pages.new_post_page import NewPostPage


use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@given('I am on the new post page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = NewPostPage(context.driver)
    context.driver.get(page.url)


@then('I am on the homepage')
def step_impl(context):
    page = HomePage(context.driver)
    print(context.driver.current_url, page.url)
    assert context.driver.current_url == page.url


@then('I am on the blog page')
def step_impl(context):
    page = BlogPage(context.driver)
    print(context.driver.current_url, page.url)
    assert context.driver.current_url == page.url
