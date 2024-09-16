import requests
from typing import Dict, Any


class ShalomService:
    BASE_URL = "https://servicesweb.shalomcontrol.com/api/v1/web"

    def __init__(self):
        self.endpoints = {
            "buscar": f"{self.BASE_URL}/rastrea/buscar",
            "estados": f"{self.BASE_URL}/rastrea/estados",
            "comprobante": f"{self.BASE_URL}/rastrea/comprobante",
        }

    def _make_request(
        self, endpoint: str, data: Dict[str, Any], method: str = "post"
    ) -> Dict[str, Any]:
        headers = {"Content-Type": "application/json"}
        response = requests.request(
            method, self.endpoints[endpoint], json=data, headers=headers
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Error en la solicitud a {endpoint}: {response.status_code}"
            )

    def get_tracking(self, numero: str, codigo: str) -> Dict[str, Any]:
        content = self._make_request("buscar", {"numero": numero, "codigo": codigo})

        ose_id = content["data"]["ose_id"]
        states = self._make_request("estados", {"ose_id": ose_id})
        content["states"] = states
        content["service_name"] = "shalom"
        content["num_tracking"] = numero + "-" + codigo

        if states["data"].get("entregado") is not None:
            comprobante = content["data"]["comprobante"]
            pdf_data = self._make_request(
                "comprobante",
                {"serie": comprobante["serie"], "numero": comprobante["numero"]},
            )
            content["comprobante"] = pdf_data.get("data", {}).get("pdf")

        return content
