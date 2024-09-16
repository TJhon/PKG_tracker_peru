# Uso de la clase
from pydantic import BaseModel
from typing import Optional, Dict, List


class TrackingResponse(BaseModel):
    service_name: str
    comprobante: Optional[str]
    data: Dict[str, str]
    states: Dict[str, Dict[str, str]]


class Estado(BaseModel):
    fecha_evento: str
    comentarios: Optional[str]


class TrackingState(BaseModel):
    registro: Estado
    transito: Estado
    destino: Estado
    entregado: Estado


class Data(BaseModel):
    remitente: str
    destinatario: str
    origen: str
    destino: str
    ultimo_estado: str
    unidad_medida: Optional[str]
    cantidad_paquetes: Optional[int]
    peso: Optional[float]
    monto_pagar: Optional[float]
    contenido: Optional[str]
