## Creating custom class for exception
import os
import sys

class HousingException(Exception): ## inheriting from Exception class of python  

    def __init__(self,error_message : Exception,error_detail : sys):
        ## creating and passing objects of exception class and sys modules 

        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(
                                error_message=error_message,
                                error_detail=error_detail
        )

    @staticmethod ## method which can be called without creating an object.
    def get_detailed_error_message(error_message: Exception,error_detail: sys)->sys:
        
        """
        error_message : Exception object
        error_detail : object of sys module
        """
        _,_ ,exec_tb = error_detail.exc_info()
        line_no = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured in scrip: [{file_name}] at line number : [{line_no}] error message : [{error_message}]"
        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str: 
        return HousingException.__name__str()