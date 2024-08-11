import sys
import traceback

class CustomException(Exception):
    def __init__(self, error):
        super().__init__(str(error))
        self.error_message = self.get_error_message(error)
    
    def get_error_message(self, error):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_message = (
            f"Error occurred in python script: {file_name} "
            f"at line {line_number} - {type(error).__name__}: {error}"
        )
        return error_message
    
    def __str__(self):
        return self.error_message




