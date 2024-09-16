from datetime import datetime
import pytz

# Formato original de fecha en UTC
fecha_utc = "2024-08-09T17:09:21.000Z"


def date_marvisur(fecha_utc):
    # Convertir la cadena a un objeto datetime
    fecha_dt = datetime.strptime(fecha_utc, "%Y-%m-%dT%H:%M:%S.%fZ")

    # Definir la zona horaria UTC y GMT-5
    zona_utc = pytz.utc
    zona_gmt_menos5 = pytz.timezone("Etc/GMT+5")

    # Asignar la zona horaria UTC al objeto datetime
    fecha_dt_utc = zona_utc.localize(fecha_dt)

    # Convertir la hora de UTC a la zona horaria GMT-5
    fecha_dt_gmt_menos5 = fecha_dt_utc.astimezone(zona_gmt_menos5)

    # Formatear la fecha al formato deseado
    fecha_formateada = fecha_dt_gmt_menos5.strftime("%d-%m-%Y %H:%M")
    return fecha_formateada
