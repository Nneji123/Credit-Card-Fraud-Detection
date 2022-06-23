import streamlit as st
import json
import requests as re

st.title("Credit Card Fraud Detection Web App")

st.image("image.png")

st.write("""
## About
Credit card fraud is a form of identity theft that involves an unauthorized taking of another's credit card information for the purpose of charging purchases to the account or removing funds from it.

**This Streamlit App utilizes a Machine Learning model served as an API in order to detect fraudulent credit card transactions based on the following criteria: hours, type of transaction, amount, balance before and after transaction etc.** 

The API was built with FastAPI and can be found [here.](https://credit-fraud-ml-api.herokuapp.com/)

The notebook, model and documentation(Dockerfiles, FastAPI script, Streamlit App script) are available on [GitHub.](https://github.com/Nneji123/Credit-Card-Fraud-Detection)        

**Made by Group 3 Zummit Africa AI/ML Team**

**Contributors:** 
- **Hilary Ifezue(Group Lead)**
- **Nneji Ifeanyi**
- **Somtochukwu Ogechi**
- **ThankGod Omieje**
- **Kachukwu Okoh**
""")


st.sidebar.header('Input Features of The Transaction')

sender_name = st.sidebar.text_input("""Input Sender ID""")
receiver_name = st.sidebar.text_input("""Input Receiver ID""")
step = st.sidebar.slider("""Number of Hours it took the Transaction to complete: """)
types = st.sidebar.subheader(f"""
                 Enter Type of Transfer Made:\n\n\n\n
                 0 for 'Cash In' Transaction\n 
                 1 for 'Cash Out' Transaction\n 
                 2 for 'Debit' Transaction\n
                 3 for 'Payment' Transaction\n  
                 4 for 'Transfer' Transaction\n""")
types = st.sidebar.selectbox("",(0,1,2,3,4))
x = ''
if types == 0:
    x = 'Cash in'
if types == 1:
    x = 'Cash Out'
if types == 2:
    x = 'Debit'
if types == 3:
    x = 'Payment'
if types == 4:
    x =  'Transfer'
    
amount = st.sidebar.number_input("Amount in $",min_value=0, max_value=110000)
oldbalanceorg = st.sidebar.number_input("""Sender Balance Before Transaction was made""",min_value=0, max_value=110000)
newbalanceorg= st.sidebar.number_input("""Sender Balance After Transaction was made""",min_value=0, max_value=110000)
oldbalancedest= st.sidebar.number_input("""Recipient Balance Before Transaction was made""",min_value=0, max_value=110000)
newbalancedest= st.sidebar.number_input("""Recipient Balance After Transaction was made""",min_value=0, max_value=110000)
isflaggedfraud = 0
if amount >= 200000:
  isflaggedfraud = 1
else:
  isflaggedfraud = 0


if st.button("Detection Result"):
    values = {
    "step": step,
    "types": types,
    "amount": amount,
    "oldbalanceorig": oldbalanceorg,
    "newbalanceorig": newbalanceorg,
    "oldbalancedest": oldbalancedest,
    "newbalancedest": newbalancedest,
    "isflaggedfraud": isflaggedfraud
    }


    st.write(f"""### These are the transaction details:\n
    Sender ID: {sender_name}
    Receiver ID: {receiver_name}
    1. Number of Hours it took to complete: {step}\n
    2. Type of Transaction: {x}\n
    3. Amount Sent: {amount}$\n
    4. Sender Balance Before Transaction: {oldbalanceorg}$\n
    5. Sender Balance After Transaction: {newbalanceorg}$\n
    6. Recepient Balance Before Transaction: {oldbalancedest}$\n
    7. Recepient Balance After Transaction: {newbalancedest}$\n
    8. System Flag Fraud Status(Transaction amount greater than $200000): {isflaggedfraud}
                """)

    res = re.post(f"https://credit-fraud-ml-api.herokuapp.com/predict",json=values)
    json_str = json.dumps(res.json())
    resp = json.loads(json_str)
    
    if sender_name=='' or receiver_name == '':
        st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
    else:
        st.write(f"""### The '{x}' transaction that took place between {sender_name} and {receiver_name} is {resp[0]}.""")
