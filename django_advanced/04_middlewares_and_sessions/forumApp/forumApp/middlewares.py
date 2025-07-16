import time
from datetime import datetime

from django.utils.deprecation import MiddlewareMixin


class MeasureTimeMiddleware(MiddlewareMixin):
    def process_request(self, request, *args, **kwargs):
        self.start_time = time.time()

    def process_response(self, request, response, *args, **kwargs):
        self.end_time = time.time()
        print(f"Request to {request.path} took {self.end_time - self.start_time:.4f}seconds.")
        return response

    # def process_template_response(self, request, response, *args, **kwargs):
    #     response.context_data["current_time"] = datetime.now()
    #     return response


# class MeasureTimeMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request, *args, **kwargs):
#         start_time = time.time()  # process_request
#         response = self.get_response(request, *args, **kwargs)
#         end_time = time.time()  # process_response
#
#         print(f"Request to {request.path} took {end_time - start_time:.4f}seconds.")
#
#         return response


def measure_time(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()  # process_request
        response = get_response(request, *args, **kwargs)
        end_time = time.time()  # process_response

        print(f"Request to {request.path} took {end_time - start_time:.4f}seconds.")

        return response

    return middleware