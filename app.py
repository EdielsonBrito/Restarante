# app.py
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# criando restaurante
restaurante_praca = Restaurante('praça', 'Gourmet')

# criando intens do cardápio
bebida_suco = Bebida('Suco de Melancia', 5.0,'grande')
prato_paozinho = Prato('Paozinho',2.00,'O melhor pão da cidade')

# aplicando desconto no itens
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

# adicionando itens ao cardápio
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

# função principal
def main():
    restaurante_praca.exibir_cardapio

if __name__== '__main__':
    main()

