FROM python:3.12-slim as builder

WORKDIR /app

RUN python3 -m venv env
RUN /app/env/bin/pip install gunicorn

COPY . .

RUN /app/env/bin/pip install -r requirements.txt
RUN mv scripts/boxesserver scripts/boxesserver.py

# ---

FROM python:3.12-slim

RUN apt update && \
  apt install -y pstoedit --no-install-recommends && \
  apt clean

WORKDIR /app
COPY --from=builder /app /app

CMD /app/env/bin/gunicorn -b [::]:8000 -w 4 scripts.boxesserver
