# Previsao da final da Eurocopa 2024 Redes-Neurais
Neste relatório, foi desenvolvido um modelo de redes neurais para prever o resultado da final da Eurocopa 2024. Os dados foram retirados do arquivo ‘Euro_2024_Matches.csv’ contendo as informações detalhadas de cada partida.

- **Seleção dos dados**
Foram selecionadas colunas relevantes para a análise, como gols marcados, chutes, passes e expectativa de gols para ambas equipes.
- **Codificação dos Resultados**
Cada partida foi codificada com base no desempenho das equipes. Os resultados foram codificados como 1 para vitória e 0 para derrota ou empate, tanto para a Espanha quanto para a Inglaterra.
- **Modelagem**
Utilizei uma arquitetura de rede neural sequencial com duas camadas densas e uma camada de dropout para evitar o overfitting. Foi feito para as duas seleções, para haver a comparação.
- **Acurácia**
O modelo treinado alcançou 100% de acerto nos jogos da Espanha, que venceu todos os jogos. Já para a Inglaterra, que teve alguns empates, fazendo alguns testes chegou a 100% de acerto, porém na maioria das vezes 83% de acerto.
- **Previsão**
Com o modelo treinado, previu-se que a Espanha iria vencer a final da Eurocopa com base nos dados extraídos. A final, realizada em 14/07, terminou com a vitória da Espanha por 2x1 sobre a Inglaterra, confirmando a previsão feita pelo modelo. É importante pontuar que todos os testes foram realizados antes da final, e a previsão correta destaca a eficácia do modelo.

<p align="center">
  <img src="https://github.com/user-attachments/assets/6630b450-c5f7-4003-8ca5-92c21c07215c">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/46d7fb66-fd99-402a-b931-6e8448b4bcf6">
</p>

- **Considerações Finais**
Embora o modelo tenha apresentado alta acurácia nos testes realizados e tenha acertado o resultado final, é importante destacar que não é possível prever perfeitamente quem ganhará uma partida de futebol, pois este é um esporte muito imprevisível. 
No entanto, foi interessante realizar essa previsão, interligando os dados das partidas com o desempenho das equipes. A análise de algumas estatísticas básicas de cada equipe forneceu insights valiosos que contribuíram para a previsão de que a Espanha iria ganhar a final da Eurocopa.

## Como Usar
 - Clone o repositório para sua máquina local.
 - Instale as bibliotecas necessárias no código
 - Execute o .ipynb para explorar o código e resultados.
 - Sinta-se à vontade para alterar a base de dados para prever resultados de outros jogos de futebol; apenas lembre-se de ajustar os parâmetros para corresponder ao seu arquivo.