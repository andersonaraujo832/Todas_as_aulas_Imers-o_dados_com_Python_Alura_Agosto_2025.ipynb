##AULA1 - PALAVRA CHAVE - PANDAS
##AULA2 - PALAVRA CHAVE - ?
##AULA3 - PALAVRA CHAVE - ?


import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
)
df.head()
df.info()
df.describe()
df.shape
linhas, colunas = df.shape[0], df.shape[1]
print("linhas:", linhas, "colunas:", colunas)


# Dicionário de renomeação
novos_nomes = {
    "work_year": "ano",
    "experience_level": "senioridade",
    "employment_type": "contrato",
    "job_title": "cargo",
    "salary": "salario",
    "salary_currency": "moeda",
    "salary_in_usd": "usd",
    "employee_residence": "residencia",
    "remote_ratio": "remoto",
    "company_location": "empresa",
    "company_size": "tamanho_empresa",
}

# Aplicando renomeação
df.rename(columns=novos_nomes, inplace=True)

# Verificando resultado
df.head()

# O método .value_counts() serve para contar quantas vezes cada valor único aparece em uma coluna.
df["senioridade"].value_counts()

df["contrato"].value_counts()

df["remoto"].value_counts()

df["tamanho_empresa"].value_counts()

senioridade = {"SE": "senior", "MI": "pleno", "EN": "junior", "EX": "executivo"}
df["senioridade"] = df["senioridade"].replace(senioridade)
df["senioridade"].value_counts()

contrato = {"FT": "integral", "PT": "parcial", "CT": "contrato", "FL": "freelancer"}
df["contrato"] = df["contrato"].replace(contrato)
df["contrato"].value_counts()

tamanho_empresa = {"L": "grande", "S": "pequena", "M": "media"}
df["tamanho_empresa"] = df["tamanho_empresa"].replace(tamanho_empresa)
df["tamanho_empresa"].value_counts()

mapa_trabalho = {0: "presencial", 100: "remoto", 50: "hibrido"}

df["remoto"] = df["remoto"].replace(mapa_trabalho)
df["remoto"].value_counts()

df.describe(include="object")
