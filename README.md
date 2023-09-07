# ChatGPT Moderation
ChatGPTのモデレーションチェックを行うことができる画面を提供します。  
また、ブックマークレットによりChatGPT Web画面からモデレーションチェックの結果を利用することができます。

## How to setup & run 'ChatGPT Moderation'

### Python for Mac
```
use brew -> pyenv  
```
https://prog-8.com/docs/python-env

### Set up venv
```
python -m venv venv  
source ./venv/bin/activate  
pip install -r requirements.txt
```
*\*including install openai library.*

#### How to upgrade requirements.txt
```
pip freeze > requirements.txt  
```

### config.py settings
Edit flaskr/config.py

### How to run Flask
#### Prepare
MODERATION_ACCESS_KEY :  
The MODERATION_ACCESS_KEY is configured as follows:  
```Access Key 1: Access Name 1, Access Key 2: Access Name 2,...```
The access key is given as /prompt/free?p=Access Key 1. The access name is displayed at the top of the Moderation API screen.
##### Mac (Bash/zsh)
```
source ./venv/bin/activate  
export FLASK_APP=flaskr  
export FLASK_ENV=development  
export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(25))')  
export REMOTE_URL=<Url of remote host include context path. The trailing slash is not necessary.>  
export MODERATION_ACCESS_KEY='Access Key 1: Access Name 1, Access Key 2: Access Name 2,...'
```

##### Windows
```
.\venv\Scripts\activate.bat  
set FLASK_APP=flaskr  
set FLASK_ENV=development  
set SECRET_KEY=***任意のランダムな文字列***
set REMOTE_URL=<Url of remote host include context path. The trailing slash is not necessary.>  
set MODERATION_ACCESS_KEY="Access Key 1: Access Name 1, Access Key 2: Access Name 2,..."
```

##### PowerShell (Windows)
```
.\venv\Scro@ts\Activate.ps1  
$env:FLASK_APP="flaskr"  
$env:FLASK_ENV="development"  
$env:SECRET_KEY="***任意のランダムな文字列***"
$env::REMOTE_URL="<Url of remote host include context path. The trailing slash is not necessary.>"  
$env::MODERATION_ACCESS_KEY="Access Key 1: Access Name 1, Access Key 2: Access Name 2,..."
```

#### Set Open API Key
##### Mac (Bash/zsh)
```
export OPENAI_API_KEY="OpenAIのAPIキー"  
```

##### Windows
```
set OPENAI_API_KEY="OpenAIのAPIキー"  
```

##### PowerShell (Windows)
```
$env:OPENAI_API_KEY="OpenAIのAPIキー"  
```

#### Run
```
flask run  
```
or  
```
flask run --port=5505  
```
*\*On a Mac, it's likely that Flask's default port might be in use, so we recommend specifying a port.*　　

*\*First, you must access /setup to setup database.*

### Flask-Babel
```
sh flaskr/pybabel.sh
#cd flaskr
#pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
##pybabel init -i messages.pot -d translations -l ja
#pybabel update -i messages.pot -d translations -l ja

cd flaskr
pybabel compile -d translations
```
