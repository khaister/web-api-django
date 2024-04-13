import logging


# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
GRAY7 = "38;5;7"
GRAY8 = "38;5;8"
ORANGE = "33"
RED = "31"
WHITE = "0"


# don't use white for any logging to help distinguish from user print statements
LEVEL_COLOR_MAP = {
    logging.DEBUG: GRAY8,
    logging.INFO: GRAY7,
    logging.WARNING: ORANGE,
    logging.ERROR: RED,
}

LEVEL_EMOJI_MAP = {
    logging.DEBUG: "🐝",
    logging.INFO: "ℹ️",
    logging.WARNING: "⚠️",
    logging.ERROR: "🚨",
}


class ColorHandler(logging.StreamHandler):
    def emit(self, record):
        csi = f"{chr(27)}["  # control sequence introducer
        color = LEVEL_COLOR_MAP.get(record.levelno, WHITE)

        try:
            msg = self.format(record)
            self.stream.write(f"{csi}{color}m{LEVEL_EMOJI_MAP.get(record.levelno, "  ")} {msg}{csi}m{self.terminator}")
            self.flush()
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)
