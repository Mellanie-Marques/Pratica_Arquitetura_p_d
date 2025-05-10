# Conectando ao servidor
import hprose
import time

client = hprose.HttpClient("http://localhost:8080/")

# Usando os métodos remotos
def cliente():
    # Saída original
    print("Execução com saída original:")
    time.sleep(1)
    print(client.Dicionario.update("chave1", 10))  # True (primeira vez)
    time.sleep(1)
    print(client.Dicionario.update("chave1", 20))  # False (já existia)
    time.sleep(1)
    print(client.Dicionario.get("chave1"))         # 20
    time.sleep(1)
    print(client.Dicionario.remove("chave1"))      # True
    time.sleep(1)
    print(client.Dicionario.get("chave1"))         # -1

    # Pausa entre as duas execuções
    print("\n" + "-" * 30 + "\n")
    time.sleep(2)

    # Saída formatada
    print("Execução com saída formatada:")
    time.sleep(1)
    print("1. Adicionando a chave 'chave1' com o valor 10...")
    resultado = client.Dicionario.update("chave1", 10)
    print(f"   Resultado: {'Sucesso (a chave foi adicionada)' if resultado else 'Erro'}\n")
    time.sleep(1)

    print("2. Atualizando a chave 'chave1' para o valor 20...")
    resultado = client.Dicionario.update("chave1", 20)
    print(f"   Resultado: {'Sucesso, mas a chave já existia (valor atualizado)' if not resultado else 'Erro'}\n")
    time.sleep(1)

    print("3. Recuperando o valor da chave 'chave1'...")
    valor = client.Dicionario.get("chave1")
    print(f"   Valor: {valor}\n")
    time.sleep(1)

    print("4. Removendo a chave 'chave1'...")
    resultado = client.Dicionario.remove("chave1")
    print(f"   Resultado: {'Sucesso (a chave foi removida)' if resultado else 'Erro (chave não encontrada)'}\n")
    time.sleep(1)

    print("5. Recuperando o valor da chave 'chave1' novamente...")
    valor = client.Dicionario.get("chave1")
    print(f"   Resultado: {'A chave não existe mais no dicionário' if valor == -1 else f'Valor: {valor}'}\n")

if __name__ == "__main__":
    cliente()
