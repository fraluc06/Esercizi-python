import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import xml.etree.ElementTree as ET
import json
from datetime import datetime
import numpy as np

class DataAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizzatore Vendite")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)

        # Per cambiare l'icona dell'applicazione, decommentare questa riga
        # self.root.iconbitmap('percorso/alla/tua/icona.ico')

        self.df = None
        self.file_path = None
        self.selected_year = None
        self.search_term = None
        self.selected_color = None

        # Frame principale
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame per i controlli
        self.controls_frame = ttk.LabelFrame(self.main_frame, text="Parametri di ricerca", padding="10")
        self.controls_frame.pack(fill=tk.X, padx=5, pady=5)

        # Selezione file
        ttk.Label(self.controls_frame, text="File dati:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.file_path_var = tk.StringVar()
        ttk.Entry(self.controls_frame, textvariable=self.file_path_var, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.controls_frame, text="Sfoglia...", command=self.browse_file).grid(row=0, column=2, padx=5, pady=5)

        # Campo per cosa cercare
        ttk.Label(self.controls_frame, text="Articolo da cercare:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.search_var = tk.StringVar(value="VZ1516")
        ttk.Entry(self.controls_frame, textvariable=self.search_var, width=20).grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Campo per colore
        ttk.Label(self.controls_frame, text="Colore (opzionale):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.color_var = tk.StringVar()
        ttk.Entry(self.controls_frame, textvariable=self.color_var, width=20).grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.controls_frame, text="Lascia vuoto per tutti i colori").grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

        # Selezione anno
        ttk.Label(self.controls_frame, text="Anno:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.year_var = tk.StringVar(value="2023")
        self.year_entry = ttk.Entry(self.controls_frame, textvariable=self.year_var, width=10)
        self.year_entry.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        # Frame per i pulsanti
        buttons_frame = ttk.Frame(self.controls_frame)
        buttons_frame.grid(row=4, column=1, pady=10, sticky=tk.W)

        # Pulsante analizza
        ttk.Button(buttons_frame, text="Analizza", command=self.analyze_data).pack(side=tk.LEFT, padx=5)

        # Pulsante per analisi per colore
        ttk.Button(buttons_frame, text="Analisi per Colore", command=self.analyze_by_color).pack(side=tk.LEFT, padx=5)

        # Pulsante esci
        ttk.Button(buttons_frame, text="Esci", command=self.exit_app).pack(side=tk.LEFT, padx=5)

        # Frame per i risultati
        self.results_frame = ttk.LabelFrame(self.main_frame, text="Risultati", padding="10")
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Frame per la tabella
        self.table_frame = ttk.Frame(self.results_frame)
        self.table_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Frame per il grafico
        self.chart_frame = ttk.Frame(self.results_frame)
        self.chart_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Statusbar
        self.status_var = tk.StringVar(value="Pronto")
        self.statusbar = ttk.Label(self.main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=2)

    def exit_app(self):
        """Funzione per uscire dall'applicazione con conferma"""
        if messagebox.askokcancel("Esci", "Sei sicuro di voler uscire?"):
            self.root.destroy()

    def browse_file(self):
        filetypes = (
            ('Excel files', '*.xlsx *.xls'),
            ('CSV files', '*.csv'),
            ('XML files', '*.xml'),
            ('JSON files', '*.json'),
            ('All files', '*.*')
        )

        filename = filedialog.askopenfilename(
            title='Seleziona un file',
            filetypes=filetypes)

        if filename:
            self.file_path_var.set(filename)

    def load_data(self):
        self.file_path = self.file_path_var.get()

        if not self.file_path or not os.path.exists(self.file_path):
            messagebox.showerror("Errore", "Seleziona un file valido.")
            return False

        try:
            extension = os.path.splitext(self.file_path)[1].lower()

            if extension in ['.xlsx', '.xls']:
                self.df = pd.read_excel(self.file_path)
            elif extension == '.csv':
                # Tenta di aprire il CSV con vari separatori
                try:
                    self.df = pd.read_csv(self.file_path, sep=None, engine='python')
                except:
                    try:
                        self.df = pd.read_csv(self.file_path, sep=',')
                    except:
                        try:
                            self.df = pd.read_csv(self.file_path, sep=';')
                        except:
                            self.df = pd.read_csv(self.file_path, sep='\t')
            elif extension == '.xml':
                # Gestione file XML migliorata
                tree = ET.parse(self.file_path)
                root = tree.getroot()
                data = []

                # Tenta di trovare elementi per dati di vendita (adatta in base alla struttura XML)
                # Diverse strutture possibili
                elem_paths = [
                    './row', './sale', './order', './orderline', './/item',
                    './sales/sale', './orders/order', './data/row'
                ]

                items = []
                for path in elem_paths:
                    items = root.findall(path)
                    if items:
                        break

                if not items:
                    # Se non trova con i percorsi predefiniti, cerca elementi che potrebbero contenere i dati
                    for elem in root.iter():
                        if len(list(elem)) > 0 and all(child.text is not None for child in elem):
                            items.append(elem)

                for item in items:
                    row = {}
                    for child in item:
                        row[child.tag.upper()] = child.text
                    if row:  # Aggiungi solo se ha elementi
                        data.append(row)

                if not data:
                    messagebox.showerror("Errore", "Impossibile estrarre dati dal file XML. Formato non riconosciuto.")
                    return False

                self.df = pd.DataFrame(data)
            elif extension == '.json':
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Gestisci diversi formati JSON
                if isinstance(data, list):
                    self.df = pd.DataFrame(data)
                elif isinstance(data, dict):
                    if 'data' in data and isinstance(data['data'], list):
                        self.df = pd.DataFrame(data['data'])
                    elif 'orders' in data and isinstance(data['orders'], list):
                        self.df = pd.DataFrame(data['orders'])
                    elif 'items' in data and isinstance(data['items'], list):
                        self.df = pd.DataFrame(data['items'])
                    else:
                        # Tenta di appiattire un JSON annidato
                        flat_data = []
                        for key, value in data.items():
                            if isinstance(value, dict):
                                flat_data.append(value)
                        if flat_data:
                            self.df = pd.DataFrame(flat_data)
                        else:
                            # Ultimo tentativo: una singola riga
                            self.df = pd.DataFrame([data])
            else:
                messagebox.showerror("Errore", "Formato file non supportato.")
                return False

            # Normalizzazione delle colonne (rende i nomi delle colonne tutti maiuscoli)
            self.df.columns = [col.upper() if isinstance(col, str) else col for col in self.df.columns]

            # Mapping dei nomi delle colonne per gestire diversi standard di naming
            column_mappings = {
                'DATAORDINE': ['DATAORDINE', 'DATA', 'DATE', 'ORDER_DATE', 'ORDERDATE', 'DATA_ORDINE'],
                'ARTICOLO': ['ARTICOLO', 'CODICE', 'ARTICLE', 'PRODUCT', 'ITEM', 'SKU', 'CODE', 'CODICE_ARTICOLO'],
                'QUANTITA': ['QUANTITA', 'QTA', 'QUANTITY', 'QTY', 'AMOUNT', 'TOTAL'],
                'COLORE': ['COLORE', 'COLOR', 'COLOUR', 'VARIANTE', 'VARIANT', 'VARIAZIONE', 'COLORAZIONE']
            }

            # Rinomina le colonne secondo il mapping
            for target_col, possible_names in column_mappings.items():
                if target_col not in self.df.columns:
                    for col_name in self.df.columns:
                        if col_name in possible_names:
                            self.df.rename(columns={col_name: target_col}, inplace=True)
                            break

            # Verifica colonne necessarie
            required_columns = ['DATAORDINE', 'ARTICOLO', 'QUANTITA']
            missing_columns = [col for col in required_columns if col not in self.df.columns]

            if missing_columns:
                messagebox.showerror("Errore", f"Colonne mancanti nel file: {', '.join(missing_columns)}")
                return False

            # Se non c'è la colonna COLORE, creala vuota
            if 'COLORE' not in self.df.columns:
                self.df['COLORE'] = 'N/D'  # Non disponibile
                messagebox.showinfo("Informazione", "Colonna COLORE non trovata nel file. Creata colonna vuota.")

            return True

        except Exception as e:
            messagebox.showerror("Errore", f"Errore nel caricamento del file: {str(e)}")
            return False

    def analyze_data(self):
        """Analisi standard per mese"""
        # Pulisci i frame precedenti
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        if not self.load_data():
            return

        self.search_term = self.search_var.get().strip().upper()
        self.selected_color = self.color_var.get().strip().upper()

        try:
            self.selected_year = int(self.year_var.get())
        except ValueError:
            messagebox.showerror("Errore", "Anno non valido. Inserisci un numero intero.")
            return

        self.status_var.set(f"Analisi in corso per {self.search_term}" +
                            (f" (colore: {self.selected_color})" if self.selected_color else "") +
                            f" nell'anno {self.selected_year}...")
        self.root.update()

        try:
            # Converti la colonna DataOrdine in formato datetime se non lo è già
            self.df['DATAORDINE'] = pd.to_datetime(self.df['DATAORDINE'], errors='coerce')

            # Filtra per l'anno desiderato e per il prodotto scelto
            df_filtrato = self.df[(self.df['DATAORDINE'].dt.year == self.selected_year) &
                                  (self.df['ARTICOLO'].str.upper() == self.search_term)]

            # Se è specificato un colore, filtriamo anche per quello
            if self.selected_color:
                df_filtrato = df_filtrato[df_filtrato['COLORE'].str.upper() == self.selected_color]

            if df_filtrato.empty:
                message = f"Nessun dato trovato per {self.search_term}"
                if self.selected_color:
                    message += f" con colore {self.selected_color}"
                message += f" nell'anno {self.selected_year}"
                messagebox.showinfo("Informazione", message)
                return

            # Estrai il numero del mese e mappa ai nomi in italiano
            mesi_italiani = {
                1: 'Gennaio', 2: 'Febbraio', 3: 'Marzo', 4: 'Aprile',
                5: 'Maggio', 6: 'Giugno', 7: 'Luglio', 8: 'Agosto',
                9: 'Settembre', 10: 'Ottobre', 11: 'Novembre', 12: 'Dicembre'
            }

            df_filtrato['Mese'] = df_filtrato['DATAORDINE'].dt.month
            df_filtrato['NomeMese'] = df_filtrato['Mese'].map(mesi_italiani)

            # Raggruppa per nome del mese e somma le quantità
            tabella = df_filtrato.groupby('NomeMese')['QUANTITA'].sum().reset_index()

            # Riordina i mesi secondo l'ordine cronologico
            ordine_mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno',
                           'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
            tabella['Ordine'] = tabella['NomeMese'].apply(lambda x: ordine_mesi.index(x))
            tabella = tabella.sort_values('Ordine').drop(columns='Ordine')

            # Aggiungi la riga con il totale
            totale = tabella['QUANTITA'].sum()
            riga_totale = pd.DataFrame({'NomeMese': ['Totale'], 'QUANTITA': [totale]})
            tabella_finale = pd.concat([tabella, riga_totale], ignore_index=True)

            # Mostra la tabella nella GUI
            self.display_table(tabella_finale)

            # Crea e mostra il grafico
            title = f"Vendite di {self.search_term}"
            if self.selected_color:
                title += f" (colore: {self.selected_color})"
            title += f" nell'anno {self.selected_year}"

            self.display_chart(tabella, title)

            self.status_var.set(f"Analisi completata per {self.search_term}" +
                                (f" (colore: {self.selected_color})" if self.selected_color else "") +
                                f" nell'anno {self.selected_year}")

        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante l'analisi: {str(e)}")
            self.status_var.set("Si è verificato un errore durante l'analisi")

    def analyze_by_color(self):
        """Analisi per colore dell'articolo"""
        # Pulisci i frame precedenti
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        if not self.load_data():
            return

        self.search_term = self.search_var.get().strip().upper()

        try:
            self.selected_year = int(self.year_var.get())
        except ValueError:
            messagebox.showerror("Errore", "Anno non valido. Inserisci un numero intero.")
            return

        self.status_var.set(f"Analisi per colore in corso per {self.search_term} nell'anno {self.selected_year}...")
        self.root.update()

        try:
            # Converti la colonna DataOrdine in formato datetime se non lo è già
            self.df['DATAORDINE'] = pd.to_datetime(self.df['DATAORDINE'], errors='coerce')

            # Filtra per l'anno desiderato e per il prodotto scelto
            df_filtrato = self.df[(self.df['DATAORDINE'].dt.year == self.selected_year) &
                                  (self.df['ARTICOLO'].str.upper() == self.search_term)]

            if df_filtrato.empty:
                messagebox.showinfo("Informazione", f"Nessun dato trovato per {self.search_term} nell'anno {self.selected_year}")
                return

            # Raggruppa per colore e somma le quantità
            tabella_colori = df_filtrato.groupby('COLORE')['QUANTITA'].sum().reset_index()

            # Ordina per quantità decrescente
            tabella_colori = tabella_colori.sort_values('QUANTITA', ascending=False)

            # Aggiungi la riga con il totale
            totale = tabella_colori['QUANTITA'].sum()
            riga_totale = pd.DataFrame({'COLORE': ['TOTALE'], 'QUANTITA': [totale]})
            tabella_finale = pd.concat([tabella_colori, riga_totale], ignore_index=True)

            # Mostra la tabella nella GUI
            self.display_table(tabella_finale)

            # Crea e mostra il grafico a torta per i colori
            self.display_pie_chart(tabella_colori)

            self.status_var.set(f"Analisi per colore completata per {self.search_term} nell'anno {self.selected_year}")

        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante l'analisi per colore: {str(e)}")
            self.status_var.set("Si è verificato un errore durante l'analisi per colore")

    def display_table(self, df):
        # Crea una tabella con Treeview
        columns = list(df.columns)
        tree = ttk.Treeview(self.table_frame, columns=columns, show='headings')

        # Aggiungi le intestazioni
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        # Aggiungi le righe
        for i, row in df.iterrows():
            values = row.values.tolist()
            tree.insert('', tk.END, values=values)

        # Aggiungi scrollbar
        scrollbar = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def display_chart(self, df, title):
        # Crea la figura
        fig, ax = plt.subplots(figsize=(5, 4))

        # Crea un grafico a barre
        bars = ax.bar(df['NomeMese'], df['QUANTITA'], color='skyblue')

        # Aggiungi etichette alle barre
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height:.0f}', ha='center', va='bottom')

        # Titolo e label
        ax.set_title(title)
        ax.set_xlabel('Mese')
        ax.set_ylabel('Quantità')

        # Ruota le etichette dell'asse x
        plt.xticks(rotation=45)

        plt.tight_layout()

        # Aggiungi il grafico alla GUI
        canvas = FigureCanvasTkAgg(fig, self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def display_pie_chart(self, df):
        # Se ci sono più di 10 colori, mostra solo i primi 9 più significativi e raggruppa gli altri
        if len(df) > 10:
            top_df = df.head(9)
            other_total = df.iloc[9:]['QUANTITA'].sum()
            other_row = pd.DataFrame({'COLORE': ['Altri'], 'QUANTITA': [other_total]})
            plot_df = pd.concat([top_df, other_row], ignore_index=True)
        else:
            plot_df = df.copy()

        # Crea la figura
        fig, ax = plt.subplots(figsize=(6, 5))

        # Aggiungi titolo
        ax.set_title(f"Distribuzione per colore di {self.search_term} nell'anno {self.selected_year}")

        # Crea etichette con percentuali
        labels = [f"{row['COLORE']} ({row['QUANTITA']} - {row['QUANTITA']/df['QUANTITA'].sum()*100:.1f}%)"
                  for _, row in plot_df.iterrows()]

        # Crea il grafico a torta
        wedges, texts = ax.pie(plot_df['QUANTITA'],
                               wedgeprops=dict(width=0.5),
                               startangle=90)

        # Crea legenda
        ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        plt.tight_layout()

        # Aggiungi il grafico alla GUI
        canvas = FigureCanvasTkAgg(fig, self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()
