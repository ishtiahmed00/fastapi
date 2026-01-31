from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def home():
    return {"name" : "Ishti Ahmed"}

@app.get("/info/{name}")
def info(name):
    return {"name" : name}

@app.get("/contact/{contact}")
def contact(contact):
    return {"contact" : contact}

@app.get("/address/{address}")
def address(address):
    return {"address" : address}        

@app.get("/data/{name}/{contact}")
def data(name : str,contact : int):
    return {
            "Name" : name,
            "Contact" : contact
            }

@app.get("/information/{name}")
def Data(name : str, age : Optional[int] = None):
    return {"name" : name,"age" : age}

@app.get("/bike/{name}")
def bike(name : str):
    return {"Bike Name" : name}

@app.get("/bike/{name}/{numPlate}")
def bikeInfo(name : str, numPlate : str):
    return {
            "Bike Name" : name,
            "Num Plate" : numPlate
            }

@app.get("/bike/{name}")
def bikeInformation(name : str, numPlate : Optional[str] = None):
    return {
            "Bike Name" : name,
            "Num Plate" : numPlate
            }

@app.get("/car/{name}")
def car(name : str):
    return {"Car Name" : name}

@app.get("/car/{name}/{numPlate}")
def carInfo(name : str, numPlate : str):
    return {
            "Car Name" : name,
            "Num Plate" : numPlate
            }

@app.get("/car/{name}")
def carInformation(name : str, numPlate : Optional[str] = None):
    return {
            "Car Name" : name,
            "Num Plate" : numPlate
            }

@app.get("/{animal_name}")
def animal(animal_name : str, speak : Optional[str] = None):
    return{
        "Animal_name" : animal_name,
        "Speaking" : speak 
    }

@app.get("/student")
def student_informaiton(id : Optional[int] = None, name : Optional[str] = None, age : Optional[int] = None, dep : Optional[str] = None):
    return{
        "ID" : id,
        "Name" : name,
        "Age" : age,
        "Department" : dep
    }

@app.get("/teacher")
def student_info(id : Optional[int] = None, name : Optional[str] = None, age : Optional[int] = None, dep : Optional[str] = None):
    return{
        "ID" : id,
        "Teachers Name" : name,
        "Age" : age,
        "Department" : dep
    }

@app.get("/mobile/{name}")
def mobile(name : str):
    return{
        "Mobile Name":name
    }

@app.get("/mobile/{name}/{model}")
def mobile_with_model(name : str, model: str):
    return{
        "Mobile Name":name,
        "Model" : model
    }

@app.get("/mobile/{name}")
def mobile_model(name : str, model : Optional[str]=None):
    return{
        "Mobile Name":name,
        "Model": model
    }

@app.get("/laptop/{name}")
def laptop(name : str):
    return{
        "Laptop Name":name
    }

@app.get("/laptop/{name}/{model}")
def laptop_with_model(name : str, model: str):
    return{
        "Laptop Name":name,
        "Model" : model
    }

@app.get("/laptop/{name}")
def laptop_model(name : str, model : Optional[str]=None):
    return{
        "Laptop Name":name,
        "Model": model
    }

@app.get("/subject/{name}")
def subject(name : str):
    return{
        "subject Name":name
    }

@app.get("/subject/{company}/{name}")
def subject_company(company : str, subject: str):
    return{
        "Company" : company,
        "Subject Name": subject,
    }

@app.get("/subject/{name}")
def subject_with_company(company : str, subject : Optional[str]=None):
    return{
        "Company" : company,
        "Subject Name": subject,
    }

@app.get("/election/{vote}")
def election(vote : str):
    return{
        "You are Voting":vote
    }

@app.get("/election/{vote}/{nid}")
def election_with_nid(vote : str, nid : int):    
    return{
        "You are Voting " : vote,
        "Your NID number " : nid 
    }

@app.get("/election/{vote}")
def election_vote(vote : str, nid: Optional[int]=None):    
    return{
        "You are Voting" : vote,
        "Your NID number " : nid 
    }

@app.get("/institute/{name}")
def institute(name : str):
    return{"institute name" : name}