# Azure Deployment Guide

## Files for Azure App Service Deployment

### 1. requirements.txt
Lists all Python dependencies needed for the app.

### 2. startup.txt (for Linux App Service)
Command to start the application using Gunicorn.

### 3. web.config (for Windows App Service)
Configuration for IIS to run the Python app.

## Deployment Steps

### Option A: Deploy via Azure Portal (Recommended)

1. **Create Azure Web App**
   - Go to Azure Portal
   - Create a new Web App
   - Choose Python 3.9+ runtime
   - Select your region

2. **Configure Application Settings**
   - Go to Configuration > Application settings
   - Add: `SCM_DO_BUILD_DURING_DEPLOYMENT = true`
   - Add: `WEBSITE_RUN_FROM_PACKAGE = 0`

3. **Deploy Code**
   - Use Deployment Center
   - Choose GitHub, Local Git, or ZIP deploy
   - Upload your code

### Option B: Deploy via Azure CLI

```bash
# Login to Azure
az login

# Create resource group
az group create --name myResourceGroup --location eastus

# Create App Service plan
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1 --is-linux

# Create web app
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name your-app-name --runtime "PYTHON:3.9"

# Configure startup command
az webapp config set --resource-group myResourceGroup --name your-app-name --startup-file "startup.txt"

# Deploy code
az webapp up --name your-app-name --resource-group myResourceGroup --runtime PYTHON:3.9
```

## Troubleshooting

### If website doesn't load:

1. **Check Application Logs**
   - Go to Azure Portal > Your App > Monitoring > Log stream
   - Look for error messages

2. **Verify Python version**
   - Ensure Python 3.9+ is selected in Configuration > General settings

3. **Check startup command**
   - For Linux: Should point to `startup.txt` or use:
     `gunicorn --bind=0.0.0.0:8000 src.app:app`

4. **Verify file structure**
   - Ensure all files are uploaded including static folder, templates, and docs

5. **Enable detailed logging**
   - Go to Configuration > General settings
   - Enable Application Logging

6. **Check if port is correct**
   - Azure assigns dynamic port via environment variable
   - Update app.py to use: `port = int(os.environ.get('PORT', 8000))`

## Important Notes

- Make sure the `docs` folder with your resume PDF is included in deployment
- Ensure `static` folder with images and CSS is uploaded
- The app should listen on `0.0.0.0` not `localhost`
- Use environment variables for sensitive data
