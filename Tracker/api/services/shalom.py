import requests

>>> url = "https://servicesweb.shalomcontrol.com/api/v1/web/rastrea/buscar"

>>> payload = {
...     "numero": "NNNNNNNNN", #8
...     "codigo": "nnnn"#4
... }

>>> headers = {
...     "Content-Type": "application/json" 
... }

>>> response = requests.post(url, json=payload, headers=headers)
