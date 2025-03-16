FROM python:3.12.9

WORKDIR /app

COPY requirements.txt /app
COPY src /app

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 7860

CMD ["python", "-m", "uvicorn", "src.app.app:app", "--host", "0.0.0.0", "--port", "7860"]
