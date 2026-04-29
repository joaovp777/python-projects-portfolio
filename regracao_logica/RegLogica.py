# ============================================================
#  Calculadora de Potência — Iterativa e Recursiva
# ============================================================

def potencia_iterativa(a, b):
    """Calcula a^b de forma iterativa."""
    if b == 0:
        return 1
    resultado = 1
    for _ in range(b):
        resultado *= a
    return resultado


def potencia_recursiva(a, b):
    """Calcula a^b de forma recursiva."""
    if b == 0:
        return 1
    else:
        return a * potencia_recursiva(a, b - 1)


# ============================================================
#  Entrada do usuário
# ============================================================

def obter_inteiro(mensagem):
    """Lê e valida um número inteiro fornecido pelo usuário."""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("  [Erro] Por favor, digite um número inteiro válido.\n")


def main():
    print("=" * 50)
    print("   CALCULADORA DE POTÊNCIA (a ^ b)")
    print("=" * 50)

    a = obter_inteiro("Digite a base    (a): ")
    b = obter_inteiro("Digite o expoente (b): ")

    if b < 0:
        print("\n  [Aviso] Este programa suporta apenas expoentes >= 0.")
        return

    resultado_iter = potencia_iterativa(a, b)
    resultado_rec  = potencia_recursiva(a, b)

    print("\n" + "-" * 50)
    print(f"  Base        : {a}")
    print(f"  Expoente    : {b}")
    print("-" * 50)
    print(f"  Resultado (iterativo)  : {a}^{b} = {resultado_iter}")
    print(f"  Resultado (recursivo)  : {a}^{b} = {resultado_rec}")
    print("-" * 50)

    if resultado_iter == resultado_rec:
        print("  ✔  Ambos os métodos produziram o mesmo resultado.")
    else:
        print("  ✘  Os resultados divergem — verifique as funções.")

    print("=" * 50)


if __name__ == "__main__":
    main()