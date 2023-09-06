# サービス時のアプリケーションルート。必要に応じて '/flask' などを指定。
APPLICATION_ROOT=''

# Protocol + Remote Host
REMOTE_URL='http://127.0.0.1:5506'

# Flask-Sessionによるセッションの格納先。filesystemはローカルファイル。他にredis、memcacheなどをサポートしている。
SESSION_TYPE='filesystem'
