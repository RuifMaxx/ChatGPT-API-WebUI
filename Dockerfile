FROM python:3.8

WORKDIR /docker_demo
 
ADD . .

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple openai==0.27.0

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask==2.0.3

CMD ["python", "app.py"]

