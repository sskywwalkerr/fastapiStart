import logging
from datetime import datetime
from pythonjsonlogger import jsonlogger

from api.config import Config

logger = logging.getLogger()

logHandler = logging.StreamHandler()


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """Класс-форматтер для логов."""

    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(
            log_record, record, message_dict
        )
        if not log_record.get('timestamp'):
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


formatter = CustomJsonFormatter(
    '%(timestamp)s %(level)s %(message)s %(module)s %(funcName)s'
)

logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(Config.LOG_LEVEL)
