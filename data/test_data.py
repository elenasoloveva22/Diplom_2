class StatusCodes:
    """Коды статусов HTTP"""
    SUCCESS = 200
    FORBIDDEN = 403
    BAD_REQUEST = 400
    NOT_FOUND = 404


class ErrorMessages:
    """Сообщения об ошибках от API"""
    USER_ALREADY_EXISTS = "User already exists"
    REQUIRED_FIELDS_MISSING = "Email, password and name are required fields"
    INVALID_CREDENTIALS = "email or password are incorrect"


class ResponseFields:
    """Поля в JSON-ответах от API"""
    SUCCESS = "success"
    ACCESS_TOKEN = "accessToken"
    MESSAGE = "message"
    USER = "user"


class TestData:
    """Основные тестовые данные"""
    
    # Статус коды
    SUCCESS_STATUS = StatusCodes.SUCCESS
    FORBIDDEN_STATUS = StatusCodes.FORBIDDEN
    
    # Сообщения об ошибках
    USER_ALREADY_EXISTS = ErrorMessages.USER_ALREADY_EXISTS
    REQUIRED_FIELDS_MISSING = ErrorMessages.REQUIRED_FIELDS_MISSING
    
    # Тестовые значения
    EMPTY_PASSWORD = ""
    EMPTY_NAME = ""
    EMPTY_EMAIL = ""