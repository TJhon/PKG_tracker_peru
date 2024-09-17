from .models import *


def olva_response(data):
    info = data["data"]
    # print(info)
    # info['']
    general = info["general"]
    details = info["details"]

    package_list = [
        Package(
            peso=general.get("peso"),
            cantidad_paquetes=int(general.get("cantidad")),
            unidad_medida="kg",
            contenido=general.get("contenido"),
        )
    ]

    data_general = Data(
        remitente=general.get("remitente"),
        destinatario=general.get("consignado"),
        origen=general["origen"],
        destino=general["destino"],
        tipo_entrega=general.get("type"),
        monto_pagar=general.get("pago"),
    )

    status_obj = [
        Estado(
            fecha_evento=state.get("fecha_creacion"),
            state=state.get("estado_tracking"),
            evento=state.get("obs"),
            id=state.get("id_rpt_envio_ruta"),
        )
        for state in details
    ]

    len_status = len(status_obj)

    try:
        transito = [
            status
            for status in status_obj
            if status.state not in ["ENTREGADO", "REGISTRADO", "RECEPCION DESPACHO"]
        ]
    except:
        transito = None
    try:
        destino = next(
            status for status in status_obj if status.state == "RECEPCION DESPACHO"
        )
    except:
        destino = None
    try:
        entregado = next(status for status in status_obj if status.state == "ENTREGADO")
    except:
        entregado = None

    tracking_state = TrackingState(
        registro=status_obj[len_status - 1],
        transito=transito,
        destino=destino,
        entregado=entregado,
        last_state=status_obj[0],
    )

    tracking_response = TrackingResponse(
        service_name=data.get("service_name"),
        tracking_number=data.get("num_tracking"),
        comprobante=data.get("comprobante"),
        pkg_info=package_list,
        data=data_general,
        states=tracking_state,
    )
    return tracking_response
