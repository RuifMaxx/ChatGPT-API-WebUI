# Chat-GBT-WebUI

the minimum webpage implement of to Call ChatGPT API

## Preview

![](./chatgpt.gif)

## Docker Hub 

```bash
docker run --name app -p 80:80 -d ruifma/chatgptwebui:0.12 python app.py your-api-key
```

## Docker

```bash
./run.sh
docker run --name app -p 80:80 -d app:v0 python app.py your-api-key
```

## pip
```bash
pip install -r requirements.txt
python app.py your-api-key
```
