counter_text = """
O comando counter serve para gerar times "counters" ao time ou pokémon de entrada. Recebe como argumento nomes ou números da pokedex referentes aos pokémons alvo.\n 

Exemplos:
1: /counter mewtwo
2: /counter 150
3: /counter moltres zapdos articuno

Respectivas respostas:

1:
Darkrai (dark move set) 
Darkrai (dark move set) 
Leavanny (bug move set) 
Liepard (dark move set) 
Genesect (bug move set) 
Mandibuzz (dark move set) 
25611.0

2:
Tyranitar (dark move set) 
Spiritomb (ghost move set) 
Genesect (bug move set) 
Scrafty (dark move set) 
Darkrai (dark move set) 
Tyranitar (dark move set) 
33525.0

3:
Tyranitar (rock move set) 
Rhydon (rock move set) 
Tyranitar (rock move set) 
82251.0

Caso apenas um pokémon seja passado como alvo, ele gera gera um time de 6 "counters" (útil para raids), mas caso seja passado mais de um alvo, será retornado um time de tamanho igual ao alvo.\n
O número ao final da resposta é o "fitness", um coeficiente que quanto maior, melhor o time gerado é em relação ao time alvo.
"""

counter2_text = """
O comando counter2 retorna os melhores pokémons "counters" ao time ou pokémon de entrada. Recebe como argumento nomes ou números da pokedex referentes aos pokémons alvo.\n 

Exemplos:
1: /counter2 mewtwo
2: /counter2 150
3: /counter2 moltres zapdos articuno

Respectivas respostas:

1:
Tyranitar (dark move set) 
Darkrai (dark move set) 
Giratina_origin (ghost move set) 
Volcarona (bug move set) 
Hydreigon (dark move set) 
Giratina (ghost move set)

2:
Tyranitar (dark move set) 
Darkrai (dark move set) 
Giratina_origin (ghost move set) 
Volcarona (bug move set) 
Hydreigon (dark move set) 
Giratina (ghost move set)

3:
Tyranitar (rock move set) 
Kyurem_white (ice move set) 
Tyranitar (rock move set)

Caso apenas um pokémon seja passado como alvo, será retornado os top 12 "counters" (útil para raids), mas caso seja passado mais de um alvo, será retornado um time com o mesmo tamanho do time alvo, com o melhor "counter para cada pokémon".
"""

notify_text="""
Faz uma menção, a todos os jogadores que estão na lista de raid passada.
Recebe argumento, um número que representa o ID da lista de raid.

Após o ID da raid pode ser colocado um texto para os notificados.

Exemplos:
/notificar 1
/notificar 2 alguma coisa...
"""

show_text="""
Mostra todas as raids que estão acontecendos.

Uso:
/mostrar

Pode também mostrar uma lista específica, basta passar o ID da lista de raid.

Exemplo:
/mostrar 8
"""

remove_text="""
Retira um nome da lista de raid.
Recebe argumento, índice do nome na lista e ID da raid, respectivamente.

Uso:
/retirar 5 3
"""

insert_text="""
Insere um nome na lista de raid.
Recebe argumentos, nome e ID da lista de raid.

Uso:
/colocar Fulano 40
"""

getout_text="""
Reverte o comando /entrar. Retira o seu nome da lista de raid que você entrou.
Recebe argumento, ID da lista de raid.

Uso:
/sair 30
"""

enter_text="""
Te adiciona a uma lista de raids.
Recebe argumento, ID da lista de raid.

Uso:
/entrar 30

Para reverter utiliza-se o comando /sair.

Pode ser usado com identificação personalizada.
Para isso, basta adicionar a identificação após o ID da lista de raid.

Exemplo:
/entrar 30 Fulano+4

OBS: Para reverter o /entrar com identificação personalizada utiliza-se o comando /retirar ao invés de /sair.
"""

