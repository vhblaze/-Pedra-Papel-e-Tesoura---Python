import os, time, random, sys, getpass as gp

from termcolor import colored, cprint
from getpass import getpass
x = 0

def clear():
  time.sleep(0.1)
  os.system('clear')

def music():
  pygame.init()
  musica = pygame.mixer.music.load()
  pygame.mixer.music.play()
  input()

def twoplayer():
  Escolhas = ["Pedra", "Papel", "Tesoura"] 
  Dig_escolha = {"1": "Pedra", "2": "Papel", "3": "Tesoura"}

  r("Espero que se divirta!\n----------JOGO----------\n")
  r("1. Pedra\n2. Papel\n3. Tesoura\n")
  
  escolha1 = gp.getpass("Escolha do jogador 1 (1/2/3): ").strip()
  while escolha1 not in Dig_escolha:
      r("Escolha inválida. Por favor, tente novamente.\n")
      escolha1 = gp.getpass("Escolha do jogador 1 (1/2/3): ").strip()
  escolha1 = Dig_escolha[escolha1]

  escolha2 = gp.getpass("Escolha do jogador 2 (1/2/3): ").strip()
  while escolha2 not in Dig_escolha:
      r("Escolha inválida. Por favor, tente novamente.\n")
      escolha2 = gp.getpass("Escolha do jogador 2 (1/2/3): ").strip()
  escolha2 = Dig_escolha[escolha2]

  r(f"\nJogador 1 escolheu: {escolha1}\n")
  r(f"Jogador 2 escolheu: {escolha2}\n")

  if escolha1 == escolha2:
      r("Empate!\n")
  elif (escolha1 == "Pedra" and escolha2 == "Tesoura") or \
       (escolha1 == "Papel" and escolha2 == "Pedra") or \
       (escolha1 == "Tesoura" and escolha2 == "Papel"):
      r("Jogador 1 vence!\n")
      time.sleep(2)  
      clear()
  else:
      r("Jogador 2 vence!\n")
      time.sleep(2)  
      clear()

  if __name__ == "__main__":
    jogar_novamentecoop()


def r(x):
  for letter in x:
    print(letter, end="", flush=True)
    time.sleep(0.05)

def jogo():
  Escolhas = ["Pedra", "Papel", "Tesoura"] 
  Dig_escolha = {"Pedra": "Pedra", "Papel": "Papel", "Tesoura": "Tesoura"}

  r("Espero que se divirta!\n----------JOGO----------\n1.Pedra\n2.Papel\n3.Tesoura\n")
  escolha = input("Digite o número da sua escolha: ")
  if escolha == "1":
        escolha = "Pedra"
  elif escolha == "2":
        escolha = "Papel"
  elif escolha == "3":
        escolha = "Tesoura"
  clear()
  r(f"Você escolheu: {escolha}")
  time.sleep(2)
  clear()
  r("Aguarde enquanto o computador escolhe...")
  time.sleep(2)
  clear()
  escolha_computador = random.choice(Escolhas)
  r(f"O computador escolheu: {escolha_computador}")
  time.sleep(2)
  clear()
  if escolha == escolha_computador:
      r("Empate!")
      time.sleep(3)
      jogar_novamente()
      clear()
  elif (escolha == "Pedra" and escolha_computador == "Tesoura") or (escolha == "Papel" and escolha_computador == "Pedra") or (escolha == "Tesoura" and escolha_computador == "Papel"):
    print(f"Você venceu! {Dig_escolha[escolha]} vence {Dig_escolha[escolha_computador]}.")
    time.sleep(5)
    jogar_novamente()
    clear()
  else:
    print(f"Você perdeu! {Dig_escolha[escolha_computador]} vence {Dig_escolha[escolha]}.")
    time.sleep(5)
    jogar_novamente()
    clear()

def jogar_novamentecoop():
  r("Deseja jogar novamente? (s/n): ")
  jogar_novamente = input()
  if jogar_novamente.lower() == "s":
    clear()
    twoplayer()
  elif jogar_novamente.lower() == "n":
    clear()
    r("Obrigado por jogar!")
    time.sleep(2)
    clear()
    r("Voltando ao menu!")
    time.sleep(2)
    clear()
  else:
    clear()
    r("Opção inválida.\n voltando ao menu incial")
    time.sleep(2)
    clear()
    twoplayer()


def jogar_novamente():
  r("Deseja jogar novamente? (s/n): ")
  jogar_novamente = input()
  if jogar_novamente.lower() == "s":
    clear()
    jogo()
  elif jogar_novamente.lower() == "n":
    clear()
    r("Obrigado por jogar!")
    time.sleep(2)
    clear()
    r("Voltando ao menu!")
    time.sleep(2)
    clear()
  else:
    clear()
    r("Opção inválida. Tente novamente.\n voltando ao menu incial")
    time.sleep(2)
    clear()
    jogo()

def regras():
  r("As regras do pedra, papel e tesoura são simples:\n\nPedra ganha da tesoura (amassa)\nPapel ganha da pedra (embrulha)\nTesoura ganha do papel (corta).\n\nPronto agora so ir se divertir jogando contra o computador!")
  time.sleep(10)
  clear()
  print("Voltando ao menu...")
  time.sleep(2)
  clear()

def creditos():
    
  vh = colored("Vitor Hugo Neves Do Vale Camargos", "cyan")
  
  print("Carregando dados dos desenvolvedores...")
  time.sleep(2)
  clear()
  r("Projeto criado por:")
  time.sleep(2)
  r(f"\n\n{vh}\n")
  r(colored("Espero que tenham gostado", "white", "on_black"))
  time.sleep(20)
  clear()

def sair():
  print("Foi um prazer jogar com você!")
  time.sleep(1)
  print("Saindo...")
  time.sleep(2)
  clear()
  sys.exit()

while x != 5:
  print("BEM VINDO AO JOGO DO PEDRA, PAPEL E TESOURA!\n----------MENU----------\n1. Jogar com o pc\n2. Jogar com amigo\n3. Regras\n4. Creditos\n5. Sair\n------------------------")
  opcao = input("Digite o numero para acessar: ")
  time.sleep(0.5)
  clear()
  match opcao:
    case "1":
      jogo()
    case "2":
      twoplayer()
    case "3":
      regras()
    case "4":
      creditos()
    case "5":
      sair()
    case _:
      print("Opção inválida. Tente novamente.")
      time.sleep(2)
      clear()