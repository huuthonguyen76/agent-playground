# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]

FROM python:3.12.9

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

COPY --chown=user  . /app

RUN pip install poetry
RUN poetry install --no-root

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]

