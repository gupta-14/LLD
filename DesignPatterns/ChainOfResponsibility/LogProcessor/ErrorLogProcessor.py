from LogProcessor.LogProcessor import LogProcessor

class ErrorLogProcessor(LogProcessor):
    def __init__(self, nextLogProcessor: LogProcessor):
        super().__init__(nextLogProcessor)

    def log(self, logLevel, message):
        if logLevel == self.ERROR:
            print(f"ERROR: {message}")
        else:
            super().log(logLevel, message)