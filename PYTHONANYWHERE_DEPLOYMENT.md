# PythonAnywhere ASGI Deployment Guide

This guide documents the current deployment flow for the project on PythonAnywhere using the experimental `pa website create` command.

## Prerequisites

- The project has been pushed to GitHub.
- You have a PythonAnywhere account.
- Your virtual environment exists and matches the Python version used by the website.

## Deployment Command

Use the following command, replacing `YOURUSERNAME` with your PythonAnywhere username:

```bash
pa website create -d polowu.pythonanywhere.com -c '/home/YOURUSERNAME/.virtualenvs/interview-tracker/bin/uvicorn --app-dir /home/YOURUSERNAME/interview-tracker-api --uds ${DOMAIN_SOCKET} app.main:app'
```

## Steps

1. Open a Bash console on PythonAnywhere.
2. Make sure the project dependencies are installed:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the deployment command:

   ```bash
   pa website create -d polowu.pythonanywhere.com -c '/home/YOURUSERNAME/.virtualenvs/interview-tracker/bin/uvicorn --app-dir /home/YOURUSERNAME/interview-tracker-api --uds ${DOMAIN_SOCKET} app.main:app'
   ```

4. If the website already exists, reload it:

   ```bash
   pa website reload polowu.pythonanywhere.com
   ```

5. Open the API docs to verify the deployment:

   ```text
   https://polowu.pythonanywhere.com/docs
   ```

## Checks

- Confirm that `YOURUSERNAME` is replaced correctly.
- Confirm that the virtual environment path exists.
- Confirm that `app.main:app` matches the FastAPI application object in the project.
- Reload the site after every code change.

## Notes

- The old WSGI manual configuration is no longer used.
- The old `a2wsgi` workaround is no longer part of the deployment flow.
- The older general deployment guide has been removed to avoid confusion.
