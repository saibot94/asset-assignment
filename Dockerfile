FROM python:3.7-alpine

RUN pip install pipenv
COPY . /app
WORKDIR /app
RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "run.py"]