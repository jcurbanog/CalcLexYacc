from arithmetic_parser import SyntaxErrorFound, parser
from arithmetic_expressions import dic

if __name__ == "__main__":
    while(True):
        a = input(">> ")
        if a == 'quit':
            break
        try:
            print(parser.parse(a).exec())
        except SyntaxErrorFound as err:
            print(err)
