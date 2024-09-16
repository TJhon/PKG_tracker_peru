from .models import *


def shalom_response(data):
    main_data = data["data"]
    states_tracking = data["states"]["data"]

    data_general = Data(
        remitente=main_data.get("remitente").get("nombre"),
        destinatario=main_data.get("destinatario").get("nombre"),
        origen=main_data.get("origen").get("departamento"),
        destino=main_data.get("destino").get("nombre"),
        tipo_entrega=main_data.get("tipo_pago"),
        monto_pagar=main_data.get("monto"),
    )

    package_list = [
        Package(
            peso=main_data.get("peso"),
            cantidad_paquetes=main_data.get("cantidad"),
            unidad_medida=main_data.get("unidad"),
            contenido=main_data.get("contenido"),
        )
    ]

    tracking_state = TrackingState(
        registro=Estado(
            id="0",
            fecha_evento=states_tracking.get("registrado").get("fecha"),
            state=states_tracking.get("registrado").get("name", "Registrado"),
            evento=None,
        ),
        transito=[
            Estado(
                id="1",
                fecha_evento=states_tracking.get("transito").get("fecha"),
                state=states_tracking.get("transito").get("name", "Transito"),
                evento=None,
            )
        ],
        destino=Estado(
            id="2",
            fecha_evento=states_tracking.get("destino").get("fecha"),
            state=states_tracking.get("destino").get("name", "Destino"),
            evento=None,
        ),
        entregado=Estado(
            id="3",
            fecha_evento=states_tracking.get("entregado").get("fecha"),
            state=states_tracking.get("entregado").get("name", "Entregado"),
            evento=None,
        ),
        last_state=Estado(
            id="4",
            fecha_evento=states_tracking.get("registrado").get("fecha"),
            state=states_tracking.get("registrado").get("name", "Registrado"),
            evento=None,
        ),
    )

    tracking_response = TrackingResponse(
        service_name=data.get("service_name"),
        tracking_number=data.get("num_tracking"),
        comprobante=data.get("comprobante"),
        data=data_general,
        pkg_info=package_list,
        states=tracking_state,
    )

    return tracking_response
