import logging

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
      
        # Logger Attributes
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Check if the logger already has a file handler
        handlers = [h for h in self.logger.handlers if isinstance(h, logging.FileHandler)]
        if not handlers:
            self.file_handler = logging.FileHandler(self.log_file)
            self.file_handler.setFormatter(self.formatter)
            self.logger.addHandler(self.file_handler)

        # Set propagate to False to avoid duplicate log messages
        self.logger.propagate = False
