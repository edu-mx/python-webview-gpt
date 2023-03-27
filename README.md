# python-webview-gpt
Uma webview do chat gpt com python

### sobre

Criei este programa apenas por teste mais acabei gostando do resultado.
o desempenho é muito melhor do que usar um navegador e é mais prático.
** Ele renderiza o html através do navegador padrão, no meu caso o Edge, não cheguei a testar com outros navegadores porque não tenho instalado.
Alguns comandos do seu navegador podem funcionar normalmente como F5, aplications e alt + esquerda ou direita.
O cash, sessões histórico etc acredito que também são salvos pelo navegador, pois eles permanecem salvos.
No começo não estava acessível para o leitor de telas, más pesquizei e achei algo sobre rótulo que acaba ajudando o leitor de tela a navegar corretamente.
< Ainda não tenho muita experiência com wxpython, então se você souber como melhorar este código, fique à vontade!

### téstes
_ Sistema
Testei o programa no Windows 10 home single language 64 bit com nvda 2023.1
_ versão do python
Python 3.9.7 - 64 bit
> Esta versão do python é a que funciona bem com wxpython, inclusive o Nvaccess (nvda) utilisa esta mesma versão.

#### bibliotecas

A única biblioteca necessária é a Wxpython, instale pelo pip:
`pip install wxpython`
< Caso não instale corretamente, opte por usar a versão python que citei acima.