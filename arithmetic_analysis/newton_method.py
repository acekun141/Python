def newton(function, function1, startingInt):
    """
    Parameters
    ----------
    function : function
        function is the f(x)
    function1 : function
        function1 is the f'(x)
    startingInt: Integer

    Return
    ------
    x_n1 : number
        x_n1 is approximations root of real-valued
    """
    x_n = startingInt
    while True:
        x_n1 = x_n - (function(x_n) / function1(x_n))
        if abs(x_n - x_n1) < 10 ** -5:
            return x_n1
        x_n = x_n1


def f(x):
    return (x**3) - (2 * x) - 5


def f1(x):
    return 3 * (x**2) - 2


if __name__ == "__main__":
    print(newton(f, f1, 3))