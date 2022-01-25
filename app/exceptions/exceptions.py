

class UserException(Exception):
    ...


class UserUnauthorizedError(UserException):
    def __init__(self):
        self.status_code = 401
        self.detail = "invalid identifiants"


class UserNotFoundError(UserException):
    def __init__(self):
        self.status_code = 404
        self.detail = "User Not Found"

class UserExistError(UserException):
    def __init__(self):
        self.status_code = 400
        self.detail = "User Exist"


class ActivitiesException(Exception):
    ...


class ActivitiesNotFoundError(ActivitiesException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Activities Not Found"

class ActivitiesExistError(ActivitiesException):
    def __init__(self):
        self.status_code = 400
        self.detail = "Activities Exist"
