# Chat-GBT-WebUI

the minimum webpage implement of to Call ChatGPT API

## Preview

![](./chatgpt.gif)

## Quick Start

* edit app.py

```python
openai.api_key = "your_key"
```

```bash
docker build --network=host -t app:v0 .
docker run --name app -p 80:80 -d app:v0

```
