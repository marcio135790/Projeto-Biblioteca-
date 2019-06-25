#criação das listas e variáveis  
lusuario=[] 
lcpf=[]
lromance=[]
lajuda=[]
ldidatico=[]
alocado=[]
usuario=0
opcao = 9

#criação da função menu retornando o valor capturado
def menu ():
    print()
    print()
    print('*** BIBLIOTECA***')
    print ('Menu:') 
    print ('   1 - Matricular Usuário') 
    print ('   2 - Remover Matrícula')    
    print ('   3 - Listar Usuários Matrículados') 
    print ('   4 - Verificar Situaçao do Usuário')
    print ('   5 - Cadastrar livro')
    print ('   6 - Listar Categoria dos livros')
    print ('   7 - Alocar livro ao Usuário')
    print ('   9 - Sair') 
    opt = input('Digite a opçao desejada: ') 
    return opt


#criação da função matrícular usuário  
def adicionar_matricula ():        
    usuario = str(input("Digite o nome do usuário:"))
    lusuario.append(usuario)    
    cpf=int(input("Informe o CPF:"))
    lcpf.append(cpf)
    
    print()
    print('------------------------------------------------')
    print('Usuário Matrículado :)')    
    
    pass #deixa passar o fluxo



#criação da função remover matrícula  
def remover_matricula (): 
    usuario=str(input("Digite o Nome do Usuário:"))
    cpf=int(input("Informe o CPF:"))
    print()
    print('------------------------------------------------')
    
    if usuario in lusuario and cpf in lcpf:
        lusuario.remove(usuario)
        lcpf.remove(cpf)                    
        print('Usuário Removido :(')
    else:
        print('Esse Usuário Não Está Matrículado :(') 
    pass #deixa passar o fluxo


#criação da função Listar Usuários Matrículados  e formatando o layout de saída
def listar_usuarios ():
    x=0
    print('--Usuários Matrículados--')

    while x<len(lusuario and lcpf):
        e=lusuario[x]
        p=lcpf[x]
        print('------------------------------------------------')
        print('NOME:',e,'  |  CPF:',p)
        print('------------------------------------------------')
        x+=1
    pass #deixa passar o fluxo


#criação da função cadastrar livro
def cadastrar_livro ():
    livro=str(input("Digite o Nome do Livro:"))
    print('--Escolha a categoria do livro--')
    categoria=int(input("1- Romance  2- Auto-ajuda   3- Didático:"))
    print()
    print('------------------------------------------------')
    
    if categoria == 1:
        lromance.append(livro)        
        print("Livro Cadastrado :)")
    elif categoria == 2:
        lajuda.append(livro)
        print("Livro Cadastrado :)")
    elif categoria == 3:
        ldidatico.append(livro)
        print("Livro Cadastrado :)")
    else:
        print('Categoria Inválida :(')        
    pass #deixa passar o fluxo



#criação da função Listar categoria e formatando o layout de saída
def listar_categoria():
    x=0    
    print('--Escolha a categoria do livro--')
    categoria=int(input("1- Romance  2- Auto-ajuda   3- Didático:"))
    print()
    if categoria == 1:        
        print('Categoria Romance')
        print('------------------------------------------------')
        while x<len (lromance):            
            e=lromance[x]            
            print(e)
            print('------------------------------------------------')
            x+=1
    elif categoria == 2:
        print('Categoria Auto-ajuda')
        print('------------------------------------------------')
        while x<len (lajuda):            
            e=lajuda[x]
            print(e)
            print('------------------------------------------------')
            x+=1
    elif categoria == 3:
        print('Categoria Didático')
        print('------------------------------------------------')
        while x<len (ldidatico):            
            e=ldidatico[x]
            print(e)
            print('------------------------------------------------')
            x+=1
    else:
        print('Categoria Inválida :(')
    
    pass #deixa passar o fluxo


#criação da função alocar livro
def alocar():
    usuario=str(input("Digite o Nome do Usuário:"))
    cpf=int(input("Informe o CPF:"))
    if usuario in lusuario and cpf in lcpf:
        livro=str(input("Digite o Nome do Livro:"))
        print()
        print('------------------------------------------------')
        if livro in lromance:
            print('Livro Alocado com Sucesso :)')
            print('Categoria Romance')
            alocado.append(livro)
        elif livro in lajuda:
            print('Livro Alocado com Sucesso :)')
            print('Categoria Auto-ajuda')
            alocado.append(livro)
        elif livro in ldidatico:
            print('Livro Alocado com Sucesso :)')
            print('Categoria Didático')
            alocado.append(livro)
        else:
            print('Livro sem Cadastro :(')
    else:
        print('Usuário sem Cadastro :(')        
    pass #deixa passar o fluxo


#criação da função veríficar situação do usuário e formatando o layout de saída  
def verificar_situacao ():
    usuario = str(input("Digite o nome do usuário: "))
    cpf=int(input("Informe o CPF:"))
    
    if usuario in lusuario and cpf in lcpf:        
        print('------------------------------------------------')
        print('NOME:',usuario,'  |  CPF:',cpf)
        print('------------------------------------------------')
        print('Usuário Ativo :)  |   Livro Alocado:',alocado)
        print('------------------------------------------------')
    else:
        print('Usuário Sem Cadastro :(')

        
       
# criação do loop que faz a interação entre o valor capturado na função MENU
while opcao != '9': 
    if opcao == '1': 
        adicionar_matricula()        
    elif opcao == '2':  
        remover_matricula() 
    elif opcao == '3':  
        listar_usuarios() 
    elif opcao == '4':  
        verificar_situacao() 
    elif opcao == '5':       
        cadastrar_livro()
    elif opcao == '6':       
        listar_categoria()
    elif opcao == '7':       
        alocar()  
    
    opcao = menu()   
  

