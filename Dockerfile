FROM python:3.12.9

WORKDIR /app

COPY . /app

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install poetry

RUN poetry install --no-root

CMD ["python3 -m uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
