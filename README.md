# Zoo Database Management System

This project consists of a Python module zoodb.py that provides a simple interface for managing a zoo database using SQLAlchemy. It includes the definition of the database schema in model.py. Additionally, there is a FastAPI application zoodb_fastapi.py that exposes endpoints for creating zoo complexes, accommodations, and species.
Table of Contents

    Installation
    Database Structure
    FastAPI Endpoints
    License

## Installation

Clone the repository:

```
git clone <repository_url>
```
Install the required dependencies:
```
pip install -r requirements.txt
```
Set up your environment variables by creating a .env file with the following keys:
```
POSTGRES_USER=<your_postgres_user>
POSTGRES_PASSWORD=<your_postgres_password>
POSTGRES_HOST=<your_postgres_host>
POSTGRES_DB=<your_postgres_db>
POSTGRES_PORT=<your_postgres_port>
```

## Database Structure

The database schema is defined in model.py and consists of three tables:

    zoocomplex: Represents zoo complexes with a unique identifier and a name.
    accommodations: Represents accommodations within a zoo complex, including a unique identifier, name, complex ID, pool availability, and area.
    species: Represents animal species within an accommodation, including a unique identifier, accommodation ID, species name, family, habitat, and live duration.

## FastAPI Endpoints

The FastAPI application in zoodb_fastapi.py exposes the following endpoints:

**POST** /create_zoocomplex: Creates a new zoo complex.

    {
    "complex_name": "Zoo Complex A"
    }

**GET** /get_zoocomplex/{complex_id}: Retrieves details of a specific zoo complex.

    {
    "complex_name": "Zoo Complex A"
    }

**PUT** /update_zoocomplex/{complex_id}: Updates the details of a specific zoo complex.

    {
    "complex_name": "Updated Zoo Complex A"
    }

**DELETE** /delete_zoocomplex/{complex_id}: Deletes a specific zoo complex.

---

**POST** /create_accommodation: Creates a new accommodation within a zoo complex.

    {
    "name": "Accommodation A",
    "complex_id": 1,
    "has_pool": 1,
    "area": 100.5
    }

**GET** /get_accommodation/{accommodation_id}: Retrieves details of a specific accommodation.

    {
      "name": "Accommodation A",
      "complex_id": 1,
      "has_pool": 1,
      "area": 100.5
    }

**PUT** /update_accommodation/{accommodation_id}: Updates the details of a specific accommodation.

    {
      "name": "Updated Accommodation A",
      "complex_id": 1,
      "has_pool": 0,
      "area": 120.0
    }

**DELETE** /delete_accommodation/{accommodation_id}: Deletes a specific accommodation.

---

**POST** /create_specie: Creates a new animal species within an accommodation.

    {
      "accommodation_id": 1,
      "specie_name": "Lion",
      "family": "Felidae",
      "habitat": "Grasslands",
      "live_duration": 10
    }

**GET** /get_specie/{specie_id}: Retrieves details of a specific animal species.

    {
      "accommodation_id": 1,
      "specie_name": "Lion",
      "family": "Felidae",
      "habitat": "Grasslands",
      "live_duration": 10
    }

**PUT** /update_specie/{specie_id}: Updates the details of a specific animal species.

    {
      "accommodation_id": 1,
      "specie_name": "Updated Lion",
      "family": "Felidae",
      "habitat": "Savanna",
      "live_duration": 12
    }

**DELETE** /delete_specie/{specie_id}: Deletes a specific animal species.

---

Ensure that the ZooDB instance is connected before making requests to these endpoints. The connection is established automatically upon instantiation of ZooDB.

## License

This project is licensed under the MIT License.