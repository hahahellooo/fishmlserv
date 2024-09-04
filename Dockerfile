#FROM datamario24/python311scikitlearn-fastapi:1.0.0
#FROM python:3.11.9-slim-bullseye
#FROM python:3.11.9-alpine3.20
FROM meiun/isdomi:0.8.3
 
WORKDIR /code

COPY src/fishmlserv/main.py /code/
#COPY requirements.txt /code/
#COPY . /code/
#COPY ./requirements.txt /code/requirements.txt

# 모델 서빙(의존성의 위 BASE 이미지에서 모두 설치 했다)
RUN pip install --no-cache-dir --upgrade git+https://github.com/hahahellooo/fishmlserv.git@1.0.0/k
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
# 모델 서빙을 위해 API 구동을 위한 FastAPI RUN
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
