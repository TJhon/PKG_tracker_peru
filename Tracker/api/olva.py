import requests
from ..models.olva import olva_response


class OlvaService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = (
            "https://reports.olvaexpress.pe/webservice/rest/getTrackingInformation"
        )

    def get_tracking(self, tracking_number, year="2024"):
        params = {
            "tracking": tracking_number,
            "emision": year[-2:],
            "apikey": self.api_key,
            "details": 1,
        }
        # print(params)
        response = requests.get(self.url, params=params)

        if response.status_code == 200:

            data = response.json()
            data["service_name"] = "olva"
            data["num_tracking"] = str(tracking_number) + "-" + year[-2:]
            return olva_response(data)
        else:
            raise Exception(f"Error en la solicitud: {response.status_code}")
