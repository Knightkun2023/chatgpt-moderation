from datetime import datetime
import string, random, tiktoken, uuid, re, requests
from urllib.parse import urlparse, parse_qs

def get_query_param_from_url(url, param_name):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get(param_name, [None])[0]

def is_empty(s) -> bool:
    if (type(s) == str):
        s = s.strip()
        if s == '':
            return True
        if is_numeric(s):
            if int(s) != 0:
                return False
            return True
        return False
    return not bool(s)

def valid_datetime(dt) -> bool:
    try:
        # strptimeは文字列を日時オブジェクトに変換します
        # 引数には変換したい文字列とその形式を指定します
        datetime.strptime(dt, '%Y%m%d%H%M%S%f')
        return True
    except ValueError:
        # ValueErrorが発生した場合は、引数の文字列が指定した形式に従っていないことを意味します
        return False

def is_valid_uuid(uuid_str):
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj) == uuid_str  # 正しい形式のUUIDであればTrueを返す
    except ValueError:
        return False  # UUIDの形式でない場合はFalseを返す

def is_numeric(s) -> bool:
    return bool(s) and s.isdigit()

def get_current_time() -> str:
    return datetime.now().strftime('%Y%m%d%H%M%S%f')[:17]

def get_display_time(s) -> str:
    # 入力の文字列を解析する
    dt = datetime.strptime(s, '%Y%m%d%H%M%S%f')

    # datetimeオブジェクトを任意の文字列形式に変換する
    # ここでは例として、'%Y-%m-%d %H:%M:%S'形式に変換するとします。
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def checkbox_to_save(c) -> int:
    if not is_empty(c) and c == '1':
        return True
    return False

def is_checked(b) -> str:
    if b:
        return ' checked'
    return ' '

def is_disabled(b) -> str:
    if b:
        return ' disabled'
    return ' '

def generate_random_string(length=48) -> str:
    # string.ascii_lettersには半角アルファベット（大文字小文字両方）が含まれています
    # string.digitsには0から9までの数字が含まれています
    characters = string.ascii_letters + string.digits

    # 指定した長さのランダムな文字列を生成
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    return random_string

import re

def is_alnum(s) -> bool:
    return re.match(r'^[a-zA-Z0-9-_]*$', s) is not None

def is_alpha_digits(s, min, max, required=False) -> bool:
    if required:
        if is_empty(s):
            return False
    if not is_empty(s):
        if len(s) < min or len(s) > max or not is_alnum(s):
            return False
    return True

models = ('gpt-3.5-turbo', 'gpt-3.5-turbo-0301', 'gpt-3.5-turbo-0613', 'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-16k-0613')
def check_model(m) -> bool:
    return m in models

def count_token(s):
    encoding = tiktoken.get_encoding('cl100k_base')
    return len(encoding.encode(s))   # トークン数を返す。

def remove_control_characters(input_string):
    # 制御文字を除去する正規表現パターン
    control_chars = ''.join(map(chr, list(range(0, 32)))) + ''.join(map(chr, list(range(127, 160))))
    control_char_re = re.compile('[%s]' % re.escape(control_chars))
    return control_char_re.sub('', input_string)

def get_moderation_result(content, key, moderation_model_no=1) -> dict:
    moderation_model = 'text-moderation-latest'
    if moderation_model_no == 2:
        moderation_model = 'text-moderation-stable'
    
    url = "https://api.openai.com/v1/moderations"
    headers = {
        "Authorization": "Bearer " + key,
    }
    payload = {
        "input": content,
        "model": moderation_model
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return {"error": {
            "status_code": response.status_code,
            "text": response.text
        }}

def get_moderation_result_simply(content, key, moderation_model_no=1) -> dict:
    result_dict = get_moderation_result(content, key, moderation_model_no)
    if 'error' in result_dict:
        return {
            'error': 'Error ocurred in Moderation API.',
            'results': []
        }

    result_val = 'ok'
    if 'results' in result_dict and len(result_dict['results']) > 0:
        result_elem = result_dict['results'][0]
        if 'category_scores' in result_elem:
            category_scores = result_elem['category_scores']
            if 'sexual' in category_scores and category_scores['sexual'] > 0.270:
                result_val = 'orange'
            if 'sexual/minors' in category_scores and category_scores['sexual/minors'] > 0.200:
                result_val = 'red'
        if result_val == 'ok' and 'flagged' in result_elem and result_elem['flagged']:
            result_val = 'orange'
    
    return {'result_val': result_val}
