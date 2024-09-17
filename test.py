from Tracker import CourierRouter

from rich import print
from dotenv import load_dotenv, find_dotenv
import os


find_dotenv()
load_dotenv()


olva_api_key = os.environ.get("OLVA_API_KEY")


if __name__ == "__main__":
    router = CourierRouter(olva_api_key=olva_api_key)

    print(router.route_tracking("v004-167414"))  # Marvisur


    print(router.route_tracking("v019-0067424"))  # Marvisur
    print(router.route_tracking("1234556-23"))  # Olva
    print(router.route_tracking("30560173-wndk"))  # Shalom
    # Para los otros caso no existe
    print(router.route_tracking("invalid-number"))  # No reconocido
