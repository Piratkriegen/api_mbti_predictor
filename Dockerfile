FROM python:3.8.6-buster

COPY api /api
COPY requirements.txt /requirements.txt
COPY model.joblib /model.joblib
COPY setup.py /setup.py
COPY scripts /scripts

RUN pip install --upgrade pip
RUN pip install -e .

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
