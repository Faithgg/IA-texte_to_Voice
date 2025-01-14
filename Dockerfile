FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN python -m venv myenv
RUN . myenv/bin/activate
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 app.py