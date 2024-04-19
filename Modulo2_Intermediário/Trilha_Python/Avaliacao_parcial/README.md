
## FLUXO DE EXECUÇÃO 

Tem o intuito de mostrar  ao usuário a ordem que o script roda.

1º  É executado a função main().

2º  A função main() estancia a classe Estacões,  e executa o método requisicaoDeDados(), que irá usar o webdriver do Selenium para acessar o site do inmet em busca do anos de dados históricos e retornar um dicionário onde a chave é o ano e o valor o link para o arquivo .zip. 

3º  A tela principal inicia o script, onde chama o widgests e a função 'ano_selecionado', ela começa a chamar todas as outras funções mencionadas acima para que o script comece a roda

4º Os Widgests(), recebem os valores das funções para exibirem a tela para o usuário, onde  podem selecionar ano, estação do ano e gerar gráficos   da média e acumulo de precipitações, com base nos dados extraídos da Url fornecida. Foi feita a configuração para deixar mas intuitiva ao usuário.

5º  A função DataFrame(), usar a biblioteca ‘requests‘,para baixar  o arquivo zip da url fornecida que contem os dados as estações meteorológicas, extraindo o conteúdo para uma pasta específica do sistema. Retorna um dicionário contendo o nome dos arquivos descompactados e seus caminhos completos como valores.

6° Função CalcTempMediaCSV(self, arquivoURL) ler o arquivo CSV baixado, após isso, trata os dados obtidos e calcula à média da temperatura máxima de cada mês. 

7° Função CalcMediaPreciptacaoCSV(self, arquivoURL) ler o arquivo CSV baixado, após isso, trata os dados obtidos, faz a soma das precipitações e retorna o acúmulo das precipitações.
 
## RESUMO DAS FUNÇÕES

### requisicaoDeDados()
    Irá usar o webdriver do Selenium para acessar o site do inmet em busca do anos de dados históricos pela tag 'article' de classe 'post-preview', itera e organiza os valores recebidos p/ retornar um dicionário onde a chave é o ano (ANO 2000 (AUTOMÁTICA)) e o valor o link para o arquivo(https://portal.inmet.gov.br/uploads/dadoshistoricos/2000.zip) .zip. 


## downloadDataFrame()  
    Recebe por parâmetro a URL do arquivo .ZIP do ano que foi selecionada, usar o request para a requisição e baixar o arquivo, e verifica ou senão cria uma pasta 'datasets/Nome do ano selecionado' para armazena-lo. Em seguida descompacta o arquivo, deleta o arquivo .zip e retorna um dicionário onde a chave é o nome formatado da cidade(Ilhéus) e o valor o caminho absoluto do arquivo.

## CalcTempMediaCSV()

## CalcMediaPreciptacaoCSV()
    Recebe o caminho da arquivo .CSV; ler; trata os dados ausente ou valor inválido (-9999); cria um dataframe do tipo Datetime pela coluna 'DATA (YYYY-MM-DD)', agrupa por mês e calcula a média da temperatura máxima. Ao final retorna uma Serie com mês e média da temperatura (10, 25.5) 

## telaError()
    Cria uma janela Tk Inter com um Frame contendo uma mensagem de erro caso  a função 'requisicaoDeDados' não retorne dados.

## widget_lista_estacoes()  
    Recebe o container de onde será executado e o dicionário de estações; criar um widget Listbox() para listar as estações e ao selecionar uma estação irá chamar as funções CalcTempMediaCSV() e CalcMediaPreciptacaoCSV(), caso elas retornem dados, os repassa para os widgets que irão  gerar os gráficos widget_grafico_temperatura e widget_grafico_precipitação.

## widget_Label_AnoSelecionado()
    Recebe por parâmetro o ano selecionado e o container de onde será executado; cria um widget Label() para exibi-lo na tela.

## telaPrincipal()
    Recebe por parâmetro o dicionário  passado pela função 'requisicaoDeDados()' com os anos disponíveis, gere o widget Listbox() para lista-los e ao selecionar o ano desejado, executa a função ano_selecionado() que irá chamar as demais funções em cadeia começando pela widget_lista_estacoes().