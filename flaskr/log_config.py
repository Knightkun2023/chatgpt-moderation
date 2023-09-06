import logging
from logging.handlers import TimedRotatingFileHandler

def configure_logging(app):

    # ロガーを作成
    logger = logging.getLogger('app_logger')
    logger.setLevel(logging.DEBUG)

    log_format = '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_format)

    # 日単位のローテーション
    log_file = 'logs/app.log'
    file_handler = TimedRotatingFileHandler(log_file, when='midnight', backupCount=30)
    file_handler.setFormatter(logging.Formatter(log_format))
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    # 標準出力へのロガー
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

