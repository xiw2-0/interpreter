from enum import Enum


class TokenType(Enum):
    INTEGER = 'INTEGER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    EOF = 'EOF'


class Token():
    def __init__(self, type: TokenType, value: object) -> None:
        self.type = type
        self.value = value

    def __str__(self) -> str:
        return f'Token({self.type}, {self.value})'
