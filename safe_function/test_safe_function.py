import unittest
import nose

import safe_function.safe_function
from safe_function import safe_function as sf


@sf.safe_function
def fun1(a: int, b: int, c: int) -> int:
    print("funcion ejecutada fun1 ")
    return a + b + c


@sf.safe_function
def fun2(*args: (int, str)) -> int:
    print("funcion ejecutada fun2 ")
    return len(args)


@sf.safe_function
def fun3(a: str, b: (str, int) = "papa", *sasa: (int, str)) -> int:
    print("funcion ejecutada fun3")
    if type(b) is str:
        return len(a) + len(sasa) + len(b)
    else:
        return len(a) + len(sasa) + b


@sf.safe_function
class MyClass:
    pass


class ProjectSafeFunctionTestCases(unittest.TestCase):

    def test_simple_fun_varOk(self):
        res = fun1(1, 1, 1)
        exp = 3
        self.assertEquals(res, exp)

    def test_simple_fun_varTypeerror(self):
        # la funcion no se ejecuta por tener un parametro no soportado
        res = fun1(1, 1, "p")
        exp = None
        self.assertEquals(res, exp)

    def test_simple_fun_varIncomplete(self):
        # la funcion no se ejecuta por tener faltarle parametro obligatorio
        res = fun1(1, 1)
        exp = None
        self.assertEquals(res, exp)
    def test_simple_fun_varNo(self):

        res = fun1()
        exp = None
        self.assertEquals(res, exp)

    def test_arguments_fun_varOk(self):
        res = fun2(2, 3, 4, 5, 6, "ret")
        exp = 6
        self.assertEquals(res, exp)

    def test_arguments_fun_varTypeerror(self):
        res = fun2(2, 3, (3, 4, 5), 5, 6, "ret")
        exp = None
        self.assertEquals(res, exp)

    def test_arguments_fun_varNo(self):
        res = fun2()
        exp = 0
        self.assertEquals(res, exp)

    def test_complete_fun_varOk(self):
        res = fun3("2", 3, 4, 5, 6, "ret")
        exp = 8
        self.assertEquals(res, exp)

    def test_complete_fun_varTypeerror(self):
        res = fun3(2, 3, (3, 4, 5), 5, 6, "ret")
        exp = None
        self.assertEquals(res, exp)

    def test_complete_fun_varNo(self):
        res = fun3()
        exp = None
        self.assertEquals(res, exp)

    def test_simple_Nofun(self):
        try:
            res = MyClass()
        except TypeError as qq:
            res = qq.args[0]
        exp = "SOLO USAR UNA FUNCION CON ESTE DECORADOR"
        self.assertEquals(res, exp)


if __name__ == '__main__':
    nose.run(defaultTest=__name__)
