# -------------------------------------------------------------
# GERADOR DE JOGOS PARA MEGA SENA 
# Testando código para armazenamento de projetos em GitHub
# -------------------------------------------------------------
import random

def gerar_jogo():
    """Gera um jogo com 6 números distintos entre 1 e 60."""
    return sorted(random.sample(range(1, 61), 6))

def gerar_multiplos_jogos(quantidade):
    """Gera a quantidade especificada de jogos."""
    jogos = []
    for i in range(quantidade):
        jogos.append(gerar_jogo())
    return jogos

# Gerar [6] 3 jogos
jogos_gerados = gerar_multiplos_jogos(3)

# Exibir os jogos
print("JOGOS GERADOS PARA A MEGA-SENA:")
print("-" * 40)
for i, jogo in enumerate(jogos_gerados, 1):
    print(f"Jogo {i}: {jogo}")
print("-" * 40)
print("Boa sorte!")