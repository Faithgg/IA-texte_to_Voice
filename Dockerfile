FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN python -m venv myenv
RUN . myenv/bin/activate
RUN python app.py