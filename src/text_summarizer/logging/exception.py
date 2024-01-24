import sys
from text_summarizer.logging.logger import logging

def error_message_detail(error, error_detail: sys):
    " Raising custom exception. "

    # Get the file and line number of exception
    _, _, exc_tb = error_detail.exc_info() 
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in python script name [{file_name}] line number [{line_number}] error message[{str(error)}]."
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
if __name__ == '__main__':
    try:
        a=2/0
    except Exception as e:
        logging.info('Divide by zero')
        raise CustomException(e, sys)

    