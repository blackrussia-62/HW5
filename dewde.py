import requests

api = "https://fake-json-api.mock.beeceptor.com"

pnts = [
    "/users/1",
    "/companies/1",
    "/customers"
]

for pnt in pnts:
    try:
        url = api + pnt
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Успешный запрос к {url}")
            print("Ответ:", response.json())
        else:
            print(f"Ошибка при запросе к {url}. Код статуса: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка! {url}: {e}")
