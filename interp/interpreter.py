from interp.token import Token, TokenType


class Interpreter():
    def __init__(self, text: str) -> None:
        self.text = text
        # for lex
        self.pos = 0

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self) -> Token:
        """Lexical analyzer. Returns one Token when it gets called.
        """
        if self.pos == len(self.text):
            return Token(TokenType.EOF, None)
        elif self.text[self.pos].isdigit():
            token = Token(TokenType.INTEGER, int(self.text[self.pos]))
            self.pos += 1
            return token
        elif self.text[self.pos] == '+':
            token = Token(TokenType.PLUS, self.text[self.pos])
            self.pos += 1
            return token
        else:
            self.error()

    def eat(self, current_token: Token, required_token_type: TokenType) -> Token:
        """Checks token type.
        """
        if current_token.type is required_token_type:
            return current_token
        self.error()

    def expr(self) -> int:
        """expr -> INTEGER PLUS INTEGER
        """
        left = self.eat(self.get_next_token(), TokenType.INTEGER)
        print(left)
        print(self.eat(self.get_next_token(), TokenType.PLUS))
        right = self.eat(self.get_next_token(), TokenType.INTEGER)
        print(right)

        return left.value + right.value
