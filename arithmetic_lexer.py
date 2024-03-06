from ply import lex

tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'SLASH', 'LP', 'RP', 'LBP', 'RBP', 'VAR', 'EQ', 'COMMA', 'DOT', 'POW', 'SIN', 'POLY', 'APP', 'DER', 'POLYTIMES', 'PI', 'E')

t_NUMBER = '(([1-9][0-9]*)|0)(\.[0-9]+)?'
t_ignore = ' '
t_PLUS = '\+'
t_MINUS = '-'
t_TIMES = '\*'
t_SLASH = '\/'
t_LP = '\('
t_RP = '\)'
t_LBP = '\['
t_RBP = '\]'
t_VAR = '[a-z][a-zA-Z0-9_-]*'
t_EQ = '='
t_COMMA = ','
t_DOT = '\.'
t_POW = '\^'
t_SIN = 'Sin'
t_POLY = 'Poly'
t_APP = 'Apply'
t_DER = 'Derivate'
t_POLYTIMES = 'Times'
t_PI = 'Pi'
t_E = 'E'

lexer = lex.lex()

if __name__ == "__main__" :
    lexer.input('a1+32=Sin Pis, Poly([3,4])')
    for tok in lexer :
        print(tok)
