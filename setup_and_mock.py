import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_project_structure():
    folders = [
        'data/input',
        'data/output',
        'data/archive',
        'src/core',
        'src/ui',
        'logs'
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    with open('requirements.txt', 'w') as f:
        f.write("pandas\nopenpyxl\ncustomtkinter\nnumpy\n")
    
    print("✅ Estrutura de pastas e requirements.txt criados com sucesso.")

def generate_mock_data():
    np.random.seed(42)
    num_rows = 50
    
    dates = [datetime.today() - timedelta(days=x) for x in range(10)]
    
    df_embarque = pd.DataFrame({
        'ID_Pedido': [f'PED-{1000 + i}' for i in range(num_rows)],
        'Data_Embarque': np.random.choice(dates, num_rows),
        'Filial_Origem': np.random.choice(['SP-01', 'RJ-02', 'MG-01', 'PR-03'], num_rows),
        'Status': np.random.choice(['Embarcado', 'Faturado', 'Cancelado'], num_rows, p=[0.7, 0.2, 0.1]),
        'Valor_Carga': np.round(np.random.uniform(5000, 50000, num_rows), 2)
    })
    
    df_transito = pd.DataFrame({
        'ID_Pedido': df_embarque['ID_Pedido'].sample(30).tolist() + [f'PED-{2000 + i}' for i in range(20)],
        'Transportadora': np.random.choice(['TransLog', 'Rodovias BR', 'LogExpress'], 50),
        'Data_Previsao': np.random.choice([datetime.today() + timedelta(days=x) for x in range(1, 15)], 50),
        'Ocorrencia': np.random.choice(['No Prazo', 'Atrasado', 'Retido na Fiscalização'], 50, p=[0.8, 0.15, 0.05])
    })

    df_embarque.to_excel('data/input/Relatorio_Embarques_Atual.xlsx', index=False)
    df_transito.to_excel('data/input/Controle_Transito_Diario.xlsx', index=False)
    
    print("✅ Arquivos Excel fictícios gerados na pasta 'data/input/'.")

if __name__ == "__main__":
    create_project_structure()
    generate_mock_data()