
from db.reservas_db import get_reserva, save_reserva, update_reserva
from db.reservas_db import ReservaInDB
from db.user_db import get_user
from models.reservas_models import ReservaOut, ReservaIn, ReservaCancelIn, ReservaCancelOut

from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = ["http://localhost.tiangolo.com",
            "https://localhost.tiangolo.com",
            "http://localhost",
            "http://localhost:8080",
            "http://localhost:8081",
            "https://reservas-hotel-app37.herokuapp.com/",]

api.add_middleware(CORSMiddleware,
                    allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],)

@api.get("/user/reserva/{id_reserva}")
async def get_reservation(id_reserva: int):
    reserva_in_db = get_reserva(id_reserva)
    if reserva_in_db == None:
        raise HTTPException(status_code = 404, detail = "La reserva no existe")
    user_in_db = get_user(reserva_in_db.username)
    reserva_out = ReservaOut(**reserva_in_db.dict(), nombre = user_in_db.nombre)
    return reserva_out

@api.put("/user/reserva/make/")
async def make_reservation(reserva_in: ReservaIn):
    user_in_db = get_user(reserva_in.username)
    if user_in_db == None:
        raise HTTPException(status_code = 404, detail = "El usuario no existe")
    reserva_in_db = ReservaInDB(**reserva_in.dict())
    reserva_in_db = save_reserva(reserva_in_db)
    reserva_out = ReservaOut(**reserva_in_db.dict(), nombre = user_in_db.nombre)
    return reserva_out

@api.put("/user/reserva/cancel/")
async def cancel_reservation(reserva_cancel_in: ReservaCancelIn):
    reserva_in_db = get_reserva(reserva_cancel_in.id_reserva)
    if reserva_in_db == None:
        raise HTTPException(status_code = 404, detail = "La reserva no existe")
    estado = reserva_in_db.estado
    if estado == "cancelada":
        raise HTTPException(status_code = 404, detail = "La reserva ya está cancelada")
    reserva_in_db.estado = "cancelada"
    update_reserva(reserva_in_db)
    reserva_cancel_out = ReservaCancelOut(**reserva_in_db.dict())
    return reserva_cancel_out
