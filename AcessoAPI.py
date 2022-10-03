import requests
url = "https://localhost:44309/api/vendas/ListarPedidos"
recebido = requests.get(url, verify = False)
print(recebido.json())