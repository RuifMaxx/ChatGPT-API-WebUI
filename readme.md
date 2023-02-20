# Chat-GBT-WebUI

## Quick Start

### Install

* pip install

```bash
pip install openai
pip install flask
```

* apply for a key from [OpenAI](https://beta.openai.com/)

* edit app.py

```python

openai.api_key = "your_key"
    
```

* edit app_frontend.html

```html
<form action="http://your-ip:5000/chat" method="POST">
```

### Run

```bash

python app.py

``` 