import pandas as pd
import logging
import os
from datetime import datetime


class ETLProcessor:
    def __init__(
        self, input_dir="data/input", output_dir="data/output", log_dir="logs"
    ):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.log_dir = log_dir
        self._setup_logging()

    def _setup_logging(self):
        """Configura o sistema de logs para registrar as atividades do pipeline."""
        log_filename = os.path.join(
            self.log_dir, f"etl_log_{datetime.now().strftime('%Y%m%d')}.txt"
        )
        logging.basicConfig(
            filename=log_filename,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        self.logger = logging.getLogger(__name__)

    def run_pipeline(self):
        """Executa as etapas de Extração, Transformação e Carga (ETL)."""
        self.logger.info("Iniciando pipeline de processamento logístico.")
        try:
            # 1. EXTRAÇÃO (Extract)
            df_embarque = pd.read_excel(
                os.path.join(self.input_dir, "Relatorio_Embarques_Atual.xlsx")
            )
            df_transito = pd.read_excel(
                os.path.join(self.input_dir, "Controle_Transito_Diario.xlsx")
            )
            self.logger.info("Arquivos carregados com sucesso da pasta input.")

            # 2. TRANSFORMAÇÃO E REGRAS DE NEGÓCIO (Transform)
            # Regra de Negócio 1: Remover pedidos com status 'Cancelado'
            qtd_antes = len(df_embarque)
            df_embarque = df_embarque[df_embarque["Status"] != "Cancelado"]
            self.logger.info(
                f"Regra 1 (Filtro): {qtd_antes - len(df_embarque)} pedidos cancelados removidos da base."
            )

            # Regra de Negócio 2: Consolidação de Dados (Merge/VPROCV)
            df_consolidado = pd.merge(
                df_embarque, df_transito, on="ID_Pedido", how="left"
            )

            # Regra de Negócio 3: Tratamento de Nulos pós-cruzamento
            df_consolidado["Transportadora"] = df_consolidado["Transportadora"].fillna(
                "Sem Transportadora Atribuída"
            )
            df_consolidado["Ocorrencia"] = df_consolidado["Ocorrencia"].fillna(
                "Aguardando Atualização"
            )

            self.logger.info(
                "Transformação concluída: bases cruzadas e valores nulos tratados."
            )

            # 3. CARGA (Load)
            output_path = os.path.join(self.output_dir, "Base_Consolidada.xlsx")
            df_consolidado.to_excel(output_path, index=False)
            self.logger.info(f"Arquivo final exportado com sucesso para: {output_path}")

            return True, "Processamento ETL concluído com sucesso!"

        except Exception as e:
            self.logger.error(f"Erro Crítico durante o processamento: {str(e)}")
            return False, f"Erro no processamento: {str(e)}"


# Bloco de execução direta para testes no terminal
if __name__ == "__main__":
    processor = ETLProcessor()
    sucesso, mensagem = processor.run_pipeline()
    print(mensagem)
