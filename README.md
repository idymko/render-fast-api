## Deploy FastAPI on the Render Cloud Server
CD: deploy fast API on render cload platform

## Create Virtual Environment - Local 

* `conda create --name render-fast-api`
* `conda activate render-fast-api`
* `conda install pip`
* `pip install -r requirements.txt`

## Perform Local Testing
* Run `pytest` 

## Cloud API Testing with Render 

In the earlier CI/CD lesson, you learned how to set up a Render.com account and deploy a Web Service from the console. Now, we will deploy our APIs to the Render cloud platform.

### Requirements
* If you have not done so, please create a new Render account(opens in a new tab) and connect it to your GitHub or GitLab account.
* Upload your FastAPI app to GitHub or GitLab repo and specify the required libraries in the `requirements.txt` file.
* GitHub: https://github.com/idymko/render-fast-api

### Deploy a Web Service from Render Console
* After you log in to your account, click New Web Service. You will be prompted to connect your project's GitHub or Gitlab repo and branch to the Web Service.
* Click "New Web Service" to connect and deploy your FastAPI app on Render cloud platform

### Configure Build and Start Command
* After you connect your GitLab and GitHub repo to the Web Service, you can configure the Build Command and * Start Command. Render will run these commands for deployment.
* Build Command: `pip install -r requirements`
* Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`


### Check API Deployment on the Website
* After Render Web Service completes the build and start commands successfully, your API is deployed. 
* You can check the live website by clicking the URL link provided in the Web Service console. E.g.: https://render-fast-api-787n.onrender.com/docs 

### Check your FastAPI app live on the website
* After your complete the project, please make sure to suspend or delete the web service to avoid any charges.