import json
import requests
from datetime import datetime


class Tracking:
    def __init__(
        self,
        ID,
        GUIA,
        FECEVENTO,
        EVENTO,
        COMENTARIO,
        REMITENTE,
        DESTINATARIO,
        DEPORIGEN,
        DEPDESTINO,
        PAGO,
        PRECIO,
    ):
        self.ID = ID
        self.GUIA = GUIA
        self.FECEVENTO = FECEVENTO
        self.EVENTO = EVENTO
        self.COMENTARIO = COMENTARIO
        self.REMITENTE = REMITENTE
        self.DESTINATARIO = DESTINATARIO
        self.DEPORIGEN = DEPORIGEN
        self.DEPDESTINO = DEPDESTINO
        self.PAGO = PAGO
        self.PRECIO = PRECIO

    @staticmethod
    def tracking_from_json(json_data):
        fecevento = datetime.fromisoformat(json_data["FECEVENTO"]).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return Tracking(
            json_data["ID"],
            json_data["GUIA"],
            fecevento,
            json_data["EVENTO"],
            json_data["COMENTARIO"],
            json_data["REMITENTE"],
            json_data["DESTINATARIO"],
            json_data["DEPORIGEN"],
            json_data["DEPDESTINO"],
            json_data["PAGO"],
            json_data["PRECIO"],
        )


class MarvisurService:
    def __init__(self):
        self.url = "https://jtfp1lubog.execute-api.us-east-1.amazonaws.com/produccion/api-marvisur"

    def get_tracking(self, serie: str, numero: str):
        payload = {"serie": serie, "numero": numero}
        response = requests.post(self.url, json=payload)
        # print(response.json())
        if response.status_code == 200:
            data = response.json()
            data["service_name"] = "marvisur"
            data["num_tracking"] = serie + "-" + numero
            return data
        else:
            raise Exception(f"Error en la solicitud: {response.status_code}")
