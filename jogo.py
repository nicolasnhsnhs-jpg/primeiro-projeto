# Jogo de adivinhar um número de 1 a 100

# Importa o módulo "random", que serve para gerar números aleatórios
import random

# Sorteia um número inteiro entre 1 e 100 (incluindo o 1 e o 100) e guarda na variável "numero_secreto"
numero_secreto = random.randint(1, 100)

# Cria a variável "tentativas" para contar quantos palpites o jogador fez; começa em 0
tentativas = 0

# Cria a variável "palpite" com o valor 0 só para ela existir antes do laço começar
palpite = 0

# Mostra uma mensagem de boas-vindas na tela
print("Bem-vindo ao jogo de adivinhar o número!")

# Explica a regra do jogo para o jogador
print("Eu pensei em um número de 1 a 100. Tente adivinhar!")

# "while" repete o bloco de código abaixo enquanto o palpite for diferente (!=) do número secreto
while palpite != numero_secreto:

    # Pede para o jogador digitar um número; "input" sempre devolve texto, então guardamos o texto em "texto"
    texto = input("Digite seu palpite: ")

    # "isdigit()" verifica se o texto tem só algarismos (0 a 9); "not" inverte, ou seja: "se NÃO for só números..."
    if not texto.isdigit():
        # ...avisa o jogador que ele precisa digitar um número
        print("Isso não é um número! Digite apenas números de 1 a 100.")
        # "continue" pula o resto do laço e volta para o começo, pedindo um novo palpite (essa vez não conta como tentativa)
        continue

    # Agora que sabemos que o texto só tem números, "int" transforma o texto em número inteiro
    palpite = int(texto)
    if palpite < 1 or palpite > 100:
        print("Número fora do intervalo! Digite um número de 1 a 100.")
        continue


    # Soma 1 ao contador de tentativas a cada palpite
    tentativas = tentativas + 1

    # Se o palpite for maior que o número secreto...
    if palpite > numero_secreto:
        # ...avisa que o palpite foi alto
        print("Muito alto! Tente um número menor.")

    # Senão, se o palpite for menor que o número secreto...
    elif palpite < numero_secreto:
        # ...avisa que o palpite foi baixo
        print("Muito baixo! Tente um número maior.")

# Quando o laço termina, significa que o jogador acertou, então mostramos a mensagem de vitória
print("Parabéns! Você acertou! O número era", numero_secreto)

# Mostra quantas tentativas o jogador precisou para acertar
print("Você precisou de", tentativas, "tentativas.")
