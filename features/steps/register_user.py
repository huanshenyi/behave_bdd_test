from behave import *

use_step_matcher("re")
@when('I open the register website "([^"]*)"')
def step_register(context, url):
    # context.driver.get("http://www.5itest.cn/register")
    context.driver.get(url)


@then('I expect that the title is "([^"]*)"')
def step_register(context, title_name):
    title = context.driver.title
    assert title_name in title

@when('I set with useremail "([^"]*)"')
def step_register(context,useremail):
    context.driver.find_element_by_id("register_email").send_keys(useremail)

@when('I set with username "([^"]*)"')
def step_register(context, username):
    context.driver.find_element_by_id("register_nickname").send_keys(username)

@when('I set with password "([^"]*)"')
def step_register(context, password):
    context.driver.find_element_by_id("register_password").send_keys(password)

@when('I set with code "([^"]*)"')
def step_register(context, code):
    context.driver.find_element_by_id("captcha_code").send_keys(code)

@when('I click with registerbutton')
def step_register(context):
    context.driver.find_element_by_id("register-btn").click()

@then('I expect that text "([^"]*)"')
def setp_register(context,code_text):
    text = context.driver.find_element_by_id("captcha_code-error").text
    assert code_text in text
