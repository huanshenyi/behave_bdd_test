Feature: Register User

     As a developer
     This is my first bdd project
     Scenario: open register website
         When I open the register website "http://www.5itest.cn/register"
         Then I expect that the title is "注册"


     Scenario: input username
         When I set with useremail "mushishid1@qq.com"
         And I set with username "mushishid1"
         And I set with password "mushish"
         And I set with code "resd"
         And I click with registerbutton
         Then I expect that text "验证码错误"