import logging

class Logger:
    def __init__(self, log_file=".", log_level=logging.DEBUG,saveFile=True):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        formatter = logging.Formatter('%(asctime)s - %(filename)s_[line:%(lineno)d] - %(name)s - %(levelname)s - %(message)s')
        if saveFile:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def debug(self, msg):
        self.logger.debug(msg,stacklevel=2)

    # def info(self, msg, *args, **kwargs):
    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, stacklevel=2)
        # self.logger.info(msg, *args, **kwargs,stacklevel=2)

    def warning(self, msg):
        self.logger.warning(msg,stacklevel=2)

    def error(self, msg):
        self.logger.error(msg,stacklevel=2)

    def critical(self, msg):
        self.logger.critical(msg,stacklevel=2)



if __name__ == '__main__':
    log = Logger('test.log')
    log.debug('这是一条debug信息')
    log.info('这是一条info信息')
    log.warning('这是一条warning信息')
    log.error('这是一条error信息')
    log.critical('这是一条critical信息')
