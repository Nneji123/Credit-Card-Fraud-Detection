# Credit Card Fraud Detection App built with Streamlit, FastAPI and Docker

[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white)](http://www.pytorch.org/news.html)
[![Framework](https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white)](https://lung-cancer-api.herokuapp.com/docs)
[![Framework](https://img.shields.io/badge/Streamlit-red.svg?style=flat&logo=streamlit&logoColor=white)](https://share.streamlit.io/nneji123/lung-cancer-prediction/main)
![hosted](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)
![build](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat)
![reposize](https://img.shields.io/github/repo-size/Nneji123/Credit-Card-Fraud-Detection)

An end-to-end Machine Learning Project carried out by Group 3 Zummit Africa AI/ML Team to detect fraudulent credit card transactions. Built with FastAPI, Streamlit and Docker.

**Contributors**
- 
- 
-
-
-

## Problem Statement
Credit card fraud is an inclusive term for fraud committed using a payment card, such as a credit card or debit card. The purpose may be to obtain goods or services or to make payment to another account, which is controlled by a criminal.
 
**This Streamlit App utilizes a Machine Learning model served as an API with FastAPI framework in order to detect fraudulent credit card transactions  based on the following criteria: hours, type of transaction, amount, balance before and after transaction etc.**

The machine learning model used for this web application was deployed as an API using the FastAPI framework and then accessed through a frontend interface with Streamlit.

The App can be viewed [through this link](https://share.streamlit.io/nneji123/credit-card-fraud-detection/main)


The API and its documentation can be viewed [here](https://credit-fraud-ml-api.herokuapp.com/docs) or [here.](https://credit-fraud-ml-api.herokuapp.com/redoc)

## Data Preparation

[Paper Review Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

[Model Deployment Dataset](https://www.kaggle.com/datasets/ealaxi/paysim1v)

### Modelling
In this project different classification algorithms namely:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- GradientBoostClassifier
- SupportVectorClassifier


The final model used for the API was the **Random Forest Classifier** model which had an accuracy score of 0.99.


## Preview

### API Demo
![fastapi](https://user-images.githubusercontent.com/101701760/173524600-961b66fc-da9f-4714-8240-52054e85d0b4.gif)

### Streamlit App Demo

![streamlit](https://user-images.githubusercontent.com/101701760/173524653-7706e13f-d3c6-46cc-abb3-ac9f79316e4b.gif)


## How to run API and Streamlit App on Google Colab:
<details> 
  <summary><b>💻 Running the API on Google Colab</b></summary>

To run a demo or carry out testing with the API it's best to do that with Google Colab. To run/test the API on Google Colab do the following:
1. Clone the repository to your Google Colab Instance.
```
!git clone  https://github.com/Nneji123/Credit-Card-Fraud-Detection.git
```
2. Install the requirements by running the following codes:
```
%%writefile requirements.txt
colabcode
fastapi
uvicorn
pyngrok
```

```
!pip install -r requirements.txt
```
3. Change the working directory:
```
!cd /content/Credit-Card-Fraud-Detection
```

4. Install Ngrok to your Google Colab Instance:
```
!wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
!tar -xvzf ngrok-v3-stable-linux-amd64.tgz
!ngrok authtoken your_token
```
Replace "your_token" with your token which is available on [Ngrok](https://dashboard.ngrok.com/get-started/your-authtoken)

5. Copy the contents of the **app.py** file to an empty cell and then run the cell.
6. Instantiate ColabCode and run the FastAPI app by running the following code in a new cell:
```
from colabcode import ColabCode
cc = ColabCode(port=18000, code=False)
cc.run_app(app=app)
```
You should now be able to view the API by clicking on the generated link.

</details>

<details> 
  <summary><b>💻 Running the Streamlit App on Google Colab</b></summary>

The Streamlit App can also be viewed using Google Colab by doing the following:
1. Copy the contents of "streamlit_app.py" to an empty cell and at the top of cell write the following code and run the cell.
```
%%writefile streamlit_app.py
contents
```

2. Install the requirements by running the following codes in different cells:
```
%%writefile requirements.txt
numpy==1.21.6
requests==2.23.0
streamlit==1.10.0
pyngrok
```

```
!pip install -r requirements.txt
```
4. Run the following code in your instance:
```
from pyngrok import ngrok 
public_url = ngrok.connect(port='8501')
public_url
```
5. You can then view the streamlit app on your Google Colab instance by running:
```
!streamlit run /content/streamlit_app.py & npx localtunnel --port 8501
```
 
</details>

## Running on Local Machine :computer:

Since we have multiple containers communcating with each other, A bridge network was created called AIservice. For testing, a **docker-compose.yml** file has been included so as to run both the API and Streamlit app simultaneously as docker containers. To run the API and the Streamlit app on your local machine do the following:
1. Clone the repository to your local machine
2. Install docker and docker-compose if you haven't
3. Open a bash/cmd in the directory and run:
```
docker network create AIservice
```
4. Then run this command
```docker
docker-compose up -d --build
```
5. After the above steps have been carried out you can now view the documentation of the API and also the Streamlit app.

To visit the FastAPI documentation go to http://localhost:8000 with a web browser.

To visit the Streamlit UI, visit http://localhost:8501.

Logs can be inspected via:
```
docker-compose logs
```
The **docker-compose** method can also be used to deploy the API and Streamlit app on Heroku(using Dockhero which is not free) or using cloud services such as Microsoft Azure, Amazon Web Services or Google Cloud Platform.

## Deployment
The API can be deployed using the dockerfile on heroku or by.

<details> 
  <summary><b>💻 Deploying the API</b></summary>
Assuming you have git and heroku cli installed just carry out the following steps:

1. Clone the repository

```
git clone https://github.com/Nneji123/Credit-Card-Fraud-Detection.git
```

2. Change the working directory

```
cd Credit-Card-Fraud-Detection
```

3. Create the heroku app

``` 
heroku create your-app-name 
```

Replace **your-app-name** with the name of your choosing.

4. Set the heroku cli git remote to that app

```
heroku git:remote your-app-name
```

5. Set the heroku stack setting to container
 
```
heroku stack:set container
```

6. Push to heroku
```
git push heroku main
```
</details>

<details> 
  <summary><b>💻 Deploying the Streamlit App to Streamlit Cloud</b></summary>
 
The Streamlit App was deployed using the streamlit cloud and accesses the API deployed on Heroku. To deploy the app using streamlit cloud share do the following:
1. Fork this repository to your Github account.
2. Create a Streamlit Account and then navigate to https://streamlit.io/cloud
3. Create a new app and then choose the repository you cloned and the **"streamlit_app.py"** and then click deploy.

After the app has been built on the cloud you should then be able to view your app right away!
</details>
