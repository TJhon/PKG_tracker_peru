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


class TrackingService:
    def __init__(self):
        self.url = "https://jtfp1lubog.execute-api.us-east-1.amazonaws.com/produccion/api-marvisur"

    def get_tracking(self, serie, numero):
        payload = {"serie": serie, "numero": numero}
        response = requests.post(self.url, json=payload)
        print(response.json())
        if response.status_code == 200:
            json_data = response.json()
            if isinstance(json_data, list) and len(json_data) > 0:
                return [Tracking.tracking_from_json(item) for item in json_data[0]]
            else:
                return []
        else:
            raise Exception(f"Error en la solicitud: {response.status_code}")


# Uso de la clase
service = TrackingService()
result = service.get_tracking("v001", "12344")
# print(result)
for tracking in result:
    print(f"ID: {tracking.ID}, GUIA: {tracking.GUIA}, FECEVENTO: {tracking.FECEVENTO}")
