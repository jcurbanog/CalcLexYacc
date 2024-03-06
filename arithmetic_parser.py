from arithmetic_expressions import (AddExpr, Assignment, DivExpr, Euler, Litteral, MulExpr, OppExpr, Pi, PolyExpr, PowExpr, SinExpr, Statement, SubExpr, Var, VariableNotFound, dic)
from arithmetic_lexer import tokens
from ply import yacc
import numpy as np

class SyntaxErrorFound(Exception):
    pass

precedence = (
    ('left', 'EQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'SLASH'),
    ('left', 'POW')
)

def p_statement(p):
    """
    statement : expression
              | assignment
              | polynomial
    """
    p[0] = p[1]

def p_litteral(p) :
    'expression : NUMBER'
    p[0] = Litteral(float(p[1]))

def p_var_assignment(p) :
    'assignment : VAR EQ expression'
    try:
        dic.setVariable(p[1], p[3].eval())
        p[0] = Assignment(f'{p[1]} = {p[3].eval()}')
    except Exception as err:
        p[0] = Assignment(err)

def p_poly_assignment(p) :
    'assignment : VAR EQ polynomial'
    dic.setVariable(p[1], p[3])
    p[0] = Assignment(f'{p[1]} = {p[3]}')

def p_apply(p):
    """
    expression : VAR DOT APP LP expression RP
              | polynomial DOT APP LP expression RP
    """
    if isinstance(p[1], Assignment):
        p[0] = p[1]
        return
    try:
        poly = p[1] if isinstance(p[1], PolyExpr) else dic.getVariable(p[1])
        assert isinstance(poly, PolyExpr)
        p[0] = poly.apply(p[5])
    except AssertionError:
        p[0] = Assignment(f'"{p[1]}" is not a PolyExpr')
    except VariableNotFound as err:
        p[0] = Assignment(err)

def p_polytimes(p):
    """
    polynomial : VAR DOT POLYTIMES LP VAR RP
              | VAR DOT POLYTIMES LP polynomial RP
              | polynomial DOT POLYTIMES LP VAR RP
              | polynomial DOT POLYTIMES LP polynomial RP
    """
    if isinstance(p[5], Assignment):
        p[0] = p[5]
        return
    if isinstance(p[1], Assignment):
        p[0] = p[1]
        return
    try:
        poly = p[1] if isinstance(p[1], PolyExpr) else dic.getVariable(p[1])
        assert isinstance(poly, PolyExpr), p[1]
        other = p[5] if isinstance(p[5], PolyExpr) else dic.getVariable(p[5])
        assert isinstance(other, PolyExpr), p[5]
        p[0] = poly.times(other)
    except AssertionError as e:
        p[0] = Assignment(f'"{e}" is not a PolyExpr')
    except VariableNotFound as err:
        p[0] = Assignment(err)

def p_derivate(p):
    """
    polynomial : VAR DOT DER LP RP
              | polynomial DOT DER LP RP
    """
    if isinstance(p[1], Assignment):
        p[0] = p[1]
        return
    try:
        poly = p[1] if isinstance(p[1], PolyExpr) else dic.getVariable(p[1])
        assert isinstance(poly, PolyExpr)
        p[0] = poly.derivate()
    except AssertionError:
        p[0] = Assignment(f'"{p[1]}" is not a PolyExpr')
    except VariableNotFound as err:
        p[0] = Assignment(err)

def p_poly(p):
    'polynomial : POLY LP list RP'
    p[0] = PolyExpr(p[3])

def p_list_term(p) :
    """
    list_term   : expression
                | list_term COMMA list_term
    """
    if len(p) == 2 :
        p[0] = [p[1]]
    else:
        p[0] = [*p[1], *p[3]]

def p_list(p):
    """
    list    : LBP RBP
            | LBP list_term RBP
    """
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]

def p_var(p) :
    'expression : VAR'
    p[0] = Var(p[1])

def p_add(p) :
    'expression : expression PLUS expression'
    p[0] = AddExpr(p[1], p[3])

def p_sub(p) :
    'expression : expression MINUS expression'
    p[0] = SubExpr(p[1], p[3])

def p_mul(p) :
    'expression : expression TIMES expression'
    p[0] = MulExpr(p[1], p[3])

def p_div(p) :
    'expression : expression SLASH expression'
    p[0] = DivExpr(p[1], p[3])

def p_power(p):
    'expression : expression POW expression'
    p[0] = PowExpr(p[1], p[3])

def p_sin(p):
    'expression : SIN LP expression RP'
    p[0] = SinExpr(p[3])

def p_parenthesis(p) :
    'expression : LP expression RP'
    p[0] = p[2]

def p_inversion(p) :
    'expression : MINUS expression'
    p[0] = OppExpr(p[2])

def p_pi(p) :
    'expression : PI'
    p[0] = Pi(p[1])

def p_euler(p) :
    'expression : E'
    p[0] = Euler(p[1])

def p_error(p):
    if p:
        raise SyntaxErrorFound(f"Syntax error at token '{p.value}' (type: {p.type}) at line {p.lineno}, position {p.lexpos}")
    else:
        raise SyntaxErrorFound("Syntax error at EOF")

parser = yacc.yacc()

if __name__ == "__main__":
    print(parser.parse('42').eval())
    print(parser.parse('10-(9+3)').eval())
    print(str(parser.parse("(2+(3*1))")), "(2+(3*1))")
    print(parser.parse('((2 + 7)*(4-2))').eval())
    print(parser.parse('test_var').eval())
    print(parser.parse('test_var + 44').eval())
    parser.parse('z = 3')
    parser.parse('x = z + 4')
    print(parser.parse("(2+(3*1))"))
    print(parser.parse("w = Poly([1,4.3,5,0,1])").exec())
    print(parser.parse("w.Apply(-1.5)").exec())
    print(parser.parse("ma.Apply(-1.5)"))
