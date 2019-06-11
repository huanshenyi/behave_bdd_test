# 実行環境の初期化
# coding=utf-8
from selenium import webdriver
import os

driver_path = os.path.abspath(os.path.join(os.getcwd(), ".."))+"\driver\chromedriver.exe"

def before_all(context):
    context.driver = webdriver.Chrome(r"D:\program\automation_test\python_bdd\driver\chromedriver.exe")

def after_all(context):
    context.driver.close()