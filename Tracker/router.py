import re
from typing import Union, Dict, Any
from .api.marvisur import MarvisurService
from .api.olva import OlvaService
from .api.shalom import ShalomService


class CourierRouter:
    def __init__(self, olva_api_key: str):
        self.marvisur_service = MarvisurService()
        self.olva_service = OlvaService(api_key=olva_api_key)
        self.shalom_service = ShalomService()

    def route_tracking(self, tracking_number: str) -> Union[Dict[str, Any], str]:
        # Para Marvisur
        marvisur_pattern = r"^v\d{3}[-\s]?(\d+)$"

        # Para Olva (asumiendo que el año siempre está presente)
        olva_pattern = r"^(\d+)[-\s]?(\d{2})$"

        # Para Shalom
        shalom_pattern = r"^(\d{8})[-\s]?([a-zA-Z0-9]{4})$"

        if re.match(marvisur_pattern, tracking_number, re.IGNORECASE):
            match = re.match(marvisur_pattern, tracking_number, re.IGNORECASE)
            serie, numero = (
                match.group(0).split("-")
                if "-" in match.group(0)
                else match.group(0).split()
            )
            return self.marvisur_service.get_tracking(serie, numero)

        elif re.match(olva_pattern, tracking_number):
            match = re.match(olva_pattern, tracking_number)
            numero, anio = match.groups()
            return self.olva_service.get_tracking(int(numero), f"20{anio}")

        elif re.match(shalom_pattern, tracking_number):
            match = re.match(shalom_pattern, tracking_number)
            numero, codigo = match.groups()
            return self.shalom_service.get_tracking(numero, codigo)

        else:
            return "Número de seguimiento no reconocido"
