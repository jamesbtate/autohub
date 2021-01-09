from backend import django_setup
from logging import Handler, LogRecord
from portal.models import DaemonLog
from datetime import datetime


class DjangoHandler(Handler):
    """ Writes logs to the Django ORM """
    def __init__(self) -> None:
        super().__init__()

    def emit(self, record: LogRecord) -> None:
        try:
            message = self.format(record)
            dt = datetime.fromtimestamp(record.created)
            new_log = DaemonLog(datetime=dt, message=message, level_name=record.levelname)
            new_log.save()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
