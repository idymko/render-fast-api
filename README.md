# render-fast-api
CD: deploy fast API on render cload platform

## Create Virtual Environment 

Steps:
* `conda create --name fast-api`
* `conda activate fast-api`
* `conda install pip`
* `pip install -r requirements.txt`

## Execution

To run our app, we will use uvicorn in our shell: 
`uvicorn main:app --reload`
* Name of the function: `main`
* Name of the app in that function: `app`
* The `--reload` allows you to make changes to your code and have them instantly 
deployed without restarting uvicorn.

By default, our app will be available locally at http://127.0.0.1:8000.