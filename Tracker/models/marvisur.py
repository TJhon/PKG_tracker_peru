from .models import *
from .utils import date_marvisur


def marvisur_response(data):
    body = data["body"]

    package_info_list = body[1]
    status_list = body[0]

    # Crear lista de estados (status_objects)
    status_objects = [
        Estado(
            fecha_evento=date_marvisur(status.get("FECEVENTO")),
            state=status.get("COMENTARIO"),
            evento=status.get("EVENTO"),
            id=str(status.get("ID")),
        )
        for status in status_list
    ]

    # Obtener el estado inicial
    initial_status = next(status for status in status_list if status.get("ID") == 0)

    # Crear el objeto de seguimiento (tracking_state) con manejo de excepciones
    try:
        registro = next(status for status in status_objects if status.id == "0")
    except StopIteration:
        registro = None

    try:
        transito = [status for status in status_objects if status.state == "EN RUTA"]
    except StopIteration:
        transito = None

    try:
        destino = next(
            status for status in status_objects if status.state == "EN ALMACÉN"
        )
    except StopIteration:
        destino = None

    try:
        entregado = next(
            status for status in status_objects if status.state == "ENTREGADO"
        )
    except StopIteration:
        entregado = None

    last_state = status_objects[0] if status_objects else None

    tracking_state = TrackingState(
        registro=registro,
        transito=transito,
        destino=destino,
        entregado=entregado,
        last_state=last_state,
    )

    # Crear el objeto de datos (sender_receiver_info)
    sender_receiver_info = Data(
        remitente=initial_status.get("REMITENTE"),
        destinatario=initial_status.get("DESTINATARIO"),
        origen=initial_status.get("DEPORIGEN"),
        destino=initial_status.get("DEPDESTINO"),
        tipo_entrega=initial_status.get("TIPO_GUIA"),
        monto_pagar=initial_status.get("pago"),  # no existe en el JSON pero incluido
    )

    # Crear la lista de paquetes (package_list)
    package_list = [
        Package(
            unidad_medida=package_info.get("UniMedida"),
            cantidad_paquetes=package_info.get("Cantidad"),
            peso=package_info.get("Peso"),
            contenido=package_info.get("Contenido"),
        )
        for package_info in package_info_list
    ]

    # Crear el objeto final de respuesta (tracking_response)
    tracking_response = TrackingResponse(
        service_name=data.get("service_name"),
        tracking_number=data.get("num_tracking"),
        comprobante=data.get("comprobante"),
        pkg_info=package_list,
        data=sender_receiver_info,
        states=tracking_state,
    )

    return tracking_response
