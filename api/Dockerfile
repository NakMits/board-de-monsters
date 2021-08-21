FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./app $APP_HOME

RUN pip install -r $APP_HOME/requirements_for_build_container.txt

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 --timeout 0 main:app
