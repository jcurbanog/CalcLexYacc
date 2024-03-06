# Calculator in Lex y Yacc

This repository shows an implementation of some of the most common mathematical expressions using an specific syntax. This is possible thanks to the `ply` library that includes a Lexer and Parser implemented in Python.
This file shows examples of what you could expect to calculate.

# Use

Run the `calc.py` script.

## Arithmetic

You can perform arithmetic operations such as addition `+`, substraction `-`, multiplication, `*`, division `/`, power `^`, use parenthesis to specify priority and use the minus `-` as an unitary operator.

```
>> 1+3
4.0
>> 3*42^-5
2.2954868158255633e-08
>> -2*4^-2
-0.125
>> (4+3)*4^(30/15)
112.0
```

## Variables

You can define variables by setting a value and also use variables in your expressions. Variables must start with a lowercase letter and can be followed by any alphanumeric character, including `_` and `-`.

```
>> a = 3.4
a = 3.4
>> b = 4.2
b = 4.2
>> c = a+b
c = 7.6
>> a+b*c/2
19.36
>> e = a*b^d
"d" is not defined
>> d = 5
d = 5.0
>> e = a*b^d
e = 4443.501888000001
```

## Trigonometry

You will find the sinus function `Sin()`, and the constants $\pi$ as `Pi` and $e$ as `E`.

```
>> Sin(Pi/2)
1.0
>> E^3
20.085536923187664
```

## Polynomials

Finally, you will also be able to define polynomials and do some operations with them. In particular, symbolic multiplication `.Times()` and differenciation `.Derivate()`, as well as evaluating `.Apply()` the polynomial in a value.

```
>> m = Poly([3,1,2])
m = 3.0 + x + 2.0*x^2
>> m.Apply(3)
24.0
>> a = Poly([3,1,2]).Times(Poly([4,5])).Derivate()
a = 19.0 + 26.0*x + 30.0*x^2
>> b = Poly([3,1,2]).Times(Poly([4,5]))
b = 12.0 + 19.0*x + 13.0*x^2 + 10.0*x^3
>> a.Times(b)
228.0 + 673.0*x + 1101.0*x^2 + 1098.0*x^3 + 650.0*x^4 + 300.0*x^5
>> a.Derivate().Times(b.Derivate())
494.0 + 1816.0*x + 2340.0*x^2 + 1800.0*x^3
>> a.Derivate().Times(b.Derivate()).Apply(-1)
-782.0
```

To quit the program, type `quit`.
