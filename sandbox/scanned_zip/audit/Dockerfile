FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN pip install notion-client google-cloud-secret-manager cryptography streamlit

CMD ["streamlit", "run", "main_app.py", "--server.port=8501", "--server.address=0.0.0.0"]