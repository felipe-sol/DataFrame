def nome_funcao(a,b,c):
    soma =  a + b + c
    return soma

print(nome_funcao(1,4,5))

####################################
#Ex.2

soma = lambda x,y: x+ y
print(soma(2,5))
###################################
#Ex3

dobro = lambda z: z*2
print(dobro(10))
####################################
import pandas as pd

dados= {
       'idade': [25,30,22],
       'nome': ['ana', 'bruno', 'carlos'],
       'cidade': ['SP','RJ', 'BH']
        }

df= pd.DataFrame(dados)

df['Idade_mais']= df['idade'].apply(lambda k: k+5)
##################################################
# Ex.5

df1 = pd.DataFrame({'valores': [1,2,3,4,5]})
df1['Novos_valores']=df1['valores'].apply(lambda z: z*2)

##########################################################
#Ex.6

df1['par_impar']=df1['valores'].apply(lambda x: 'par' if x%2==0 else 'impar')
##############################################################################
#Ex.7

dados2 = {
    'nome': ['ana', 'bruno', 'carlos'],
    }

df2=pd.DataFrame(dados2)

df['nomes_maiusculo']=df2['nome'].apply(lambda nome: nome.upper())
#####################################################################
#Ex.8

dados3 = {
    'idade': [25,30,22,34,23],
    }

df3 = pd.DataFrame(dados3)

\
df3['classific_idade']=df3['idade'].apply(lambda idade: 'adolescente' if idade < 18   else 'adulto' if 18<idade<60  else 'idoso')