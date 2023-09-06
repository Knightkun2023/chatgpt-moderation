from flask import Flask, request
from flask_babel import Babel
from flask_cors import CORS
from .log_config import configure_logging
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['REMOTE_URL'] = os.environ['REMOTE_URL']
CORS(app, resources={
    r"/prompt/moderation2": {
        "origins": "https://chat.openai.com",
        "allow_headers": ["Content-Type", "X-Chat-Url"]
    }
})
configure_logging(app)

# Jinja2フィルタを登録
from .utils.commons import get_display_time, is_checked, is_disabled
app.jinja_env.filters['get_display_time'] = get_display_time
app.jinja_env.filters['is_checked'] = is_checked
app.jinja_env.filters['is_disabled'] = is_disabled

# ルーティングをインポート
from . import moderation, token_counter, translation_js

@app.context_processor
def inject_common_variables():
    return dict(remote_url=app.config['REMOTE_URL'])
    # 必要に応じて他の変数も辞書に追加します。

def get_locale():
    # return request.accept_languages.best_match(['ja', 'fr', 'de', 'es', 'ko', 'pt', 'uk', 'zh_CN', 'zh_TW'])  # , 'ja_JP', 'en'
    return request.accept_languages.best_match(['ja'])

babel = Babel(app, locale_selector=get_locale)

@app.before_request
def set_application_root():
    '''
    アプリケーションルートを設定
    '''
    request.environ['SCRIPT_NAME'] = app.config['APPLICATION_ROOT']

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

def setup_access_keys():
    # 環境変数からアクセスキーを登録
    moderation_access_key = os.environ.get('MODERATION_ACCESS_KEY', '')

    # 文字列を','で分割して、さらに':'でキーと値に分割して辞書に変換
    dict_values = dict(item.split(":") for item in moderation_access_key.split(","))
    app.config['MODERATION_CREDENTIALS'] = dict_values

setup_access_keys()
