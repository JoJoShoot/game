import requests

corpid = 'ww56f308b196999eb9'
corpsecret = 'KE1eHZzgkU0tgvX5d4eYWxo2MzaQmg8xEatd4nv8gW0'

# 构造请求 URL
url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'

# 发送 GET 请求并获取响应结果
response = requests.get(url).json()

print(response)

# 获取 access_token
access_token = response['access_token']