setplace_text="""
Muda o local de uma lista de raid.
Recebe argumentos, ID da lista de raid e novo local.

Uso:
/mudarLocal 10 Praça dos cornos

Antes:
🔰 RAID LEVEL 5
🐣 Chefe: Mewtwo
⏳ Hora: 11:30
🏟 Gym: Estátua do corno manso
🌎 Local: Praça dos pescadores
ℹ️ RAID ID: 10

Depois:
🔰 RAID LEVEL 5 
🐣 Chefe: Mewtwo 
⏳ Hora: 11:30 
🏟 Gym: Estátua do corno manso 
🌎 Local: Praça dos cornos 
ℹ️ RAID ID: 10
"""

setgym_text="""
Muda o gym de uma lista de raid.
Recebe argumentos, ID da lista de raid e novo gym.

Uso:
/mudarGym 10 grafite do peixe-boi

Antes:
🔰 RAID LEVEL 5
🐣 Chefe: Mewtwo
⏳ Hora: 11:30
🏟 Gym: Estátua do corno manso
🌎 Local: Praça dos pescadores
ℹ️ RAID ID: 10

Depois:
🔰 RAID LEVEL 5 
🐣 Chefe: Mewtwo 
⏳ Hora: 11:30 
🏟 Gym: grafite do peixe-boi 
🌎 Local: Praça dos pescadores 
ℹ️ RAID ID: 10
"""

settime_text="""
Muda a hora de uma lista de raid.
Recebe argumentos, ID da lista de raid e nova hora.

Uso:
/mudarHora 10 12h em ponto!

Antes:
🔰 RAID LEVEL 5
🐣 Chefe: Mewtwo
⏳ Hora: 11:30
🏟 Gym: grafite do peixe-boi
🌎 Local: Praça dos pescadores
ℹ️ RAID ID: 10

Depois:
🔰 RAID LEVEL 5 
🐣 Chefe: Mewtwo 
⏳ Hora: 12h em ponto! 
🏟 Gym: grafite do peixe-boi 
🌎 Local: Praça dos pescadores 
ℹ️ RAID ID: 10
"""

setboss_text="""
Muda o boss (chefe) de uma lista de raid.
Recebe argumentos, ID da lista de raid e novo boss.

Uso:
/mudarChefe 10 Giratina

Antes:
🔰 RAID LEVEL 5
🐣 Chefe: Mewtwo
⏳ Hora: 12h em ponto! 
🏟 Gym: grafite do peixe-boi 
🌎 Local: Praça dos pescadores 
ℹ️ RAID ID: 10

Depois:
🔰 RAID LEVEL 5 
🐣 Chefe: Giratina 
⏳ Hora: 12h em ponto! 
🏟 Gym: grafite do peixe-boi 
🌎 Local: Praça dos pescadores 
ℹ️ RAID ID: 10
"""

setlevel_text="""
Muda o level de uma lista de raid.
Recebe argumentos, ID da lista de raid e novo level.

Uso:
/mudarChefe 10 4

Antes:
🔰 RAID LEVEL 4
🐣 Chefe: Giratina
⏳ Hora: 12h em ponto! 
🏟 Gym: grafite do peixe-boi 
🌎 Local: Praça dos pescadores 
ℹ️ RAID ID: 10

Depois:
🔰 RAID LEVEL 5 
🐣 Chefe: Giratina 
⏳ Hora: 12h em ponto! 
🏟 Gym: grafite do peixe-boi 
🌎 Local: Praça dos pescadores 
ℹ️ RAID ID: 10
"""

