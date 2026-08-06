from fastapi import FastAPI
from dtos import Account 


app = FastAPI()
# now creating the backend point for the creating the acccount
@app.post("/accounts")
def create_account(create_account:Account):
    data = dict(create_account)
    print(data)
    Account.append(data)

    return Account

# # now we are adding in the existing account 
# @app.post("/account/{account_number}/deposit")
# def Money_Deposite(account_number:int):


@app.get("/accounts/{account_number}")
def get_account(account_number: int):

    for account in Account:
        if account["Account_Number"] == account_number:
            return account

    raise HTTPException(
        status_code=404,
        detail="Account not found"
    )


# return{"staus code":"200 ok"}





# # now we are withdrawing the ammount
# @app.post("accounts/{account_number}/withdraw")
# def withdraw_Money(account_number:int):








# now the fourth task which is the get account details

# @app.get("/accounts/{account_number}")
# def show_account(): 
# @app.get("accounts/{account_number}")
# def show_account(account_number:int):
#     for index, acc_number in enumerate@app.post("/accounts/{account_number}/withdraw")
def withdraw_money(account_number: int, withdraw: AmountDTO):

    if withdraw.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Withdrawal amount must be greater than zero"
        )

    for account in Account:

        if account["Account_Number"] == account_number:

            if account["Account_Balance"] < withdraw.amount:
                raise HTTPException(
                    status_code=400,
                    detail="Insufficient balance"
                )

            account["Account_Balance"] -= withdraw.amount
            return account

    raise HTTPException(
        status_code=404,
        detail="Account not found"
    )

