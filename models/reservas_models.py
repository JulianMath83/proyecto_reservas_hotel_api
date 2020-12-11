
from datetime import datetime
from pydantic import BaseModel

class ReservaOut(BaseModel):
    id_reserva: int
    nombre: str
    fecha_reserva: str
    destino: str
    hotel: str
    tipo_habitacion: str
    valor: int
    fecha_in: str
    fecha_out: str
    estado: str

class ReservaIn(BaseModel):
    username: str
    destino: str
    hotel: str
    tipo_habitacion: str
    valor: int
    fecha_in: str
    fecha_out: str

class ReservaCancelIn(BaseModel):
    id_reserva: int

class ReservaCancelOut(BaseModel):
    id_reserva: int
    estado: str