raid_text="""
Cria uma nova lista de raid:

Uso:
/raid

Resposta:
🔰 RAID LEVEL ?
🐣 Chefe: ??
⏳ Hora: ???
🏟 Gym: ????
🌎 Local: ?????
ℹ️ RAID ID: ID

Pode ser iniciado com parâmetros predefinidos.

Exemplo:
/raid 5 Mewtwo 20h20 grafite_cobra_coral Rua_Dr.Santana

Resposta:
🔰 RAID LEVEL 5
🐣 Chefe: Mewtwo
⏳ Hora: 20h20
🏟 Gym: grafite cobra coral
🌎 Local: Rua Dr.Santana
ℹ️ RAID ID: ID

Obs1: Note que na criação de lista com parâmetros predefinidos não é possível o uso de " " (espaços).\n
Porém parâmetros com espaço podem ser inseridos utilizando '_' no lugar de espaços ou pelos comandos de edição:\n
/mudarLevel
/mudarChefe
/mudarHora
/mudarGym
/mudarLocal

Obs2: O ID da lista de raid é definido pelo bot e não pode ser alterado.

"""
help_text = """
Retorna lista completa de comandos.

Uso:    
/help

Caso algum comando seja passado como argumento, retorna uma descrição mais detalhada do comando.

Exemplos:
/help counter
/help raid
/help mudarHora

"""

info_text="""
Retorna informações sobre o bot.

Uso:
/info
"""

setwelocome_text="""
Digite uma mensagem que você queira colocar nas boas vindas, em seguida, clique em cima dela e aperte na opção "responder", na resposta digite "/setwelcome".

Obs: Caso queira mencionar o novo membro do grupo, basta colocar "{}" (sem aspas) na mensagem ("{}" será substituído pela menção).

Uso:
/setwelcome
"""

delwelcome_text="""
Deleta menssagem de boas vindas do grupo.

Uso:
/delwelcome
"""

ban_text="""
O membro do chat que tiver uma menssagem respondida por "/ban" (sem aspas) por um admin, será banido imediatamente.

Restrições: O bot precisa ser admin, o alvo não pode ser admin e o comando só pode ser usado por um admin.

Uso:
/ban
"""

rules_text="""
Mostra o texto referente as regras.

Uso:
/regras
"""

setrules_text="""
Digite uma mensagem que você queira colocar como regras, em seguida, clique em cima dela e aperte na opção "responder", na resposta digite "/setrules".

Uso:
/setrules
"""

delrules_text="""
Deleta as regras do grupo.

Uso:
/delrules
"""

helpTexts = {
    'help': help_text,
    'info': info_text,
    'regras': rules_text,
    'setrules': setrules_text,
    'delrules': delrules_text,
    'setwelcome': setwelocome_text,
    'delwelcome': delwelcome_text,
    'ban': ban_text,
    'raid': raid_text,
    'mudarLevel': setlevel_text,
    'mudarChefe': setboss_text,
    'mudarHora': settime_text,
    'mudarGym': setgym_text,
    'mudarLocal': setplace_text,
    'entrar': enter_text,
    'sair': getout_text,
    'colocar': insert_text,
    'retirar': remove_text,
    'mostrar': show_text,
    'notificar': notify_text,
    'counter': counter_text,
    'counter2': counter2_text
}

helpText = """
Seja atento a sintaxe correta:
Para ver a descrição de um comando específico use "/help comando".

Informações:
/help
/info
/regras

Gerenciamento (Uso restrito a admins):
/setwelcome
/delwelcome
/setrules
/delrules
/ban

Raid:
/raid
/mudarLevel
/mudarChefe
/mudarHora
/mudarGym
/mudarLocal
/entrar
/sair
/colocar
/retirar
/mostrar
/notificar

Countering:
/counter 
/counter2 
"""

infoText="""
ROTOM_POGO_BOT

src:
-ssh: git@github.com:GuiEgle/Rotom_bot.git
-https: https://github.com/GuiEgle/Rotom_bot.git
"Pull requests são sempre bem vindos!"

Requerimentos:
-python-telegram-bot 12.0.0b1
-pyeasyga 0.3.1
-pandas 1.0.3
-pymongo 3.10.1

Contato para dúvidas ou report de bugs:
https://t.me/PokeGoIMDDevs.

Para começar digite "/help".
É isso, bom proveito!
"""

raidText="""
🔰 RAID LEVEL {}
🐣 Chefe: {}
⏳ Hora: {}
🏟 Gym: {}
🌎 Local: {}
ℹ️ RAID ID: {}
"""

startText="""
Olá eu sou o rotom, digite /help para saber como eu posso te ajudar!"
"""