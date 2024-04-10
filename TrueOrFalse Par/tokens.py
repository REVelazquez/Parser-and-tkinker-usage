from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    TRUE =1
    FALSE = 2
    AND = 3
    OR = 4
    NOT= 5
    LPAREN = 6
    RPAREN = 7  

@dataclass
class Token:
    token_type: TokenType
    lexeme: str