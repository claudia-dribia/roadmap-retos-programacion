"""Ejercicio 10: Execpciones, corregido"""
print("Ejercicios básicos")
# Fuerza un error de división por cero
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print(e)

# Fuerza un error de índice fuera de límites
lista = []
try:
    lista[1]
except IndexError as e:
    print(e)
print()
# Dificultad extra
print("Ejercicio extra")
print()


class ErrorNumeroNegativo(Exception):
    """Error cuando el número es negativo."""

    def __init__(self, variable: str):
        self.message = f"La variable {variable} no puede ser menor que cero."
        super(ErrorNumeroNegativo, self).__init__(self.message)


def dividir_cuenta(cuenta: float, comensales: list):
    n_comensales = len(comensales)

    if n_comensales == 0:
        raise ZeroDivisionError()
    elif n_comensales < 3:
        raise IndexError()

    if cuenta < 0:
        raise ErrorNumeroNegativo("cuenta")

    cuenta_por_persona = cuenta / n_comensales
    print(f"Cada persona paga {cuenta_por_persona:.2f}€")
    print(f"Sí, tú también {comensales[2]}...")



# Ejecución normal
try:
    dividir_cuenta(50, ["María", "Ana", "Juan"])
except ZeroDivisionError as e:
    print("Error: no hay comensales")
except IndexError as e:
    print("Error: Hay menos que tres comensales. Haz tú la cuenta ;)")
except ErrorNumeroNegativo as e:
    print("Error: La cuenta no puede ser negativa")
except Exception as e:
    print("Error genérico")
    print(e)
else:
    print("Ejecución sin errores")
finally:
    print("Fin!")

