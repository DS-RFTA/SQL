import pandas as pd
import sqlite3

# ==============================
# 1. Carregar o Excel
# ==============================
df = pd.read_excel("lead_time_resultado.xlsx")

# ==============================
# 2. Criar/abrir banco SQLite
# ==============================
con = sqlite3.connect("leadtime.db")

# ==============================
# 3. Enviar o dataframe para o banco
# ==============================
df.to_sql("lead_time", con, if_exists="replace", index=False)

# ==============================
# 4. Exemplo de consulta SQL
# ==============================
consulta = """
SELECT 
    [NF-e],
    [Data Pedido MAR],
    [Data de entrada],
    LeadTime_dias
FROM lead_time
WHERE [NF-e] = '1-000872011'
"""

resultado = pd.read_sql_query(consulta, con)

print(resultado)
