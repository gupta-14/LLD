from LogProcessor.LogProcessor import LogProcessor

class DebugLogProcessor(LogProcessor):
    def __init__(self, nextLogProcessor: LogProcessor):
        super().__init__(nextLogProcessor)

    def log(self, logLevel, message):
        if logLevel == self.DEBUG:
            print(f"DEBUG: {message}")
        else:
            super().log(logLevel, message)