# Chat-GBT-WebUI

## Preview

![](./chatgpt.gif)

## Quick Start

```bash
docker build --network=host -t app:v0 .
docker run --name app -p 80:80 -d app:v0

```

* edit app_frontend.html

```html
<form action="http://your-ip:5000/chat" method="POST">
```

### Run

```bash

python app.py

``` 