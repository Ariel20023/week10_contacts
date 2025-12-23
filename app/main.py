from fastapi import FastAPI, HTTPException
from data_interactor import get_all_contacts , create_contact , update_contact ,delete_contact
from pydantic import BaseModel


app = FastAPI()


@app.get("/contacts")
def get_contacts():
    return get_all_contacts()



class NewContacts(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


@app.post("/contacts")
def create_contact_route(contact:NewContacts):
    new_id = create_contact(
        contact.first_name,
        contact.last_name,
        contact.phone_number
    )
    return {"message": "Contact created successfully", "id": new_id}


@app.put("/contacts/{contact_id}")
def update_contact_route(contact_id: int, contact: NewContacts):
    updated = update_contact(
        contact_id,
        contact.first_name,
        contact.last_name,
        contact.phone_number
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact updated successfully"}



@app.delete("/contacts/{contact_id}")
def delete_contact_route(contact_id: int):
    deleted = delete_contact(contact_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}





