FROM python:3.12-alpine

ENV PROJECT_DIR="/code" \
    PORT=8000

WORKDIR $PROJECT_DIR

RUN apk update && apk add --no-cache \
    build-base \
    postgresql-dev

COPY requirements.txt $PROJECT_DIR

RUN pip install -r $PROJECT_DIR/requirements.txt
gaa
COPY . $PROJECT_DIR/

RUN chmod +x ${PROJECT_DIR}/scripts/start_api.sh

EXPOSE $PORT

CMD ["./scripts/start_api.sh"]