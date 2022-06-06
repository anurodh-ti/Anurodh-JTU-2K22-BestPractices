from rest_framework.exceptions import APIException


class UnauthorizedUserException(APIException):
    status_code = HTTP_404_NOT_FOUND
    default_detail = "Not Found"
    default_code = "Records unavailable"