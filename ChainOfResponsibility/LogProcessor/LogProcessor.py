from abc import ABCMeta, abstractmethod
# from LogProcessor.LogProcessor import LogProcessor

class LogProcessor(metaclass=ABCMeta):

    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self, loggerProcessor) -> None:
        self.nextLoggerProcessor = loggerProcessor
    
    @abstractmethod
    def log(self, logLevel, message):
        if self.nextLoggerProcessor:
            self.nextLoggerProcessor.log(logLevel, message)