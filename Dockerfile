FROM python:3.11-alpine
RUN apk add --no-cache python3-dev
WORKDIR /app
COPY ./ /app
RUN python3 -m venv venv && source ./venv/bin/activate && pip install -r requirements.txt &&  chmod +x main.py
ENV VIRUAL_ENV=/app/venv
ENV PATH="$VIRUAL_ENV/bin:$PATH"
CMD [ "python3", "main.py" ]
