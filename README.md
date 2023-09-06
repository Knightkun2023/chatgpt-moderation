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

### Voice Environment (Optional)
Install and Run VOICEVOX  
https://voicevox.hiroshiba.jp/  

### config.py settings
Edit flaskr/config.py

### How to run Flask
#### Prepare
##### Mac (Bash/zsh)
```
source ./venv/bin/activate  
export FLASK_APP=flaskr  
export FLASK_ENV=development  
export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(25))')
```

##### Windows
```
.\venv\Scripts\activate.bat  
set FLASK_APP=flaskr  
set FLASK_ENV=development  
set SECRET_KEY=***任意のランダムな文字列***
```

##### PowerShell (Windows)
```
.\venv\Scro@ts\Activate.ps1  
$env:FLASK_APP="flaskr"  
$env:FLASK_ENV="development"  
$env:SECRET_KEY="***任意のランダムな文字列***"
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

## Reference Links
【PythonでWebアプリ作成】Flask入門 ！この動画１本でWebアプリが作れちゃう！ 〜 Pythonプログラミング初心者用 〜  
https://www.youtube.com/watch?v=EQIAzH0HvzQ  

【話題の技術】ChatGPTのAPIをPythonから使う方法を解説！APIを使って議事録の要約プログラムを作ってみた！〜人工知能の進化が凄すぎる〜  
https://www.youtube.com/watch?v=kodz6fzbAUA  

【コピペでOK】CSSだけでLINE風の「吹き出し」を作る方法！  
https://stand-4u.com/css/fukidashi.html  

Free Icons | Font Awesome  
https://fontawesome.com/search?o=r&m=free&s=regular&f=classic  

WindowsでPIP Install するとSSLエラーになるのを解消する。  
https://qiita.com/kekosh/items/e96e822bf9cb6ca1aff8  

自然な会話できてすごい / JavaScriptで簡単に作れる  
https://www.youtube.com/watch?v=oOUBvdLKLK4  

ChatGPTとWhisperのAPIを使用して、AIと話せる会話アプリを作ってみた【Python初心者でも使えるコード付きで解説】  
https://www.youtube.com/watch?v=ECwfieE5hDU  
