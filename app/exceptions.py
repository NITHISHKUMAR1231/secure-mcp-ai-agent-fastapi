# app/exceptions.py

class ToolNotFoundException(Exception):
    pass


class UnauthorizedException(Exception):
    pass


class PromptInjectionException(Exception):
    pass