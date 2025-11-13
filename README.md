# Restarante
códigos

# Importamos as classes necessárias para montar o sistema
from plataforma.livraria import Livraria
from plataforma.stand.romance import Romance
from plataforma.stand.terror import Terror

# --- Criação das livrarias ---
# Cada livraria possui um nome e uma categoria (tipo de livros que vende)
livraria_tijuca = Livraria('Tijuca', 'Romance')
livraria_barra = Livraria('Barra', 'Terror')

# --- Criação dos livros ---
# Criamos livros específicos para cada categoria
livro1 = Romance('Orgulho e Preconceito', 39.90)
livro2 = Terror('It - A Coisa', 59.90)

# --- Adicionando livros aos stands (estoques) das livrarias ---
livraria_tijuca.adicionar_no_stand(livro1)
livraria_barra.adicionar_no_stand(livro2)

# --- Avaliações feitas por leitores ---
livraria_tijuca.receber_avaliacao('Maria', 9)
livraria_tijuca.receber_avaliacao('João', 8)
livraria_barra.receber_avaliacao('Ana', 10)

# --- Função principal ---
def main():
    # Mostra todas as livrarias criadas
    Livraria.listar_livrarias()
    print()
    
    # Mostra os livros disponíveis em cada stand
    livraria_tijuca.exibir_stand()
    print()
    livraria_barra.exibir_stand()
    print()
    
    # Mostra a média das avaliações recebidas por cada livraria
    print(f'Média de avaliações da livraria Tijuca: {livraria_tijuca.media_avaliacoes()}')
    print(f'Média de avaliações da livraria Barra: {livraria_barra.media_avaliacoes()}')

# --- Executa o programa apenas se este arquivo for rodado diretamente ---
if __name__ == '__main__':
    main()
