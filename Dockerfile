FROM python:3.8-slim-buster

WORKDIR /docker_demo
 
ADD . .

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

CMD ["python", "app.py"]