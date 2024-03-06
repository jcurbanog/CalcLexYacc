from abc import ABC, abstractmethod
from numbers import Number
import math

class Dic:
    def __init__(self):
        self._dic = {'test_var': 22}

    def getVariable(self, var):
        try:
            return self._dic[var]
        except KeyError:
            raise VariableNotFound(var)

    def setVariable(self, var, value):
        self._dic[var] = value


dic = Dic()

class VariableNotFound(Exception):
    """Exception raised when accessing to an undefined variable.

    Attributes:
        var -- variable name
    """

    def __init__(self, var):
        self.var = var
        self.message = f'"{self.var}" is not defined'
        super().__init__(self.message)

class Statement(ABC):
    def exec(self):
        try:
            return self.eval()
        except VariableNotFound as err:
            return err

    @abstractmethod
    def eval(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class Assignment(Statement):
    def __init__(self, v = None) -> None:
        super().__init__()
        self._value = v

    def eval(self):
        return self._value

    def __str__(self):
        return f"{ self.eval() }"

class AExpr(Statement):
    """ This class is abstract and serves as a superclass for all Arithmetic Expressions
    """

    @abstractmethod
    def eval(self) -> Number:
        pass


class Litteral(AExpr):
    """ This class represents the constant expressions. It inherits from AExpr and, unlike AExpr,
        it is a concrete class (because 'eval' is implemented).
    """
    def __init__(self, v: Number = 0) -> None:
        super().__init__()
        self._value = v

    def eval(self) -> Number:
        return self._value

    def __str__(self):
        return f"{ self.eval() }"

class Var(AExpr):
    def __init__(self, var_name: str = '') -> None:
        super().__init__()
        self._var_name = var_name

    def eval(self):
        return dic.getVariable(self._var_name)

    def __str__(self) -> str:
        return f"{ self._var_name }"


class BExpr(AExpr):
    """ This class represents the binary expressions and, by inheritance, it is abstract.
        The reason is that the 'eval' abstract method is not yet implemented.
        This class has four concrete subclasses that represent
        addition, subtraction, multiplication and division expressions.
    """

    def __init__(self, l: AExpr = None, r: AExpr = None) -> None:
        super().__init__()
        self._left = l
        self._right = r


class AddExpr(BExpr):
    """ Now come the concrete instances of binary expressions
    """

    def eval(self):
        return self._left.eval() + self._right.eval()

    def __str__(self):
        return f"({self._left} + {self._right})"


class SubExpr(BExpr):
    def eval(self):
        return self._left.eval() - self._right.eval()

    def __str__(self):
        return f"({self._left} - {self._right})"


class MulExpr(BExpr):
    def eval(self):
        return self._left.eval() * self._right.eval()

    def __str__(self):
        return f"({self._left} * {self._right})"


class DivExpr(BExpr):
    def eval(self):
        return self._left.eval() / self._right.eval()

    def __str__(self):
        return f"({self._left} / {self._right})"

class PowExpr(BExpr):
    def eval(self):
        return self._left.eval() ** self._right.eval()

    def __str__(self):
        return f"({self._left} ^ {self._right})"

class UExpr(AExpr):
    def __init__(self, v: Number = 0) -> None:
        super().__init__()
        self._value = v

class OppExpr(UExpr):
    def eval(self) -> Number:
        return self._value.eval() * -1

    def __str__(self):
        return f"(-({self._value}))"

class SinExpr(UExpr):
    def eval(self) -> Number:
        return math.sin(self._value.eval())

    def __str__(self):
        return f"(Sin({self._value}))"

class Const(AExpr):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def __str__(self):
        return f'{self._name}'

class Pi(Const):
    def eval(self) -> Number:
        return math.pi

class Euler(Const):
    def eval(self):
        return math.e

class PolyExpr(Statement):
    def __init__(self, c) -> None:
        self._coeff = c
        self._len = len(self._coeff)

    def eval(self):
        return str(self)

    def apply(self, v):
        sum = 0
        for i in range(0,self._len):
            sum += self._coeff[i].eval()*v.eval()**i
        return Litteral(sum)

    def derivate(self):
        new_coeff = []
        for i in range(1,self._len):
            try:
                new_coeff.append(Litteral(self._coeff[i].eval()*i))
            except VariableNotFound:
                new_coeff.append(MulExpr(self._coeff[i],i))
        return PolyExpr(new_coeff)

    def times(self, other):
        new_coeff = []
        for i in range(0, self._len + other._len - 1):
            new_coeff.append(0)

        for i in range(0, self._len):
            for j in range(0, other._len):
                try:
                    new_coeff[i+j] += self._coeff[i].eval() * other._coeff[j].eval()
                except VariableNotFound:
                    mult = MulExpr(self._coeff[i], other._coeff[j])
                    if type(new_coeff[i+j]) == float:
                        if new_coeff[i+j] == 0:
                            new_coeff[i+j] = mult
                        else:
                            new_coeff[i+j] = AddExpr(Litteral(new_coeff[i+j]), mult)
                    else:
                        new_coeff[i+j] = AddExpr(new_coeff[i+j], mult)



        for i in range(0, self._len + other._len - 1):
            if type(new_coeff[i]) == float:
                new_coeff[i] = Litteral(new_coeff[i])
        return PolyExpr(new_coeff)

    def __str__(self):
        s = ''
        for i in range(0,self._len):
            coeff = str(self._coeff[i])
            if coeff == '0.0':
                continue
            elif coeff != '1.0' or i == 0:
                s += f'{coeff}'

            if i != 0:
                if coeff != '1.0':
                    s += '*'
                if i==1:
                    s += 'x'
                else:
                    s += f'x^{i}'
            if i != self._len-1:
                s += ' + '
        return s

## TODO 0: define the object representing the expression (2 + (2 + 2))
##         then, define the object representing the expression ((2 + 2) + 2)

## TODO 1: implement the eval methods of the SubExpr, MulExpr and DivExpr classes

## TODO 2: perform the test at line 81, and check that it passes. Add a few more tests.

## TODO 3: add an abstract class for unary expressions,
## and one concrete subclass for "Opposites" -1 will be represented as "OppExpr(Litteral(1))"

## TODO 4: add an abstract __str__ method to AExpr and implement it
## for all concrete classes (add parentheses everywhere when it is necessary)

## TODO (Not now. Later) : add variables. What do you need to change?

if __name__ == "__main__":
    onePlusTwo = AddExpr(Litteral(1), Litteral(2))
    print(f"Hello, World {onePlusTwo.eval()}")
    todo00 = AddExpr(Litteral(3), AddExpr(Litteral(2),Litteral(5)))
    todo01 = AddExpr(AddExpr(Litteral(3),Litteral(2)), Litteral(5))
    print(f"Both should be 10 : {todo00.eval()}, {todo01.eval()}")
    e = MulExpr(AddExpr(Litteral(1),Litteral(2)),DivExpr(Litteral(2),Litteral(2)))
    print(f"value should be 3 : {e} = {e.eval()}")
    e2 = DivExpr(MulExpr(Litteral(3),AddExpr(Litteral(7), OppExpr(Litteral(2)))),AddExpr(Litteral(9), Litteral(1)))
    print(f"value should be 1.5 : {e2} = {e2.eval()}")
