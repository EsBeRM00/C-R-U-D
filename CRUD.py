#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir pasajeros
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#uvicorn CRUD:app --reload
#{"id":"25", "Name":"Torborg Danira", "Pclass":"3", "Survived":"0", "Sex":"female", "Age":"8", "SibSp":"3", "Parch":"1"}
#Definimos nuestra entidad: Passenger

class Passenger(BaseModel):
    id: int
    Name: str
    Pclass: int
    Survived: int
    Sex: str
    Age: int
    SibSp: int
    Parch: int

#Creamos un objeto en forma de lista con diferentes pasajeros (Esto sería una base de datos)  
passengers_list= []


#***Get
@app.get("/passengersclass/")
async def passengersclass():
    return (passengers_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/passengersclass/


#***Post
@app.post("/passengersclass/")
async def passengersclass(passenger:Passenger):

    found=False     #Usamos bandera found para verificar si hemos encontrado el pasajero 

    for index, saved_passenger in enumerate(passengers_list):
        if saved_passenger.id == passenger.id:  #Si el Id del passenger guardado es igual al Id del passenger nuevo
            return {"error":"el pasajero ya existe"}
    else:
        passengers_list.append(passenger)
        return passenger

    #http://127.0.0.1:8000/passengersclass/
    
#***Put
@app.put("/passengersclass/")
async def passengersclass(passenger:Passenger):

    found=False     #Usamos bandera found para verificar si hemos encontrado el pasajero 

    for index, saved_passenger in enumerate(passengers_list):
        if saved_passenger.id == passenger.id: #Si el Id del pasajero guardado es igual al Id del pasajero nuevo
            passengers_list[index] = passenger
            found=True
    if not found:
            return {"error":"No se ha actualizado el pasajero"}
    else:
        return passenger, {"respuesta": "El pasajero se ha actualizado"}
    
#***Delete
@app.delete("/passengersclass/")
async def passengersclass(passenger: Passenger):
    found = False

    for index, saved_passenger in enumerate(passengers_list):
        if saved_passenger.id == passenger.id:
            del passengers_list[index] #Se utiliza la palabra clave -del- para eliminar el elemento en el indice especificado de la lista passengers_list
            found = True
            break #Salir inmediatamente del bucle -for- cuando se cumple la condicion, en este caso cuando encuentra un pasajero que coincide con el id proporcionado en la lista

    if not found:
        return {"error": "No se encontró el pasajero"}

    return {"mensaje": "Pasajero eliminado correctamente"}