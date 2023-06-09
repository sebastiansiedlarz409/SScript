from lexer.sslexer import *
from misc.exceptions import *
from parser.ssparser import *
from runtime.ssscope import *
from runtime.ssruntime import *

def execute(source, db = False):
    lexer = SSLexer()
    parser = SSParser()
    runtime = SSRuntime()

    tokens = lexer.tokenize(source)
    if db == True:
        for t in tokens: print(t)

    program = parser.parseProgram(tokens)
    if db == True:
        print(program)

    globalScope = SSRuntimeScope()
    result = runtime.execute(program, globalScope)
    if db == True:
        print(result)

    return str(result)

def t1():
    s = ""
    with open("tests\\t1.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "0":
            print("T1 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T1 NOT OK")

def t2():
    s = ""
    with open("tests\\t2.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "false":
            print("T2 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T2 NOT OK")

def t3():
    s = ""
    with open("tests\\t3.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "EBAtrue99":
            print("T3 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T3 NOT OK")

def t4():
    s = ""
    with open("tests\\t4.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "true":
            print("T4 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T4 NOT OK")

def t5():
    s = ""
    with open("tests\\t5.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "100":
            print("T5 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T5 NOT OK")

def t6():
    s = ""
    with open("tests\\t6.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "512":
            print("T6 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T6 NOT OK")

def t7():
    s = ""
    with open("tests\\t7.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "10":
            print("T7 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T7 NOT OK")

def t8():
    s = ""
    with open("tests\\t8.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "false":
            print("T8 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T8 NOT OK")

def t9():
    s = ""
    with open("tests\\t9.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "false":
            print("T9 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T9 NOT OK")

def t10():
    s = ""
    with open("tests\\t10.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "-9":
            print("T10 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T10 NOT OK")

def t11():
    s = ""
    with open("tests\\t11.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "2":
            print("T11 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T11 NOT OK")

def t12():
    s = ""
    with open("tests\\t12.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "-1":
            print("T12 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T12 NOT OK")

def t13():
    s = ""
    with open("tests\\t13.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "null":
            print("T13 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T13 NOT OK")

def t14():
    s = ""
    with open("tests\\t14.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "4":
            print("T14 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T14 NOT OK")

def t15():
    s = ""
    with open("tests\\t15.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "255":
            print("T15 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T15 NOT OK")

def t16():
    s = ""
    with open("tests\\t16.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "20":
            print("T16 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T16 NOT OK")

def t17():
    s = ""
    with open("tests\\t17.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "40":
            print("T17 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T17 NOT OK")

def t18():
    s = ""
    with open("tests\\t18.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "1":
            print("T18 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T18 NOT OK")

def t19():
    s = ""
    with open("tests\\t19.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "3":
            print("T19 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T19 NOT OK")

def t20():
    s = ""
    with open("tests\\t20.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T20 NOT OK")
        return
    except SSLexerException as x:
        if x.got == '`' and x.line == 2 and x.column == 1:
            print("T20 OK")
        else:
            print("T20 NOT OK")
            print(x)

def t21():
    s = ""
    with open("tests\\t21.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T21 NOT OK")
        return
    except SSLexerException as x:
        if x.got == '.' and x.line == 1 and x.column == 12:
            print("T21 OK")
        else:
            print("T21 NOT OK")
            print(x)

def t22():
    s = ""
    with open("tests\\t22.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T22 NOT OK")
        return
    except SSLexerException as x:
        if x.got == '~' and x.line == 1 and x.column == 42:
            print("T22 OK")
        else:
            print("T22 NOT OK")
            print(x)

def t23():
    s = ""
    with open("tests\\t23.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T23 NOT OK")
        return
    except SSParserException as x:
        if x.got.type == SSTokens.NumberToken and x.got.line == 1 and x.got.column == 16:
            print("T23 OK")
        else:
            print("T23 NOT OK")
            print(x)

def t24():
    s = ""
    with open("tests\\t24.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T24 NOT OK")
        return
    except SSParserException as x:
        if x.expected == SSTokens.IdentifierToken and x.got.line == 1 and x.got.column == 6:
            print("T24 OK")
        else:
            print("T24 NOT OK")
            print(x)

def t25():
    s = ""
    with open("tests\\t25.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T25 NOT OK")
        return
    except SSParserException as x:
        if x.expected == SSTokens.SemicolonToken and x.got.line == 3 and x.got.column == 23:
            print("T25 OK")
        else:
            print("T25 NOT OK")
            print(x)

def t26():
    s = ""
    with open("tests\\t26.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T26 NOT OK")
        return
    except SSParserUnexpectedException as x:
        if x.got.value == "=" and x.got.line == 3 and x.got.column == 5:
            print("T26 OK")
        else:
            print("T26 NOT OK")
            print(x)

def t30():
    s = ""
    with open("tests\\t30.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "13":
            print("T30 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T30 NOT OK")

def t31():
    s = ""
    with open("tests\\t31.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "0":
            print("T31 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T31 NOT OK")

def t32():
    s = ""
    with open("tests\\t32.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "3":
            print("T32 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T32 NOT OK")

def t33():
    s = ""
    with open("tests\\t33.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "3":
            print("T33 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T33 NOT OK")

def t34():
    s = ""
    with open("tests\\t34.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "0":
            print("T34 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T34 NOT OK")

def t35():
    s = ""
    with open("tests\\t35.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "2":
            print("T35 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T35 NOT OK")

def t36():
    s = ""
    with open("tests\\t36.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "10":
            print("T36 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T36 NOT OK")

def t37():
    s = ""
    with open("tests\\t37.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "3":
            print("T37 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T37 NOT OK")

def t38():
    s = ""
    with open("tests\\t38.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T38 NOT OK")
        return
    except SSException as x:
        print("T38 OK")

def t39():
    s = ""
    with open("tests\\t39.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        if result == "88":
            print("T39 OK")
            return
    except Exception as x:
        print(x)

    result = execute(s, True)
    print("T39 NOT OK")

def t40():
    s = ""
    with open("tests\\t40.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T40 NOT OK")
        return
    except SSException as x:
        print("T40 OK")

def t41():
    s = ""
    with open("tests\\t41.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T41 NOT OK")
        return
    except SSException as x:
        print("T41 OK")

def t42():
    s = ""
    with open("tests\\t42.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T42 NOT OK")
        return
    except SSException as x:
        print("T42 OK")

def t43():
    s = ""
    with open("tests\\t43.ss", "r") as f:
        s = f.read()

    try:
        result = execute(s)
        print("T43 NOT OK")
        return
    except SSException as x:
        print("T43 OK")

print()
print("TEST TEST TEST")

tests = list(filter(lambda x: str(x).startswith("t"), dir()))
tests.sort(key = lambda x: int(x[1:]))
for t in tests:
    globals()[t]()