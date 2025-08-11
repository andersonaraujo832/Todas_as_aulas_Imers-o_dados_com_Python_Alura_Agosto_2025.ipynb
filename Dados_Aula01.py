##AULA1 - PALAVRA CHAVE - PANDAS
##AULA2 - PALAVRA CHAVE - PRINT
##AULA3 - PALAVRA CHAVE - MATPLOTLIB
##AULA4 - PALAVRA CHAVE -

import pandas as pd
import pip

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

df.isnull().sum()

import numpy as np

# criando dataframe de teste
df_salarios = pd.DataFrame(
    {
        "nome": ["Ana", "Bruno", "Claudio", "João"],
        "salario": [4000, np.nan, 5000, np.nan],
    }
)

# cálcula média salarial e arredonda os valores
df_salarios["salario_media"] = df_salarios["salario"].fillna(
    round(df_salarios["salario"].mean(), 2)
)

df_salarios


df_temparaturas = pd.DataFrame(
    {
        "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
        "Temperatura": [30, np.nan, np.nan, 28, 27],
    }
)

df_temparaturas["Preenchido_ffill"] = df_temparaturas["Temperatura"].ffill()
df_temparaturas

df_cidades = pd.DataFrame(
    {
        "nome": ["Ana", "Bruno", "Claudio", "João", "Junior"],
        "cidade": ["São Paulo", np.nan, "Curitiba", np.nan, "Belém"],
    }
)

df_cidades["cidade_preenchida"] = df_cidades["cidade"].fillna("Não Informado")
df_cidades

df_limpo = df.dropna()

df_limpo.isnull().sum()

df_limpo.head()

df_limpo = df_limpo.assign(ano=df_limpo["ano"].astype("int64"))
df_limpo.info()

df_limpo["senioridade"].value_counts().plot(
    kind="bar", title="Distribuição de Senioridade"
)

import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(data=df_limpo, x="senioridade", y="usd")
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x="senioridade", y="usd")
plt.title("Salario Medio por Senioridade")
plt.xlabel("Nível de Senioridade")
plt.ylabel("Salario Médio Anual")
plt.show()

ordem = df_limpo.groupby("senioridade")["usd"].mean().sort_values(ascending=False).index
ordem

plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x="senioridade", y="usd", order=ordem)
plt.title("Salario Medio por Senioridade")
plt.xlabel("Nível de Senioridade")
plt.ylabel("Salario Médio Anual")
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(df_limpo["usd"], bins=50, kde=True)
plt.title("Distribuição Salario")
plt.xlabel("Salario")
plt.ylabel("Frequencia")
plt.show()

import streamlit as st
import plotly.express as px
import pycountry


# Função para converter ISO-2 para ISO-3
def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha3
    except:
        return None


# Criar nova coluna com código ISO3-3
df_limpo["residencia_iso3"] = df_limpo["residencia"].apply(iso2_to_iso3)

# Calcular média salarial por país (ISO-3)
df_ds = df_limpo[df_limpo["cargo"] == "Data Scientist"]
media_ds_pais = df_ds.groupby("residencia_iso3")["usd"].mean().reset_index()

# Gerar o mapa
fig = px.choroleth(
    media_ds_pais,
    locations="residencia_iso3",
    color="usd",
    color_continuos_scale="rdylgn",
    title="Salário médio de Cientista de dados por país",
    labels={"usd": "Salário médio (USD)", "residencia_iso3": "País"},
)

fig.show()
