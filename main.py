import pandas as pd
import numpy as np
import networkx as nx

#Definir uma função que acha o primeiro índice que tem os valores id_1 e id_2

def indexs(df,value1,value2):
    i=0
    while i<len(df.index):
        if df.iloc[i,5]==value1 and df.iloc[i,7]==value2:
            return i
        if df.iloc[i,7]==value1 and df.iloc[i,5]==value2:
            return i
        i += 1


def lessInformativeIndex(df,index1,index2):
    if pd.isnull(df.iloc[index1,12]):
        if pd.isnull(df.iloc[index2,12]) and pd.isnull(df.iloc[index2,13]):
            return index2
        return index1
    return index1


#   TEM QUE ESPECIFICAR ONDE ESTÁ A PASTA COM O ARQUIVO EXCEL AQUI

df = pd.read_csv('C:\\Users\\Pc home dez 2021\\Documents\\RA\\R\\only_classified_actions1.csv')

#   TEM QUE ESPECIFICAR ONDE ESTÁ A PASTA COM O ARQUIVO EXCEL AQUI


#df = pd.DataFrame([[1, 1], [2, 1]])
#G = nx.from_pandas_adjacency(df)
#G=nx.Graph()
#G.add_node('A',span=[1958,1999])
#G.add_node('B',b='1958',e='1999')
#G.add_edge('A','C',type='ally')
#G.add_edge('B','C')
#G.add_edge('A','D')
#G.add_edge('B','E')
#G.add_edge('A','B')
#print(list(G.nodes(data=True)))
#x=G.nodes['A']['span']
#print(x)
#print(G.edges.data())
#e=('A','C')
#k=G.get_edge_data(*e)
#print(type(k['type']))
#print(k['type']=='ally')
#y=[n for n in G.neighbors('A')]
#print(y)
#print(y[0])
#print([n for n in G.neighbors('B')])
#z=list(G.nodes())
#print(z)
#print(z[0])

#df = pd.read_csv('C:\\Users\\Pc home dez 2021\\Documents\\RA\\R\\actions_with_birth_death.csv')
#df1=pd.read_csv('C:\\Users\\Pc home dez 2021\\Documents\\RA\\R\\Ids_birth2_death2.csv')
#df=pd.read_csv('C:\\Users\\Pc home dez 2021\\Documents\\RA\\R\\only_classified_actions1.csv')
#print(list(df.columns))
#n=len(df1.index)
#print(df.iloc[0,:])
#df.drop(0,inplace = True)

#print(df.iloc[0,:])
#df['P(ally in common)']=np.nan
#df['P(ally | ally in common)']=np.nan
#G=nx.Graph()
#G.add_node('A',span=[1958,1999])
#rel=[]
#count=0
#data=pd.DataFrame()
#data['duration']=np.nan
#data['start']=np.nan
#new_row={'duration':2,'start':4}
#data=data.append(new_row, ignore_index=True)
#x=df.iloc[0,0:2]
#data=data.append(x, ignore_index=True)
#print(data)


#for i in range(len(df.index)):
#    if not pd.isnull(df.iloc[i,12]) and not pd.isnull(df.iloc[i,13]):
#        if df.iloc[i,12]>df.iloc[i,13]:
#            temp=df.iloc[i,13]
#            df.iloc[i,13]=df.iloc[i,12]
#            df.iloc[i,12]=temp
#for i in range(len(df.index)):
#    if not pd.isnull(df.iloc[i,12]) and not pd.isnull(df.iloc[i,13]):
#        if df.iloc[i,12]>df.iloc[i,13]:
#            count+=1
#print(count)

#df=pd.read_csv('C:\\Users\\Pc home dez 2021\\Documents\\RA\\R\\actions_with_birth_death_single_edges.csv')
#count1=0
#count2=0
#rel=[]
#listed=['ally','enemy','family','other']
#for i in range(len(df.index)):
#    if df.iloc[i,15] in listed:
#       if df.iloc[i,24]==0:
#            count2+=1
        #else:
#        if [df.iloc[i, 5], df.iloc[i, 7]] in rel:
#            if not pd.isnull(df.iloc[i,5]) and not pd.isnull(df.iloc[i,7]):
#                count1+=1
#        if [df.iloc[i, 7], df.iloc[i, 5]] in rel:
#            if not pd.isnull(df.iloc[i,5]) and not pd.isnull(df.iloc[i,7]):
#                count1+=1
#        if [df.iloc[i,5],df.iloc[i,7]] not in rel and [df.iloc[i,7],df.iloc[i,5]] not in rel:
#            rel.append([df.iloc[i,5],df.iloc[i,7]])

#print(count1)
#print(count2)

#.add_edge(df.iloc[i,5],df.iloc[i,7])
#G.add_node(df.iloc[i,4],span=[])

#print(df.iloc[0,:])
#df.drop(0,inplace = True)
#print(df.iloc[0,:])
rel=['ally','enemy','family','other']
index=[]
count=0
print(df.iloc[0])
#for i in range(len(df.index)):
#    if df.iloc[i,15] not in rel:
#        index.append(i)
#    if df.iloc[i,15]==np.nan:
#        index.append(i)
#df.drop(index, inplace=True)
ids=[]
indexes=[]
for i in range(len(df.index)):
    if [df.iloc[i,5],df.iloc[i,7]] not in ids and [df.iloc[i,7],df.iloc[i,5]] not in ids:
        ids.append([df.iloc[i,5],df.iloc[i,7]])
    else:
        index=indexs(df,df.iloc[i,5],df.iloc[i,7])
        if df.iloc[i,15]=='ally':
            if df.iloc[index,15]!='ally':
                indexes.append(index)
            else:
                index=lessInformativeIndex(df,i,index)
                indexes.append(index)
        if df.iloc[i,15]=='enemy':
            if df.iloc[index,15]=='ally':
                indexes.append(i)
            if df.iloc[index,15]=='enemy':
                index=lessInformativeIndex(df,index,i)
                indexes.append(index)
            else:
                indexes.append(index)
        if df.iloc[i,15]=='family':
            if df.iloc[index,15]=='other':
                indexes.append(index)
            if df.iloc[index,15]=='family':
                index=indexs(df,index,i)
                indexes.append(index)
            else:
                indexes.append(i)
        if df.iloc[i,15]=='other':
            if df.iloc[index,15]=='other':
                index=lessInformativeIndex(df,index,i)
                indexes.append(index)
            else:
                indexes.append(i)

df.drop(indexes,inplace=True)
#df.to_csv('C:\\Users\\Pc home dez 2021\\Documents\\RA\\R\\classified_actions1.csv',na_rep='NA',index= False)

#   TEM QUE ESPECIFICAR ONDE ESTÁ A PASTA QUE VAI CRIAR O ARQUIVO EXCEL AQUI

df.to_csv('C:\\Users\\Pc home dez 2021\\Documents\\RA\\R\\only_single_classified_actions1.csv',na_rep='NA',index= False)

#   TEM QUE ESPECIFICAR ONDE ESTÁ A PASTA QUE VAI CRIAR O ARQUIVO EXCEL AQUI