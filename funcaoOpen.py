# A função open() é utilizada para a abertura dos arquivos.


# Sua sintaxe é:

# arquivo = open(‘arquivo.txt’, ‘w’)
               
# A função open(), após a declaração da variável que receberá a função, necessita de dois parâmetros: primeiramente o nome do arquivo e, depois, o modo como estamos abrindo esse arquivo.

# Na sintaxe apresentada acima foi utilizado o ‘w’ para fazer a escrita em um arquivo.

# Caso o arquivo não exista nesse modo, o código criará um arquivo com o nome escrito no primeiro parâmetro

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# A função write() é utilizada para gravar

# informações em um arquivo existente.


# Sua síntaxe é:

# arquivo.write (‘Curso Python n’)

# arquivo.write (‘Aula Prática’)
               
# Na função, adicionamos o nome do arquivo e, logo após o símbolo do ponto final, fazemos a chamada da função write. Em seguida, adicionamos o texto que deverá ser gravado entre aspas simples


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# A função close() é muito importante para encerrar o arquivo após sua utilização.

# Atenção: Nunca abra o arquivo com a função open e depois o faça de novo, sem antes fechar a instância anterior.

# Sua síntaxe é:
# arquivo.close()

# Um dos motivos da necessidade da função close() é que se tentarmos escrever em um arquivo e não o fecharmos depois de terminar a escrita, as informações não chegarão ao arquivo e nada será escrito


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# A função read() realiza a leitura

# de todo conteúdo do arquivo.


# Sua sintaxe é:

# leitura=open(‘arquivo.txt, ‘r’)

# print leitura.read()

# leitura.close()

# Utilizamos o parâmetro ‘r’ que representa que o arquivo está sendo aberto em modo leitura.

# Desta forma, não é possível modificar os dados contidos no arquivo.