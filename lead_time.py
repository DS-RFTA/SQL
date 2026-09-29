import pandas as pd
import numpy as np

# ==============================
# 1. Ler os arquivos
# ==============================
orders = pd.read_excel("Orders.xls")
notas = pd.read_csv("relatorioAnaliticoDeNotasFiscaisCompra.csv", sep=";", encoding="latin1")

# ==============================
# 2. Normalizar e limpar os números das NF
# ==============================
# Extrair apenas os dígitos finais da NF (ex: "1-000872011" → "872011")
orders["NF_limpa"] = orders["NF-e"].astype(str).str.extract(r"(\d{5,})$")

# Mostrar linhas com NF inválida (opcional para auditoria)
nf_invalidas = orders[orders["NF_limpa"].isna()][["NF-e"]]
if not nf_invalidas.empty:
    print("\n Linhas com NF inválida detectadas no Orders.xls:")
    print(nf_invalidas)

# Remover linhas sem NF válida
orders = orders.dropna(subset=["NF_limpa"])

# Converter tipo para inteiro
orders["NF_limpa"] = orders["NF_limpa"].astype(int)
notas["Número do Documento"] = notas["Número do Documento"].astype(str).str.extract(r"(\d+)").astype(int)

# ==============================
# 3. Converter datas
# ==============================
orders["Data Pedido MAR"] = pd.to_datetime(orders["Data Pedido MAR"], dayfirst=True, errors="coerce")
notas["Data de entrada"] = pd.to_datetime(notas["Data de entrada"], dayfirst=True, errors="coerce")

# ==============================
# 4. Juntar os datasets pela NF
# ==============================
df = pd.merge(
    orders,
    notas,
    left_on="NF_limpa",
    right_on="Número do Documento",
    how="inner"
)

# ==============================
# 5. Calcular lead time em dias (corridos)
# ==============================
df["LeadTime_dias"] = (df["Data de entrada"] - df["Data Pedido MAR"]).dt.days

# ==============================
# 6. Criar dataframe final e exportar
# ==============================
df_resultado = df[[
    "NF-e",
    "Data Pedido MAR",
    "Data de entrada",
    "LeadTime_dias"
]].sort_values(by="LeadTime_dias")

# Exibir prévia
print("\n Prévia do resultado:")
print(df_resultado.head())

# Exportar para Excel
df_resultado.to_excel("lead_time_resultado.xlsx", index=False)
print("\n Arquivo 'lead_time_resultado.xlsx' gerado com sucesso.")
