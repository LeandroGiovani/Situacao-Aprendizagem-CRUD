from database import *

def sair():
    print("\nSaindo...")

def voltarMenuT():
    vtMenuT = input("\nPressione ENTER para voltar... ")
    if len(vtMenuT) >= 0:
        menuTimes()

def voltarMenuTJ():
    vtMenuTJ = input("\nDigite o id do time para visualizar os jogadores ou pressione ENTER para voltar... ")
    if len(vtMenuTJ) == 0:
        menuTimes()
    elif len(vtMenuTJ) > 0:
        print(vtMenuTJ)
        for t in times:
            if t['id'] == int(vtMenuTJ):
                print(f'\n{t["nome"]} - {t["cidade"]} - {t["pontuacao"]} pontos')
        for j in jogadores:
            if j["idTime"] == int(vtMenuTJ):
                print(f'[{j["id"]}] {j["nome"]}, {j["posicao"]}, {j["idade"]} anos ({j["data_nascimento"]})')
        voltarMenuT()

def atualizarTime(timeId, novoNome, novaCidade, novaPont, novoJogosJogados):
    for t in times:
        if t["id"] == timeId:
            t["nome"] = novoNome
            t["cidade"] = novaCidade
            t["pontuacao"] = novaPont
            t["jogos_jogados"] = novoJogosJogados
            print("\nTime atualizado com sucesso!")
            return
    print("\nTime não encontrado!")
    menuTimes()

def atualizarJogador(jogadorId, novoNome, novaIdade, novaData, novaPosicao, novoIdTime):
    for j in jogadores:
        if j["id"] == jogadorId:
            j["nome"] = novoNome
            j["idade"] = novaIdade
            j["data_nascimento"] = novaData
            j["posicao"] = novaPosicao
            j["idTime"] = novoIdTime
            print("\nJogador atualizado com sucesso!")
            return
    print("\nJogador não encontrado!")
    menuJogadores()

def remover(idJ): 
    for j in jogadores:
        if j["id"] == idJ:
            jogadores.remove(j)
            print("\nJogador removido com sucesso!")
            return
    print("\nJogador não encontrado!")


def menu():
    indiceMenu = int(input("""
-----------------------
O que deseja gerenciar?
[1] Times
[2] Jogadores
[3] Sair    
-----------------------
"""))
    if indiceMenu == 1:
        menuTimes()
    elif indiceMenu == 2:
        menuJogadores()
    elif indiceMenu == 3:
        sair()
    else:
        print("\nValor inserido inválio.")
        menu()


def menuTimes():
    indiceMenuTimes = int(input("""
---------Times---------
[1] Visualizar
[2] Cadastrar
[3] Atualizar
[4] Voltar
[5] Sair
-----------------------
"""))
    if indiceMenuTimes == 1:
        for t in times:
            print(f'[{t["id"]}] {t["nome"]} - {t["cidade"]} - {t["pontuacao"]} pontos')
        voltarMenuTJ()
    elif indiceMenuTimes == 2:
        novoId = max(times, key=lambda x: x["id"])["id"]
        novoId = novoId + 1
        novoNome = input("Nome do time: ")
        novaCidade = str(input("Nome da cidade: "))
        novaPontuacao = int(input("Pontuação do time: "))
        novoJogosJogados = int(input("Quantidade de jogos jogados: "))

        novoTime = {
            "id": novoId
            ,"nome": novoNome
            ,"cidade": novaCidade
            ,"pontuacao": novaPontuacao
            ,"jogos_jogados": novoJogosJogados
        }

        times.append(novoTime)
        print("\nNovo time cadastrado com sucesso!")
        menuTimes()
    elif indiceMenuTimes == 3:
        idTime = int(input("Id to time que deseja modificar: "))
        nomeAtt = input("Novo nome do time: ")
        cidadeAtt = str(input("Nova cidade do time: "))
        pontuacaoAtt = int(input("Nova pontuação do time: "))
        jogosJogados = int(input("Nova quantidade de jogos jogados do time: ")) 
        atualizarTime(idTime, nomeAtt, cidadeAtt, pontuacaoAtt, jogosJogados)
        menuTimes()
    elif indiceMenuTimes == 4:
        menu()
    elif indiceMenuTimes == 5:
        sair()
    else:
        print("\nValor inserido inválio.")
        menuTimes()


def menuJogadores():
    indiceMenuJogadores = int(input("""
-------Jogadores-------
[1] Visualizar
[2] Cadastrar
[3] Atualizar
[4] Remover
[5] Voltar
[6] Sair
-----------------------
"""))
    if indiceMenuJogadores == 1:
        for i in range(len(times) + 1):    
            for t in times:
                if t["id"] == i:
                    print(f'\n{t["nome"]} - {t["cidade"]} - {t["pontuacao"]} pontos')
            for j in jogadores:
                if j["idTime"] == i:
                    print(f'{j["id"]} - {j["nome"]} - {j["posicao"]} - {j["idade"]} anos')
        menuJogadores()
    elif indiceMenuJogadores == 2:
        novoId = max(jogadores, key=lambda x: x["id"])["id"]
        novoId = novoId + 1
        novoNome = input("Nome do jogador: ")
        novaIdade = int(input("Idade do jogador: "))
        novoNascimento = input("Nova idade (Ex: 19/10/2001): ")
        novaPosicao = input("Posição do jogador: ")
        novoIdTime = int(input("Qual o id do time do jogador: "))

        novoJogador = {
            "id": novoId
            ,"nome": novoNome
            ,"idade": novaIdade
            ,"data_nascimento": novoNascimento
            ,"posicao": novaPosicao
            ,"idTime": novoIdTime
        }

        jogadores.append(novoJogador)
        print("Jogador cadastrado com sucesso!")
        menuJogadores()
    elif indiceMenuJogadores == 3:
        idJogador = int(input("Id to jogador que deseja modificar: "))
        nomeAtt = input("Novo nome do jogador: ")
        idadeAtt = input("Nova idade do jogador: ")
        dataAtt = input("Nova data de nascimento do jogador: ")
        posicaoAtt = input("Nova posição do jogador: ")
        timeAtt = int(input("Novo id do time: "))
        atualizarJogador(idJogador, nomeAtt, idadeAtt, dataAtt, posicaoAtt, timeAtt)
        menuJogadores()
    elif indiceMenuJogadores == 4:
        removerJogador = int(input("Id do jogador que deseja remover: "))
        remover(removerJogador)
        menuJogadores()
    elif indiceMenuJogadores == 5:
        menu()
    elif indiceMenuJogadores == 6:
        sair()
    else:
        menuJogadores()