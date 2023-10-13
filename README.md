[targoyle.github.io](https://targoyle.github.io/)

### API localtest

localtest.sh

`pip install uvicorn`

```bash
#!/bin/bash

# Vercel
# export APP_PATH="/var/task/app"
export APP_PATH="/local/hoge/fuga/app"

uvicorn app.main:app --reload
```
