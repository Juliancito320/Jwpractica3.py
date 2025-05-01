def imprimir_formulas():
    print("== FORMULAS USADAS EN LOS MÉTODOS ==")
    print("\n--- Método de Punto Fijo ---")
    print("Despejes utilizados:")
    print("1) y = -x^2 + x + 0.75")
    print("2) y = x^2 / (1 + 5x)   -> despeje de la segunda ecuación")

    print("\n--- Método de Newton-Raphson ---")
    print("El sistema se reescribe como:")
    print("f1(x, y) = y + x^2 - x - 0.75 = 0")
    print("f2(x, y) = y + 5xy - x^2 = 0")

    print("\nDerivadas parciales:")
    print("∂f1/∂x = 2x - 1")
    print("∂f1/∂y = 1")
    print("∂f2/∂x = 5y - 2x")
    print("∂f2/∂y = 1 + 5x")

    print("\nMatriz Jacobiana:")
    print("J = [[∂f1/∂x, ∂f1/∂y],")
    print("     [∂f2/∂x, ∂f2/∂y]]")

    print("\nActualización por Newton-Raphson:")
    print("[x_{n+1}]   [x_n]   [dx]")
    print("[y_{n+1}] = [y_n] + [dy]")
    print("donde [dx, dy] se obtiene de:")
    print("J * [dx, dy]^T = -[f1(x, y), f2(x, y)]^T")

imprimir_formulas()


def g1(x, y):
    return -x**2 + x + 0.75

def g2(x, y):
    return (x**2) / (1 + 5 * x)

def f1(x, y):
    return y + x**2 - x - 0.75

def f2(x, y):
    return y + 5*x*y - x**2

def df1_dx(x, y):
    return 2*x - 1

def df1_dy(x, y):
    return 1

def df2_dx(x, y):
    return 5*y - 2*x

def df2_dy(x, y):
    return 1 + 5*x

def punto_fijo(x0, y0, tol=1e-8, max_iter=100):
    print("\n== ITERACIONES PUNTO FIJO ==")
    print("{:<10} {:<15} {:<15}".format("Iter", "x", "y"))
    for i in range(max_iter):
        x_new = g2(x0, y0)
        y_new = g1(x0, y0)
        print("{:<10} {:<15.8f} {:<15.8f}".format(i+1, x_new, y_new))
        if abs(x_new - x0) < tol and abs(y_new - y0) < tol:
            print(f"\nEl metodo de punto Fijo se resolvio en {i+1} iteraciones.\n")
            return x_new, y_new
        x0, y0 = x_new, y_new
    print("Por el metodo de punto Fijo no se resolvio.\n")
    return x0, y0

def newton_raphson(x0, y0, tol=1e-8, max_iter=100):
    print("== ITERACIONES NEWTON-RAPHSON ==")
    print("{:<10} {:<15} {:<15}".format("Iter", "x", "y"))
    for i in range(max_iter):
        J11 = df1_dx(x0, y0)
        J12 = df1_dy(x0, y0)
        J21 = df2_dx(x0, y0)
        J22 = df2_dy(x0, y0)

        # Determinante
        det = J11 * J22 - J12 * J21
        if abs(det) < 1e-14:
            print("Jacobian no invertible.")
            return x0, y0

        invJ11 = J22 / det
        invJ12 = -J12 / det
        invJ21 = -J21 / det
        invJ22 = J11 / det

        # Funciones
        F1 = f1(x0, y0)
        F2 = f2(x0, y0)

        # Delta = -J^(-1) * F
        dx = - (invJ11 * F1 + invJ12 * F2)
        dy = - (invJ21 * F1 + invJ22 * F2)

        x0 += dx
        y0 += dy

        print("{:<10} {:<15.8f} {:<15.8f}".format(i+1, x0, y0))

        if abs(dx) < tol and abs(dy) < tol:
            print(f"\nEl metodo de Newton-Raphson se resolvio en {i+1} iteraciones.\n")
            return x0, y0

    print("Por el metodo de Newton-Raphson no se resolvio.\n")
    return x0, y0


x_init = 1.2
y_init = 1.2

xf, yf = punto_fijo(x_init, y_init)
xn, yn = newton_raphson(x_init, y_init)

print("\n== RESULTADOS FINALES ==")
print("Punto Fijo       -> x = {:.8f}, y = {:.8f}".format(xf, yf))
print("Newton-Raphson   -> x = {:.8f}, y = {:.8f}".format(xn, yn))
