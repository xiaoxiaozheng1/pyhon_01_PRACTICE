# post请求json类型
"""
需求：
需求：
1. 请求微商城项目的登录接口，请求数据（ {"username":"admin123","password":"admin123"}）
2. 登录接口URL：http://121.196.13.152:8080/admin/auth/login
"""
# 1. 导包
import requests

# 2. 请求post方法
login_url = "http://121.196.13.152:8080/admin/auth/login"
login_data = {"username": "admin123", "password": "admin123"}
headers = {"Content-Type": "application/json"}
response = requests.post(login_url, json=login_data, headers=headers)
print(response.text)
