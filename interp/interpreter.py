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

        There will be spaces in text.
        """
        # skip spaces
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

        # eof
        if self.pos >= len(self.text):
            return Token(TokenType.EOF, None)
        # integer
        if self.text[self.pos].isdigit():
            num = 0
            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                num = num * 10 + int(self.text[self.pos])
                self.pos += 1
            return Token(TokenType.INTEGER, num)
        # operator
        if self.text[self.pos] == '+':
            token = Token(TokenType.PLUS, self.text[self.pos])
            self.pos += 1
            return token
        if self.text[self.pos] == '-':
            token = Token(TokenType.MINUS, self.text[self.pos])
            self.pos += 1
            return token
        # error
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
        op = self.get_next_token()
        if not (op.type is TokenType.PLUS or op.type is TokenType.MINUS):
            self.error()
        right = self.eat(self.get_next_token(), TokenType.INTEGER)
        print(right)
        if op is TokenType.PLUS:
            return left.value + right.value
        else:
            return left.value - right.value
