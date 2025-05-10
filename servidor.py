import threading
import hprose

# Dicionário compartilhado
dicionario = {}

# Mutex para proteger o dicionário
mutex = threading.Lock()

# Funções do servidor
class Dicionario:
    def update(self, chave, valor):
        with mutex:
            if chave not in dicionario:
                dicionario[chave] = valor
                return True
            else:
                dicionario[chave] = valor
                return False

    def remove(self, chave):
        with mutex:
            if chave in dicionario:
                del dicionario[chave]
                return True
            else:
                return False

    def get(self, chave):
        with mutex:
            return dicionario.get(chave, -1)

# Inicializando o servidor em uma thread
def start_server():
    print("Iniciando servidor...")
    server = hprose.HttpServer(port=8080)
    server.add(Dicionario(), "Dicionario")
    server.start()  # Este método bloqueia o fluxo

def run_server():
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    print("Servidor iniciado na porta 8080...")

if __name__ == "__main__":
    run_server()
    # Manter o programa principal ativo
    input("Pressione Enter para encerrar o servidor...\n")
