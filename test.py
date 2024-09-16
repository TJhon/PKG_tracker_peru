from Tracker import (
    MarvisurService,
    OlvaService,
    ShalomService,
    CourierRouter,
)
from rich import print
from dotenv import load_dotenv, find_dotenv
import os


find_dotenv()
load_dotenv()


olva_api_key = os.environ.get("OLVA_API_KEY")


# print(olva_api_key)
# # Ejemplo de uso
if __name__ == "__main__":
    router = CourierRouter(olva_api_key=olva_api_key)

    # Pruebas
    # print(router.route_tracking("v004-0167414"))  # Marvisur

    m1 = router.route_tracking("v004-0156568")  # Marvisur
    # convertir_marvisur(m1)
    print(m1)
    # print(router.route_tracking("v019-0067424"))  # Marvisur
    # print(router.route_tracking("1234556-23"))  # Olva
    # print(router.route_tracking("30560173-wndk"))  # Shalom
    # print(router.route_tracking("invalid-number"))  # No reconocido
