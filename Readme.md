# Calculator in Lex and Yacc

This repository shows an implementation of some of the most common mathematical expressions using an specific syntax. This is possible thanks to the `ply` library that includes a Lexer and Parser implemented in Python.
This file shows examples of what you could expect to calculate.

## Use

Run the `calc.py` script and start using the prompt input.
To quit the program, type `quit`.

## Arithmetic

You can perform arithmetic operations such as addition `+`, substraction `-`, multiplication `*`, division `/`, power `^`, use parenthesis to specify priority and use the minus `-` as an unitary operator.

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

You can even pass expressions as coefficients. For instance, you could pass a `j` variable even if it is not defined. You will still be able to perform `.Derivate()` and `.Times()`. However, if you want to `.Apply()` a value, you would be required to set a value to your symbolic variable.

```
>> j
"j" is not defined
>> my_poly = Poly([1,3+4,0,j])
my_poly = 1.0 + (3.0 + 4.0)*x + j*x^3
>> my_poly.Derivate()
7.0 + (j * 3)*x^2
>> my_poly.Derivate().Apply(-1)
"j" is not defined
>> my_poly.Times(Poly([0,0,2]))
2.0*x^2 + (14.0 + (j * 0.0))*x^3 + (j * 0.0)*x^4 + (0 + (j * 2.0))*x^5
>> my_poly.Times(Poly([0,0,2])).Apply(-1)
"j" is not defined
>> j=-3
j = -3.0
>> my_poly.Derivate().Apply(-1)
-2.0
>> my_poly.Times(Poly([0,0,2])).Apply(-1)
-6.0
```

## Future work

There is space for plenty of improvements. Among which:

- Include more trigonometrical functions such as `Cos`, `Tan` and their inverses/hyperbolic functions.
- Perform addition, substraction, and euclidian division between polynomials
- Simplify terms after a symbolic operation.
- Develop a CLI where more commands would be available: be able to repeat the previous input by tapping up-arrow, use the lateral arrows to naviagte between the input, clean the command window, delete a variable from the memory, delete all variables, etc.
