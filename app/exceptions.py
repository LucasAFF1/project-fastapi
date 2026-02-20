from fastapi import status


class DomainError(Exception):
    status_code = status.HTTP_400_BAD_REQUEST 
    detail = {"error":"Domain Error"}

class UserAlreadyExist(DomainError): 
    status_code = status.HTTP_400_BAD_REQUEST
    detail = {"error":"User already exists"}

class NotAuthenticated(DomainError):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = {"error":"Not authenticated"}

class InvalidToken(DomainError):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    detail = {"error": "User is not logged in"}

class NotAuthorized(DomainError): 
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = {"error":"Not authorized"}

class OrderNotFound(DomainError): 
    status_code = status.HTTP_404_NOT_FOUND
    detail = {"error":"Order not found"}

class NotActiveUser(DomainError):
    status_code = status.HTTP_404_NOT_FOUND
    detail = {"error": "User is not active"}

class UserNotFound(DomainError):
    status_code = status.HTTP_404_NOT_FOUND
    detail = {"error":"User not found"}

class IncorrectPassword(DomainError):
    status_code = status.HTTP_403_FORBIDDEN
    detail = {"error": "Incorrect password"}