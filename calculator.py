# App que se puede usar como calculadore

def main():
    num_final = int(input('Dime un numero: '))  # Initialize with the first number
    operator = None
    
    while operator != '=':
        operator = input('Dime un operador: ')
        if operator == '=':
            break  # Exit the loop if the operator is '='
        num_añadido = int(input('Dime un numero: '))
        
        if operator == '+':
            num_final += num_añadido
        elif operator == '-':
            num_final -= num_añadido
        elif operator == '*':
            num_final *= num_añadido
        elif operator == '/':
            num_final /= num_añadido
        elif operator == '**':
            num_final **= num_añadido
        else:
            print("Escoje un operador valido entre los siguientes: '+' '-' '*' '/' '**' ")

    print(f"Resultado final: {num_final}")

if __name__ == "__main__":
    main()
