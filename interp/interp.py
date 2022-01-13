from interp.interpreter import Interpreter

def interp():
    while True:
        text = input('calc> ')
        interpreter = Interpreter(text)
        print(interpreter.expr())