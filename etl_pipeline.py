import pandas as pd
import random
import time
import os

# --- MÓDULO DE "IA" SIMULADA (Transformação) ---
def mock_ai_generation(nome, foco):
    """
    Simula uma IA gerando mensagens baseadas no foco do cliente.
    """
    # Banco de frases
    templates = {
        'Investimentos': [
            f"Olá {nome}, seu futuro começa hoje. Vamos investir?",
            f"{nome}, o mercado está aquecido. Veja nossas opções de renda fixa.",
            f"Multiplique seu patrimônio com nossos fundos, {nome}."
        ],
        'Viagem': [
            f"{nome}, prepare as malas! Temos câmbio com taxas especiais.",
            f"Sua viagem dos sonhos está mais perto com nossa poupança, {nome}.",
            f"Viaje tranquilo com o seguro viagem do nosso banco, {nome}."
        ],
        'Segurança': [
            f"Proteja quem você ama, {nome}. Confira nossos seguros de vida.",
            f"{nome}, segurança digital é prioridade. Ative o 2FA no app.",
            f"Durma tranquilo, {nome}. Seu patrimônio está seguro conosco."
        ]
    }
    
    # Frases genéricas caso o foco não seja reconhecido
    genericas = [
        f"Bem-vindo ao banco digital, {nome}!",
        f"{nome}, confira as novidades no seu app hoje.",
        f"Temos ofertas especiais para você, {nome}."
    ]

    # Simula um "tempo de pensamento" da IA (latência de API)
    time.sleep(0.2) 
    
    # Lógica de seleção
    foco_normalizado = str(foco).capitalize().strip()
    opcoes = templates.get(foco_normalizado, genericas)
    
    return random.choice(opcoes)

# --- PIPELINE ETL ---

def run_etl():
    # Caminhos dos arquivos
    arquivo_entrada = 'data/clientes.csv'
    arquivo_saida = 'clientes_com_mensagens.csv'

    print(">>> [1/3] EXTRAÇÃO (Lendo dados)...")
    
    # Verificação de segurança
    if not os.path.exists(arquivo_entrada):
        arquivo_entrada = 'clientes.csv' 
        if not os.path.exists(arquivo_entrada):
            print(f"ERRO CRÍTICO: O arquivo '{arquivo_entrada}' não foi encontrado.")
            return

    try:
        df = pd.read_csv(arquivo_entrada)
        print(f"   Dados carregados: {len(df)} registros encontrados.")
    except Exception as e:
        print(f"   Erro ao ler CSV: {e}")
        return

    print("\n>>> [2/3] TRANSFORMAÇÃO (Processando via 'IA')...")
    
    try:
        df['Mensagem_Gerada'] = df.apply(
            lambda row: mock_ai_generation(row['Nome'], row['Foco']), axis=1
        )
        print("   Transformação concluída com sucesso.")
        print("   Amostra dos dados gerados:")
        print(df[['Nome', 'Foco', 'Mensagem_Gerada']].head())
    except KeyError as e:
        print(f"   Erro nas colunas do CSV. Verifique se existem as colunas 'Nome' e 'Foco'. Detalhe: {e}")
        return

    print("\n>>> [3/3] CARREGAMENTO (Salvando resultados)...")
    df.to_csv(arquivo_saida, index=False, encoding='utf-8')
    print(f"   Arquivo '{arquivo_saida}' salvo com sucesso!")
    print("\n>>> PIPELINE FINALIZADO.")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    run_etl()
