import logging
from core.config import settings
from modals.logging import Log
from core.database import get_db


class DatabaseLoggerHandler(logging.Handler):
    """
    Customized logging handler that puts logs to the database.
    """

    def __init__(self):
        super().__init__()
        self.db = get_db()
        self.dummy_log = logging.LogRecord(None, None, "", 0, "", (), None, None)

    def emit(self, record):
        try:
            if record.levelno in [logging.INFO, logging.ERROR, logging.CRITICAL]:
                extra = dict()
                all_fields = record.__dict__.copy()
                known_fields = dir(self.dummy_log)

                diff = set(all_fields) - set(known_fields)
                for field in diff:
                    extra[field] = all_fields[field]

                if record.exc_info:
                    extra["traceback"] = logging._defaultFormatter.formatException(
                        record.exc_info
                    )

                # Make log
                log = Log(
                    server=settings.app_name,
                    level=record.levelname,
                    message=record.getMessage(),
                    extra=extra,
                )

                self.db.add(log)
                self.db.commit()
        except Exception as e:
            print(f"Error while logging to database: {e}")


def setup() -> None:
    # Creating formatter
    logging_format = "[%(asctime)s] %(levelname)s | %(message)s"
    if settings.logging_format:
        logging_format = settings.logging_format

    formatter = logging.Formatter(logging_format, "%Y-%m-%d %H:%M:%S")

    # Creating the handler
    db_handler = DatabaseLoggerHandler()
    db_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Assigning the handler
    logger = logging.getLogger()
    logger.setLevel(settings.logging_level)
    logger.handlers.clear()
    logger.addHandler(db_handler)
    logger.addHandler(stream_handler)
