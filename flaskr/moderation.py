from flask import session, render_template, request, jsonify
from . import app
from .utils.commons import generate_random_string, get_query_param_from_url, get_moderation_result, get_moderation_result_simply
import os

@app.route('/prompt/free', methods=['GET'])
def system_prompt_detail_show_free():

    csrf_token = generate_random_string(48)  # CSRF対策にランダムなシークレットキーを設定
    session['system_prompt_csrf_token'] = csrf_token

    free_key = request.args.get('p', '')
    if free_key in app.config['MODERATION_CREDENTIALS']:
        return render_template("moderation.html", system_prompt={}, csrf_token=csrf_token,
                                user_name=app.config['MODERATION_CREDENTIALS'][free_key])

    return render_template("error/403.html"), 403

@app.route('/prompt/moderation', methods=['POST'])
def check_moderation():

    # free_keyをチェックする
    custom_header_value = request.headers.get('X-Chat-Url', None)
    free_key = get_query_param_from_url(custom_header_value, 'p')
    if not free_key in app.config['MODERATION_CREDENTIALS']:
        response_code = 403
        result_dict = {'error_message':'Error', 'result': []}
        return jsonify(result_dict), response_code

    # パラメータを受け取る
    data = request.get_json()
    
    # csrf_token = data['csrf_token']
    # # CSRFトークンのチェック
    # if not session['system_prompt_csrf_token'] == csrf_token:
    #     dic = {}
    #     dic['error_message'] = 'Invalid access.'
    #     return jsonify(dic), 403  # 不正なアクセス

    content = data['content']
    moderation_model_no = 1
    if data['moderation_model_no'] == '2':
        moderation_model_no = 2
    result_dict = get_moderation_result(content=content, key=os.environ['OPENAI_API_KEY'], moderation_model_no=moderation_model_no)

    response_code = 200
    if 'error' in result_dict:
        # エラーだった場合
        response_code = 400
        dic = {'error_message':'Error', 'result': result_dict}
        result_dict = dic

    return jsonify(result_dict), response_code

@app.route('/prompt/moderation2', methods=['POST'])
def check_moderation2():

    # free_keyをチェックする
    custom_header_value = request.headers.get('X-Chat-Url', None)
    if custom_header_value and not custom_header_value.startswith('https://chat.openai.com/'):
        response_code = 403
        result_dict = {'error_message':'Error', 'result': []}
        return jsonify(result_dict), response_code

    # パラメータを受け取る
    data = request.get_json()

    content = data['content']
    moderation_model_no = 1
    if data['moderation_model_no'] == '2':
        moderation_model_no = 2
    result_dict = get_moderation_result_simply(content=content, key=os.environ['OPENAI_API_KEY'], moderation_model_no=moderation_model_no)

    response_code = 200
    if 'error' in result_dict:
        # エラーだった場合
        response_code = 400
        dic = {'error': result_dict['error'], 'error_message':'Error'}
        result_dict = dic

    return jsonify(result_dict), response_code
