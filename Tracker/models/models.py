# Uso de la clase
from pydantic import BaseModel
from typing import Optional, Dict, List


class Estado(BaseModel):
    id: Optional[str]
    fecha_evento: str
    state: Optional[str]
    evento: Optional[str]


class TrackingState(BaseModel):
    registro: Estado
    transito: Optional[List[Estado]]
    destino: Optional[Estado]
    entregado: Optional[Estado]
    last_state: Optional[Estado]


class Data(BaseModel):
    remitente: str
    destinatario: str
    origen: str
    destino: str
    tipo_entrega: Optional[str]
    monto_pagar: Optional[float]


class Package(BaseModel):
    unidad_medida: Optional[str]
    cantidad_paquetes: Optional[int]
    peso: Optional[float]
    contenido: Optional[str]


class TrackingResponse(BaseModel):
    service_name: str
    tracking_number: str
    comprobante: Optional[str]
    pkg_info: Optional[List[Package]]
    data: Data
    states: TrackingState
