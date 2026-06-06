import requests

res = requests.post(
    "https://redz.up.railway.app/post",
    headers={"Authorization": "SUA_API_KEY_AQUI"},
    data="oi"
)

print(res.json()["choices"][0]["message"]["content"])
