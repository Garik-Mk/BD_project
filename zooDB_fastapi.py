from fastapi import FastAPI, HTTPException, status
from zoodb import ZooDB
import model

APP = FastAPI()


@APP.post("/create_zoocomplex")
async def create_zoocomplex(
    complex_name: str
):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    if ZooDB.session.query(model.ZooComplex).filter(model.ZooComplex.complex_name==complex_name).first() is None:
        new_complex = model.ZooComplex(
            complex_name=complex_name, 
        )
        ZooDB.session.add(new_complex)
        ZooDB.session.commit()
        return f"{new_complex.complex_name} complex added"
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Complex already exists")


@APP.post("/create_specie", tags=["specie"])
async def create_specie(
    accommodation_id: int,
    specie_name: str = None,
    family: str = None,
    habitat: str = None,
    live_duration: int = None
):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    if ZooDB.session.query(model.Species).filter(model.Species.specie_name==specie_name).first() is None:
        new_specie = model.Species(
            accommodation_id=accommodation_id, 
            specie_name=specie_name, 
            family=family,
            habitat=habitat,
            live_duration=live_duration
        )
        ZooDB.session.add(new_specie)
        ZooDB.session.commit()
        return f"{new_specie.specie_name} specie added"
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specie already exists")

