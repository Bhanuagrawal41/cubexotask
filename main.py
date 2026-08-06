from fastapi import FastAPI, HTTPException
from dtos import Account 



app = FastAPI()
accounts = []
# now creating the backend point for the creating the acccount
@app.post("/accounts")
def create_account(create_account: Account):
    data = create_account.model_dump()
    for account in accounts:
        if account["Account_Number"] == data["Account_Number"]:
            raise HTTPException(
                status_code=400,
                detail="Account already exists"
            )
    accounts.append(data)
    return data



#now creating backend point to getting the account details
@app.get("/accounts/{account_number}")
def get_account(account_number: int):
    for account in accounts:
        if account["Account_Number"] == account_number:
            return account

    raise HTTPException(
        status_code=404,
        detail="Account not found"
    )







# @app.post("accounts/{account_number}/withdraw")
# def withdraw_money(account_number: int, withdraw: AmountDTO):

#     if withdraw.amount <= 0:
#         raise HTTPException(
#             status_code=400,
#             detail="Withdrawal amount must be greater than zero"
#         )

#     for account in Account:

#         if account["Account_Number"] == account_number:

#             if account["Account_Balance"] < withdraw.amount:
#                 raise HTTPException(
#                     status_code=400,
#                     detail="Insufficient balance"
#                 )

#           





