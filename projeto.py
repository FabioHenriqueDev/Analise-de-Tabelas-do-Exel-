import pandas as pd

# Importação de modulos e arquivos
servicos_prestados_df = pd.read_excel(r'BaseServiçosPrestados.xlsx')
cadastro_clientes_df = pd.read_csv(r'CadastroClientes.csv', sep=';', decimal=',')
cadastro_funcionarios_df = pd.read_csv(r'CadastroFuncionarios.csv', sep=';', decimal=',')

#retirando colunas Estado Civil e Cargo da tabela Funcionários
cadastro_funcionarios_df = cadastro_funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)



# Configurações para exibir todas as colunas e maior largura no terminal
pd.set_option('display.max_columns', None)  # Exibe todas as colunas
pd.set_option('display.width', 200)        # Define a largura total para visualização (ajuste conforme necessário)
pd.set_option('display.expand_frame_repr', False)  # Evita quebra de linha na visualização do DataFrame



print()
print()


#1. Qual foi o gasto total com salários de funcionários pela empresa?
cadastro_funcionarios_df['Salário Total'] = cadastro_funcionarios_df['Salario Base'] + cadastro_funcionarios_df['Impostos'] + cadastro_funcionarios_df['Beneficios'] + cadastro_funcionarios_df['VT'] + cadastro_funcionarios_df['VR']
print(cadastro_funcionarios_df.head())

print()
print()

soma_funcioarios_total = cadastro_funcionarios_df['Salário Total'].sum()
print(f'Gasto total de Funcionários da Empresa: ${soma_funcioarios_total:,}')

print()
print()

#2. Qual foi o faturamento da empresa?
faturamentos_df = servicos_prestados_df[['ID Cliente','Tempo Total de Contrato (Meses)']].merge(cadastro_clientes_df[['ID Cliente', 'Valor Contrato Mensal' ]], on='ID Cliente')
faturamentos_df['Faturamento Total'] = faturamentos_df['Valor Contrato Mensal'] * faturamentos_df['Tempo Total de Contrato (Meses)']
print(faturamentos_df.head())
soma_faturamento_total = faturamentos_df['Faturamento Total'].sum()
print()
print(f'Soma de todos faturamentos da tabela: ${soma_faturamento_total:,}')


print()
print()



#3. Qual o % de funcionários que já fechou algum contrato?
total_funcionarios_fecharam_servico = len(servicos_prestados_df['ID Funcionário'].unique())
total_funcionarios = len(cadastro_funcionarios_df['ID Funcionário'])
porcentagem_de_funcionarios_contrato_fechado = total_funcionarios_fecharam_servico / total_funcionarios
print(f'Percentual de funcionários que já fechou algum contrato: {porcentagem_de_funcionarios_contrato_fechado:.2%}')

print()
print()

#4. Calcule o total de contratos que cada área da empresa já fechou
contratos_area_df = servicos_prestados_df[['ID Funcionário']].merge(cadastro_funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário')#primeiro a tabela que recebe as informaçoes e dentro do merge a tabela que vai da as informações
contratos_area_qtnd = contratos_area_df['Area'].value_counts()
print(contratos_area_qtnd)

print()
print()

#5. Calcule o total de funcionários por área
contagem_funcionario_por_area = cadastro_funcionarios_df['Area'].value_counts()
print(contagem_funcionario_por_area)
print(contagem_funcionario_por_area.plot(kind='bar'))

print()
print()

#6. Qual o ticket médio mensal (faturamento médio mensal) dos contratos?
# #Dica: .mean() calcula a média -> exemplo: media_colunaA = dataframe['colunaA'].mean()

