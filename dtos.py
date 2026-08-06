from pydantic import BaseModel

class Account(BaseModel):
            Account_Number : int
            Account_Holder_Name : str
            Account_Type : str
            Account_Balance : float

# class AmountDTO(BaseModel):
#     amount: float