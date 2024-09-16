from Tracker import (
    MarvisurService,
    OlvaService,
    ShalomService,
    CourierRouter,
)

from Tracker.models import marvisur, olva, shalom

from rich import print
from dotenv import load_dotenv, find_dotenv
import os


find_dotenv()
load_dotenv()


olva_api_key = os.environ.get("OLVA_API_KEY")


# # print(olva_api_key)
# # # Ejemplo de uso
if __name__ == "__main__":
    router = CourierRouter(olva_api_key=olva_api_key)

    print(router.route_tracking("v004-0167414"))  # Marvisur

    m1 = router.route_tracking("v004-0167414")  # Marvisur

    print(router.route_tracking("v019-0067424"))  # Marvisur
    print(router.route_tracking("1234556-23"))  # Olva
    print(router.route_tracking("30560173-wndk"))  # Shalom
    print(router.route_tracking("invalid-number"))  # No reconocido
