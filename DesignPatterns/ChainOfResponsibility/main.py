from LogProcessor.LogProcessor import LogProcessor
from LogProcessor.InfoLogProcessor import InfoLogProcessor
from LogProcessor.ErrorLogProcessor import ErrorLogProcessor
from LogProcessor.DebugLogProcessor import DebugLogProcessor

logObject = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor(None)))

logObject.log(LogProcessor.DEBUG, message="need to debug this")
logObject.log(LogProcessor.INFO, message="just for info")
logObject.log(LogProcessor.ERROR, message="exception happens")



