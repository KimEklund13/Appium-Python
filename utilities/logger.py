import inspect
import logging


def logger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from which this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(filename="automation.log", mode='w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s: - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
