# Conversor_Unidades

Leonardo Zaniboni Silva - 11801049

Repositório referente ao trabalho final da disciplina de Desenvolvimento de Software para Sistemas Embarcados com Sistemas Operacionais (SEL0456).

O trabalho final consiste em um conversor de unidades feito de forma genérica - isto é, as grandezas e unidades podem ser acrescentadas ou retiradas por meio de um arquivo de configuração. O arquivo de configuração segue disposto neste repositório, com o nome de "config.xlsx".

<div align="center">
<img src="https://user-images.githubusercontent.com/65432723/207854539-88958b3a-4a3f-4135-b158-f7c8a637314c.png" width="700px" />
</div>

Para que seja possível configurar o arquivo, é necessário seguir o padrão já estabalecido. Por exemplo, ao adicionar uma nova grandeza, deve-se repetir o termo "Unidade" e colocar o nome das unidades, enquanto que na coluna ao lado deve ser dispostos os fatores em relação ao SI (por exemplo, g = 0.001 kg -> logo o fator para esta unidade é 0.001).

A figura abaixo ilustra o "front-end" do aplicativo.

<div align="center">
<img src="https://user-images.githubusercontent.com/65432723/207856722-b5547ccf-0e42-4ddf-a602-08cf08491594.png" width="300px" />
</div>

A conversão de unidades irá acontecer quando clicado no botão "Converter!". 
