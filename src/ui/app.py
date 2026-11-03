import customtkinter as ctk
import sys
import os
import threading
import time

# Adiciona a raiz do projeto ao path para conseguir importar o core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.core.etl_processor import ETLProcessor

# Configuração visual do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LogisticsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Logistics Data Automation Platform")
        self.geometry("600x400")
        self.resizable(False, False)

        # Título
        self.lbl_title = ctk.CTkLabel(self, text="Automação de Relatórios Logísticos", font=("Arial", 20, "bold"))
        self.lbl_title.pack(pady=(20, 5))
        
        self.lbl_subtitle = ctk.CTkLabel(self, text="Consolidação de Embarque e Trânsito", font=("Arial", 12), text_color="gray")
        self.lbl_subtitle.pack(pady=(0, 20))

        # Botão de Execução
        self.btn_run = ctk.CTkButton(self, text="Executar Processamento", command=self.start_processing, width=200, height=40)
        self.btn_run.pack(pady=10)

        # Barra de Progresso
        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.pack(pady=15)
        self.progress_bar.set(0)

        # Caixa de Texto para Logs
        self.textbox = ctk.CTkTextbox(self, width=500, height=150, state="disabled")
        self.textbox.pack(pady=10)

    def log_message(self, message):
        """Adiciona mensagens à caixa de texto da interface."""
        self.textbox.configure(state="normal")
        self.textbox.insert("end", f"> {message}\n")
        self.textbox.see("end")
        self.textbox.configure(state="disabled")

    def start_processing(self):
        """Inicia a thread para não travar a interface gráfica durante o processamento."""
        self.btn_run.configure(state="disabled")
        self.progress_bar.set(0)
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        self.textbox.configure(state="disabled")
        
        # Usamos threading para a interface não congelar enquanto o Pandas roda
        thread = threading.Thread(target=self.run_etl)
        thread.start()

    def run_etl(self):
        self.log_message("Inicializando motor de ETL...")
        time.sleep(0.5) # Pausa pequena apenas para efeito visual na UI
        self.progress_bar.set(0.3)
        
        processor = ETLProcessor()
        
        self.log_message("Lendo planilhas de entrada e cruzando dados...")
        time.sleep(1) 
        self.progress_bar.set(0.6)
        
        # Executa o motor que criamos no passo anterior
        sucesso, mensagem = processor.run_pipeline()
        
        self.progress_bar.set(1.0)
        self.log_message(f"Status: {mensagem}")
        
        if sucesso:
            self.log_message("✓ Arquivo 'Base_Consolidada.xlsx' gerado em data/output/")
        
        self.btn_run.configure(state="normal")

if __name__ == "__main__":
    app = LogisticsApp()
    app.mainloop()