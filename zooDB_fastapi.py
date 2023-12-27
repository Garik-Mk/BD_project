from fastapi import FastAPI, HTTPException, status
from zoodb import ZooDB
import model

APP = FastAPI()


@APP.post("/create_zoocomplex", tags=["zoocomplex"])
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


@APP.get("/get_zoocomplex/{complex_id}", tags=["zoocomplex"])
async def get_zoocomplex(complex_id: int):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    zoocomplex = ZooDB.session.query(model.ZooComplex).get(complex_id)
    if zoocomplex:
        return zoocomplex
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zoo Complex not found")


@APP.put("/update_zoocomplex/{complex_id}", tags=["zoocomplex"])
async def update_zoocomplex(complex_id: int, complex_update: model.ZooComplex):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    zoocomplex = ZooDB.session.query(model.ZooComplex).get(complex_id)
    if zoocomplex:
        zoocomplex.complex_name = complex_update.complex_name
        ZooDB.session.commit()
        return f"Zoo Complex {complex_id} updated"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zoo Complex not found")


@APP.delete("/delete_zoocomplex/{complex_id}", tags=["zoocomplex"])
async def delete_zoocomplex(complex_id: int):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    
    zoocomplex = ZooDB.session.query(model.ZooComplex).get(complex_id)
    
    if zoocomplex:
        ZooDB.session.delete(zoocomplex)
        ZooDB.session.commit()
        return f"Zoo Complex {complex_id} deleted"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zoo Complex not found")


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


@APP.get("/get_specie/{specie_id}", tags=["specie"])
async def get_specie(specie_id: int):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    specie = ZooDB.session.query(model.Species).get(specie_id)
    if specie:
        return specie
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specie not found")


@APP.put("/update_specie/{specie_id}", tags=["specie"])
async def update_specie(specie_id: int, specie_update: model.Species):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    specie = ZooDB.session.query(model.Species).get(specie_id)
    if specie:
        specie.accommodation_id = specie_update.accommodation_id
        specie.specie_name = specie_update.specie_name
        specie.family = specie_update.family
        specie.habitat = specie_update.habitat
        specie.live_duration = specie_update.live_duration
        ZooDB.session.commit()
        return f"Specie {specie_id} updated"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specie not found")


@APP.delete("/delete_specie/{specie_id}", tags=["specie"])
async def delete_specie(specie_id: int):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    specie = ZooDB.session.query(model.Species).get(specie_id)
    if specie:
        ZooDB.session.delete(specie)
        ZooDB.session.commit()
        return f"Specie {specie_id} deleted"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specie not found")


@APP.post("/create_accommodation", tags=["accommodation"])
async def create_accommodation(
    name: str,
    complex_id: int,
    has_pool: int = None,
    area: float = None
):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    if ZooDB.session.query(model.Accommodations).filter(model.Accommodations.name==name).first() is None:
        new_accommodation = model.Accommodations(
            name=name,
            complex_id=complex_id,
            has_pool=has_pool,
            area=area
        )
        ZooDB.session.add(new_accommodation)
        ZooDB.session.commit()
        return f"{new_accommodation.name} accommodation added"
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Accommodation already exists")


@APP.get("/get_accommodation/{accommodation_id}", tags=["accommodation"])
async def get_accommodation(accommodation_id: int):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    accommodation = ZooDB.session.query(model.Accommodations).get(accommodation_id)
    if accommodation:
        return accommodation
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Accommodation not found")


@APP.put("/update_accommodation/{accommodation_id}", tags=["accommodation"])
async def update_accommodation(accommodation_id: int, accommodation_update: model.Accommodations):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    accommodation = ZooDB.session.query(model.Accommodations).get(accommodation_id)
    if accommodation:
        accommodation.name = accommodation_update.name
        accommodation.complex_id = accommodation_update.complex_id
        accommodation.has_pool = accommodation_update.has_pool
        accommodation.area = accommodation_update.area
        ZooDB.session.commit()
        return f"Accommodation {accommodation_id} updated"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Accommodation not found")


@APP.delete("/delete_accommodation/{accommodation_id}", tags=["accommodation"])
async def delete_accommodation(accommodation_id: int):
    if not ZooDB.is_connected():
        ZooDB.connect_to_DB()
    accommodation = ZooDB.session.query(model.Accommodations).get(accommodation_id)
    if accommodation:
        ZooDB.session.delete(accommodation)
        ZooDB.session.commit()
        return f"Accommodation {accommodation_id} deleted"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Accommodation not found")
