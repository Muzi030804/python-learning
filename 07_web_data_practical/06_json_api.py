from asyncio import exceptions

import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1,
}

headers = {
    "Accept": "application/json",
}
try:

    response = requests.get(url, params=params, headers=headers, timeout=5)
    response.raise_for_status()
    datas = response.json()
    for data in datas[:3]:
        print(f"{data['id']}|{data['title']}")
    print(f"文章总数: {len(datas)}")
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.HTTPError as err:
    print(f"连接失败:{err}")
except requests.exceptions.RequestException as err:
    print(f"请求失败:{err}")


