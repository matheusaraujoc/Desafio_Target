try:
    def pertence_fibonacci(n):
            a, b = 0, 1
            while a <= n:
                if a == n:
                    return True
                a, b = b, a + b
            return False
        
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except:
    print("O valor que você digitou não é válido")