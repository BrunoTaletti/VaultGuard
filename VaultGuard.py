import os
import subprocess
from datetime import datetime

def main():
    # Defina o caminho para a pasta do Obsidian
    
    # Caso esteja usando MacOS, retire o comentário (#) da linha abaixo.
    # folder_path = r"~/Users/seu_usuario_mac/Documents/nome_da_pasta_vault"
	
    # Caso esteja usando Windows, retire o comentário (#) da linha abaixo
    # folder_path = r"C:\Users\seu_usuario_windows\documents\nome_da_pasta_vault"
    
    # Mude para o diretório especificado
    os.chdir(folder_path)

    # Verifica se há alterações no repositório Git
    result = subprocess.run(["git", "status", "--porcelain"], stdout=subprocess.PIPE, text=True)
    if not result.stdout.strip():
        print("Nenhuma alteração encontrada. Fechando...")
        return  # Fecha o script se não houver alterações

    # Executa os comandos Git
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "status"], check=True)
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Formato dd/mm/aaaa hh:mm:ss
        commit_message = f"Daily backup: {current_time}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Backup concluído com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar um comando Git: {e}")
        return

if __name__ == "__main__":
    main()