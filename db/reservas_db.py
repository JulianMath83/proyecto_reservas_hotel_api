
from typing import Dict
from pydantic import BaseModel
from datetime import datetime

class ReservaInDB (BaseModel):
    id_reserva: int = 0
    username: str
    fecha_reserva: str = datetime.now().strftime('%Y-%m-%d')
    destino: str
    hotel: str
    tipo_habitacion: str
    valor: int
    fecha_in: str
    fecha_out: str
    estado: str = "activa"

database_reservas : Dict[int, ReservaInDB]
database_reservas = {
    1:  ReservaInDB(**{"id_reserva":"1",
                       "username":"roger23",
                       "fecha_reserva":"2020-10-30",
                       "destino":"Cartagena",
                       "hotel":"Puerta del Sol",
                       "tipo_habitacion":"Doble",
                       "valor":300000,
                       "fecha_in":"15-dic-2020",
                       "fecha_out":"29-dic-2020",
                       "estado":"CANCELADA"
                       }),
    2:  ReservaInDB(**{"id_reserva":"2",
                       "username":"karen45",
                       "fecha_reserva":"2020-7-30",
                       "destino":"Medellin",
                       "hotel":"Ave María",
                       "tipo_habitacion":"Queen",
                       "valor":800000,
                       "fecha_in":"05-ene-2021",
                       "fecha_out":"10-ene-2021",
                       "estado":"ACTIVA"
                       }),
    3:  ReservaInDB(**{"id_reserva":"3",
                       "username":"juan88",
                       "fecha_reserva":"2020-1-24",
                       "destino":"Santa Marta",
                       "hotel":"Pescadito",
                       "tipo_habitacion":"King",
                       "valor":650000,
                       "fecha_in":"03-mar-2021",
                       "fecha_out":"04-mar-2021",
                       "estado":"ACTIVA"
                       }),
}

def get_reserva(reserva_in_db: int):
    if reserva_in_db in database_reservas.keys():
        return database_reservas[reserva_in_db]
    else:
        return None

def update_reserva(user_in_db: ReservaInDB):
    database_reservas[user_in_db.id_reserva] = user_in_db
    return user_in_db

generator = {"id":len(database_reservas)}

def save_reserva(reserva_in_db: ReservaInDB):
    generator["id"] += 1
    reserva_in_db.id_reserva = generator["id"]
    database_reservas[generator["id"]] = reserva_in_db
    return reserva_in_db
