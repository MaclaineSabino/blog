import requests
import json




def deletar(url):  #excluir post sem autenticação



    resultado = requests.delete(url)




    return 'erro: '+str(resultado.status_code)+'\n'+resultado.text

def cadastrarPost(url):



    corpo = json.dumps({'title':'aulas de jango',
                        'body':'aulas com o professor Ely Miranda'
                        })
    headers = {'content-type': 'application/json'}
    resultado = requests.post(url,data=corpo,headers=headers,auth=('Bret','Bret123'))

    return 'status_code: '+str(resultado.status_code)+'\n'+resultado.text



def deletarAut(url,usuario,senha): #excluir post com autenticação

    resultado = requests.delete(url,auth=(usuario,senha))

    return 'status_code: '+str(resultado.status_code)+'\n'+resultado.text

def usuarios(url): #listar usuários
    resultado = requests.get(url)

    return 'status_code: '+ str(resultado.status_code) +'\n'+ str(resultado.json())


def cadastrarUsuarios(url): #tentativa de cadastrar usuários, vai gerar um erro
    corpo = json.dumps({'name':'maclaine',
                        'username':'mac',
                        'email':'emacsabino@hotmail.com',
                        'senha':'mac123',
                        'address':2})
    headers = {'content-type': 'application/json'}
    resultado = requests.post(url,data=corpo,headers=headers,auth=('Bret','Bret123'))

    return 'status_code: '+str(resultado.status_code)+'\n'+resultado.text

def deletarUsuario(url): #tentativa de deletar usuário, vai gerar erro

    resultado = requests.delete(url,auth=('Bret','Bret123'))

    return 'status_code: '+str(resultado.status_code)+'\n'+resultado.text


def postarComentario(url):
    corpo = json.dumps({'name':'Bret',
                        'email':'bret@hotmail.com',
                        'body':'post excelente',
                        'post':'et ea vero quia laudantium autem'})
    headers = {'content-type': 'application/json'}
    resultado = requests.post(url,data=corpo,headers=headers,auth=('Bret','Bret123'))
    return 'status_code: '+str(resultado.status_code)+'\n'+resultado.text

def excluirComentario(url):

    resultado = requests.delete(url,auth=('Bret','Bret123'))
    return 'status_code: '+str(resultado.status_code)+'\n'+resultado.text



print(deletar('http://127.0.0.1:8000/posts/1/')) #teste para deletar(url)

#print(deletarAut('http://127.0.0.1:8000/posts/13/','Bret','Bret123'))#teste para deletar autenticado

#print(usuarios('http://127.0.0.1:8000/users/'))

#print(cadastrarUsuarios('http://127.0.0.1:8000/users/')) tentativa de cadastrar usuário

#print(deletarUsuario('http://127.0.0.1:8000/users/1'))

#print(cadastrarPost('http://127.0.0.1:8000/posts/'))
#print(excluirComentario('http://127.0.0.1:8000/comments/54/')) tentativa de excluir comentario de um post de usuário diferente
#print(postarComentario('http://127.0.0.1:8000/comments/'))
