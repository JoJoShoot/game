import requests

# 定义企业 ID 和应用 Secret
corpid = 'ww56f308b196999eb9'
corpsecret = 'KE1eHZzgkU0tgvX5d4eYWxo2MzaQmg8xEatd4nv8gW0'

# 构造请求 URL
url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'

# 发送 GET 请求并获取响应结果
response = requests.get(url).json()

# 打印响应结果
print(response)

if 'access_token' in response:
    access_token = response['access_token']
    print(access_token)
else:
    print("无法获取 access_token")