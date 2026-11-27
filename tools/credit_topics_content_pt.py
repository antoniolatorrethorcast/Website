"""Guias em português (2026-11-26): otimização do ponto de corte e análise de inferência de rejeitados.
Tradução de credit_topics_content_en.py, com as mesmas cifras ilustrativas."""

DATE = "2026-11-26"

CUTOFF = dict(
    FILE="otimizacao-ponto-de-corte-credito.html",
    TITLE="Otimização do ponto de corte no crédito: guia e calculadora",
    DESC=("Como otimizar o ponto de corte de um score de crédito passo a passo: fórmula da PD de equilíbrio, exemplo "
          "numérico, calculadora gratuita, taxa de aprovação vs taxa de maus e cortes por segmento."),
    H1="Otimização do ponto de corte no crédito: como definir o corte que maximiza o lucro",
    TAG="GUIA",
    META="Thorcast.AI · Atualizado em 27 de novembro de 2026 · 10 min de leitura",
    MODIFIED="2026-11-27",
    DEF=("<strong>Otimizar o ponto de corte</strong> é escolher o limite de score que separa os proponentes aprovados dos "
         "recusados para que o lucro esperado seja o maior possível dentro do apetite de risco da instituição. A regra central: "
         "aprovar quando a probabilidade de inadimplência calibrada está abaixo da <strong>PD de equilíbrio = margem ÷ "
         "(margem + perda)</strong>. <a href=\"#calculator\">Teste a calculadora</a>."),
    CRUMB="Otimização do ponto de corte",
    ABOUT="Otimização do ponto de corte de um score de crédito",
    SECTIONS=[
        (None,
         "<p>Um modelo de crédito ordena os proponentes por risco. O <strong>ponto de corte</strong> transforma essa ordem em "
         "decisão: aprova todos acima dele e recusa o resto. É o número do processo de crédito que mais movimenta dinheiro e, "
         "muitas vezes, o que é escolhido com menos análise. Este guia mostra como defini-lo com números, passo a passo, para "
         "equipes de risco, política de crédito e finanças de bancos, financeiras, fintechs e varejo financeiro.</p>"
         "<p>As cifras dos exemplos são <strong>ilustrativas</strong>: números redondos escolhidos para mostrar o método, não "
         "dados de nenhuma carteira.</p>"),
        ("O que o ponto de corte decide",
         "<p>Mover o corte troca um erro por outro. Subindo o corte, você aprova menos e perde menos com inadimplência, mas "
         "recusa clientes que pagariam. Baixando, ganha mais receita em troca de mais perdas. Os dois números mais olhados são:</p><ul>"
         "<li><strong>Taxa de aprovação (cut-off rate):</strong> a proporção de proponentes acima do corte. Uma taxa de 60 % "
         "significa que seis em cada dez são aprovados. Algumas equipes chamam de «cut-off rate» a proporção recusada; deixe "
         "claro qual definição você usa em cada relatório.</li>"
         "<li><strong>Taxa de maus dos aprovados:</strong> a proporção de créditos aprovados que deve ficar inadimplente na "
         "janela de desempenho (por exemplo, 90 dias de atraso em 12 meses).</li></ul>"
         "<p>Nenhum dos dois diz onde parar. O lucro diz.</p>"),
        ("Passo 1: a probabilidade de inadimplência de equilíbrio",
         "<p>Para um proponente, aprovar compensa quando o ganho esperado supera a perda esperada:</p>"
         "<p><strong>Lucro esperado = (1 − PD) × margem − PD × perda</strong></p>"
         "<p>onde <em>PD</em> é a probabilidade de inadimplência dada pelo modelo, <em>margem</em> é o que você ganha com um "
         "crédito pago (juros e tarifas, menos custo de funding e operação) e <em>perda</em> é o que você perde com um crédito "
         "inadimplente (exposição × severidade, líquida de recuperações). Igualando o lucro esperado a zero, chega-se à "
         "<strong>PD de equilíbrio</strong>:</p>"
         "<p><strong>PD de equilíbrio = margem ÷ (margem + perda)</strong></p>"
         "<p>Exemplo ilustrativo: um crédito de 1.000 deixa margem de 150 se for pago e perda de 650 se ficar inadimplente. A PD "
         "de equilíbrio é 150 ÷ 800 = 18,75 %. Cada proponente com PD abaixo de 18,75 % soma lucro esperado; cada um acima "
         "disso o reduz. O corte ótimo é o score em que a PD cruza essa linha, desde que o modelo esteja calibrado.</p>"),
        ("Passo 2: um exemplo numérico",
         "<p>Considere 10.000 proponentes divididos em cinco faixas de risco de 2.000 cada, com a mesma economia acima "
         "(cifras ilustrativas):</p>"
         "<div class=\"cmp-wrap\"><table class=\"cmp-table\"><thead><tr><th>Faixas aprovadas</th><th>Taxa de aprovação</th>"
         "<th>Taxa de maus dos aprovados</th><th>Lucro esperado</th></tr></thead><tbody>"
         "<tr><td>Só A (PD 2 %)</td><td>20 %</td><td>2,0 %</td><td>268.000</td></tr>"
         "<tr><td>A–B (PD até 5 %)</td><td>40 %</td><td>3,5 %</td><td>488.000</td></tr>"
         "<tr><td>A–C (PD até 10 %)</td><td>60 %</td><td>5,7 %</td><td>628.000</td></tr>"
         "<tr><td>A–D (PD até 18 %)</td><td>80 %</td><td>8,8 %</td><td><strong>640.000</strong></td></tr>"
         "<tr><td>Todas (PD até 32 %)</td><td>100 %</td><td>13,4 %</td><td>428.000</td></tr>"
         "</tbody></table></div>"
         "<p>O lucro é máximo aprovando as faixas A a D. A faixa D acrescenta muito pouco (12.000 em 2.000 créditos) porque sua "
         "PD de 18 % fica logo abaixo do equilíbrio de 18,75 %; a faixa E, com 32 %, perde 212.000. Daí saem duas lições:</p><ul>"
         "<li>As faixas próximas do equilíbrio quase não mudam o lucro, mas mudam muito o volume e o risco. É aí que entram o "
         "apetite de risco, o capital e a estratégia.</li>"
         "<li>O ótimo é frágil. Se a perda por inadimplência sobe de 650 para 700, a PD de equilíbrio cai para 17,6 % e a faixa "
         "D fica negativa: o melhor corte sobe para A–C. O corte precisa acompanhar a economia, e não o contrário.</li></ul>"),
        ("Passo 3: confira as restrições",
         "<p>O corte que maximiza o lucro é o ponto de partida, não a resposta final. Antes de defini-lo, confira:</p><ul>"
         "<li><strong>Apetite de risco:</strong> a taxa de maus ou a perda esperada máxima aprovada pelo conselho.</li>"
         "<li><strong>Capital e funding:</strong> quanto volume o balanço suporta.</li>"
         "<li><strong>Metas de volume:</strong> o crescimento pode justificar aprovar de propósito uma faixa marginal, com o custo explícito.</li>"
         "<li><strong>Regulação e tratamento justo:</strong> regras de capacidade de pagamento, crédito responsável e explicação de recusas.</li>"
         "<li><strong>Calibração:</strong> a lógica do equilíbrio só funciona se uma PD de 10 % significar de fato cerca de 10 "
         "inadimplências em 100. Verifique a calibração com dados recentes e fora do período de treino.</li></ul>"),
        ("Passo 4: análise de swap set ao trocar de modelo",
         "<p>Quando um modelo novo substitui o atual, compare as duas políticas proponente a proponente, com a mesma taxa de "
         "aprovação:</p><ul>"
         "<li><strong>Swap-ins:</strong> proponentes que o modelo novo aprova e o antigo recusava.</li>"
         "<li><strong>Swap-outs:</strong> proponentes que o modelo antigo aprovava e o novo recusa.</li></ul>"
         "<p>O modelo novo é melhor se os swap-ins forem menos arriscados que os swap-outs. O problema: só se observa o "
         "desempenho dos swap-outs, porque os swap-ins foram recusados. O desempenho deles precisa ser estimado, que é "
         "justamente o papel da <a href=\"analise-inferencia-de-rejeitados.html\">inferência de rejeitados</a>, ou medido com "
         "um teste controlado e limitado abaixo do corte antigo.</p>"),
        ("Passo 5: um corte ou vários",
         "<p>Um corte único supõe que todos os proponentes têm a mesma economia. Muitas vezes não é assim: margens, valores e "
         "recuperações mudam por produto, canal e segmento. Definir um corte por segmento, cada um com sua PD de equilíbrio, "
         "costuma somar lucro com o mesmo risco total. Mantenha poucos segmentos, para poder explicá-los e monitorá-los, e "
         "documente por que cada um existe.</p>"),
        ("Passo 6: revise com frequência fixa",
         "<p>Um corte ótimo há seis meses pode não ser hoje. Revise quando mudarem o custo de funding, os preços, a severidade "
         "das perdas, o perfil dos proponentes ou o cenário macroeconômico, e pelo menos a cada trimestre. Acompanhe a taxa de "
         "aprovação, a inadimplência precoce das safras recentes e a calibração do score: um desvio em qualquer um deles é o "
         "sinal para recalcular o corte.</p>"),
        ("Erros comuns",
         "<ul><li>Escolher o corte pela taxa de aprovação («aprovamos 60 %») sem relação com a economia.</li>"
         "<li>Usar um score sem calibração como se fosse uma probabilidade.</li>"
         "<li>Medir a política nova só nos proponentes que a antiga aprovava.</li>"
         "<li>Manter o mesmo corte depois que mudam os preços ou o custo de funding.</li>"
         "<li>Definir o corte numa planilha que ninguém consegue auditar depois.</li></ul>"),
        ("Como funciona na Thorcast",
         "<p>Na Thorcast, a passagem do score à decisão é feita com <strong>camadas de decisão</strong>. As "
         "<strong>Thorcast Decision Layers</strong> pré-configuradas incluem o ponto de corte de originação: você informa a "
         "economia da sua política, como o que ganha com um crédito pago e o que perde com um inadimplente, e vê aprovação, "
         "risco e lucro em cada corte, lado a lado. Quando a decisão não cabe numa camada padrão, por exemplo regras diferentes "
         "por segmento, você a descreve ao MJÖ em linguagem natural e o agente monta uma <strong>Customized Decision Layer</strong> "
         "para você revisar e aprovar.</p>"
         "<p>Assim o corte é recalculado com as mesmas premissas sempre que a economia muda, e premissas e resultados ficam "
         "documentados para o comitê de risco e o validador.</p>"),
    ],
    FAQ=[
        ("O que é a otimização do ponto de corte?",
         "É o processo de escolher o limite de score de crédito que maximiza o lucro esperado dentro do apetite de risco, do "
         "capital e das restrições regulatórias da instituição. Parte da probabilidade de inadimplência de equilíbrio, "
         "margem ÷ (margem + perda), e é conferido com uma tabela de lucro por faixa de score."),
        ("O que é o ponto de corte de um score de crédito?",
         "É o limite de score que separa os proponentes aprovados dos recusados. Quem fica acima do corte é aprovado, ou segue "
         "para a próxima etapa do processo; o resto é recusado."),
        ("O que é cut-off rate?",
         "Normalmente, a taxa de aprovação num ponto de corte: a proporção de proponentes acima dele. Algumas equipes usam o "
         "termo para a proporção recusada, então convém colocar sempre a definição ao lado do número."),
        ("Como se calcula o ponto de corte ótimo?",
         "Calcule a PD de equilíbrio, margem ÷ (margem + perda), e aprove os proponentes cuja PD calibrada esteja abaixo dela. "
         "Depois ajuste por apetite de risco, capital, metas de volume e regulação, e confira o resultado com uma tabela de "
         "lucro por faixa de score."),
        ("Com que frequência revisar o ponto de corte?",
         "Sempre que a economia mudar (preços, custo de funding, severidade) ou o perfil dos proponentes mudar, e pelo menos a "
         "cada trimestre. Taxa de aprovação, inadimplência precoce e calibração indicam quando recalculá-lo."),
        ("Qual a relação entre o ponto de corte e a inferência de rejeitados?",
         "Baixar o corte significa aprovar proponentes que a política anterior recusava e cujo desempenho nunca foi observado. "
         "A inferência de rejeitados estima como eles teriam se comportado, para que o novo corte não seja definido sobre uma amostra enviesada."),
    ],
    MORE=[
        ("analise-inferencia-de-rejeitados.html", "Análise de inferência de rejeitados: guia passo a passo"),
        ("como-escolher-software-de-credit-scoring.html", "Como escolher software de credit scoring"),
        ("credit-scoring-com-ia.html", "Credit scoring com IA e dados alternativos"),
        ("blog-12.html", "Reject inference in credit scoring (em inglês)"),
        ("tutorials-pt.html", "Tutoriais em vídeo"),
    ],
)

REJECT = dict(
    FILE="analise-inferencia-de-rejeitados.html",
    TITLE="Inferência de rejeitados no credit scoring: guia — Thorcast.AI",
    DESC=("Como fazer uma análise de inferência de rejeitados (reject inference) no credit scoring: dados necessários, "
          "exemplo de parcelling com números, escolha do método, validação e o que documentar."),
    H1="Análise de inferência de rejeitados: guia passo a passo com um exemplo",
    TAG="GUIA",
    META="Thorcast.AI · Atualizado em 26 de novembro de 2026 · 9 min de leitura",
    CRUMB="Análise de inferência de rejeitados",
    ABOUT="Inferência de rejeitados no credit scoring",
    SECTIONS=[
        (None,
         "<p>Um score de originação aprende com os créditos que você concedeu, mas é aplicado a todos que pedem crédito. A "
         "<strong>inferência de rejeitados</strong> (reject inference) estima como os proponentes recusados teriam se "
         "comportado, para que o modelo novo não aprenda só com quem a política anterior deixou passar. Este guia é a parte "
         "prática: como fazer a análise, passo a passo, com um exemplo. Os métodos e armadilhas estão no nosso artigo "
         "<a href=\"blog-12.html\">Reject inference in credit scoring</a> (em inglês).</p>"
         "<p>As cifras do exemplo são <strong>ilustrativas</strong>, escolhidas para mostrar o método.</p>"),
        ("Passo 1: monte a amostra de todos os proponentes",
         "<p>Você precisa de todas as propostas do período, não só dos créditos:</p><ul>"
         "<li>Um identificador e a data da proposta.</li>"
         "<li>A <strong>decisão</strong>: aprovada ou recusada. Separe quem foi aprovado mas não contratou: não é bom nem mau.</li>"
         "<li>O <strong>desempenho</strong> dos aprovados, com definição e janela fixas (por exemplo, 90 dias de atraso em 12 meses).</li>"
         "<li>As mesmas variáveis para aprovados e recusados, capturadas no momento da proposta.</li></ul>"
         "<p>Se os recusados não têm as variáveis, ou foram filtrados do data warehouse, a inferência não é possível. Corrigir "
         "essa falta de dados é a primeira entrega.</p>"),
        ("Passo 2: construa o score preliminar",
         "<p>Treine um modelo só com os aprovados (o modelo de «bons e maus conhecidos») ou use um score existente em que você "
         "confie. A função dele é ordenar os recusados por risco. Confirme que ele ordena bem numa amostra de aprovados fora do "
         "período de treino antes de inferir qualquer coisa.</p>"),
        ("Passo 3: infira o desempenho (exemplo de parcelling)",
         "<p>Aplique o score a todos, aprovados e recusados, e agrupe-os em faixas de risco. Em cada faixa, pegue a taxa de maus "
         "observada dos aprovados e atribua aos recusados uma taxa maior, porque dentro da mesma faixa eles costumam ser mais "
         "arriscados. Aqui o fator de ajuste é 1,5:</p>"
         "<div class=\"cmp-wrap\"><table class=\"cmp-table\"><thead><tr><th>Faixa</th><th>Aprovados</th>"
         "<th>Taxa de maus observada</th><th>Recusados</th><th>Taxa de maus inferida (×1,5)</th><th>Maus inferidos</th></tr></thead><tbody>"
         "<tr><td>1 (menor risco)</td><td>4.000</td><td>2 %</td><td>200</td><td>3 %</td><td>6</td></tr>"
         "<tr><td>2</td><td>3.000</td><td>4 %</td><td>400</td><td>6 %</td><td>24</td></tr>"
         "<tr><td>3</td><td>2.000</td><td>7 %</td><td>800</td><td>10,5 %</td><td>84</td></tr>"
         "<tr><td>4</td><td>800</td><td>12 %</td><td>1.200</td><td>18 %</td><td>216</td></tr>"
         "<tr><td>5 (maior risco)</td><td>200</td><td>20 %</td><td>1.400</td><td>30 %</td><td>420</td></tr>"
         "<tr><td>Total</td><td>10.000</td><td>4,8 %</td><td>4.000</td><td>18,8 %</td><td>750</td></tr>"
         "</tbody></table></div>"
         "<p>No <em>parcelling</em>, 750 dos 4.000 recusados são marcados como maus, ao acaso dentro de cada faixa e nessas "
         "proporções, e o resto como bons. No <em>fuzzy augmentation</em>, cada recusado entra duas vezes, uma como bom e outra "
         "como mau, ponderado pelas probabilidades inferidas. Nos dois casos a amostra de treino passa de 10.000 para 14.000 "
         "registros e a taxa de maus sobe de 4,8 % para 8,8 %, mais perto da população que o modelo vai avaliar.</p>"),
        ("Passo 4: escolha o método",
         "<div class=\"cmp-wrap\"><table class=\"cmp-table\"><thead><tr><th>Situação</th><th>Opção razoável</th></tr></thead><tbody>"
         "<tr><td>Poucas recusas, ou a política anterior foi quase aleatória na região que importa</td><td>Treinar só com aprovados e documentar o porquê</td></tr>"
         "<tr><td>Um score preliminar confiável e proponentes suficientes por faixa</td><td>Parcelling</td></tr>"
         "<tr><td>Você prefere carregar a incerteza em vez de forçar rótulos</td><td>Fuzzy augmentation</td></tr>"
         "<tr><td>Há dados de bureau de recusados que conseguiram crédito em outra instituição</td><td>Usar primeiro esse desempenho real e inferir só o resto</td></tr>"
         "<tr><td>É possível um teste controlado e limitado abaixo do corte</td><td>Fazê-lo: o desempenho observado vale mais que qualquer inferência</td></tr>"
         "</tbody></table></div>"),
        ("Passo 5: defina os parâmetros com cuidado",
         "<ul><li><strong>Faixas:</strong> faixas por quantis mantêm tamanhos parecidos; faixas de largura igual seguem a escala "
         "do score. Defina um mínimo de registros por faixa.</li>"
         "<li><strong>Fator de ajuste:</strong> justifique-o com o que o negócio sabe dos recusados, ou com dados de bureau. "
         "Teste um intervalo, não um único valor.</li>"
         "<li><strong>Peso da população recusada:</strong> controla quanto a inferência move o modelo final.</li>"
         "<li><strong>Calibração e limites:</strong> calibre as probabilidades preliminares (Platt ou regressão isotônica) e "
         "limite os valores extremos para que não dominem.</li></ul>"),
        ("Passo 6: valide o resultado",
         "<p>A inferência não pode ser validada com os próprios registros inferidos. Estes são os testes que um analista ou "
         "validador deveria ver:</p><ul>"
         "<li><strong>Medir só com desempenho real.</strong> Registros inferidos vão para o treino, nunca para a amostra de teste "
         "nem para um fold de teste da validação cruzada.</li>"
         "<li><strong>Comparar com o modelo só de aprovados</strong> na mesma amostra de teste fora do período: o desempenho não "
         "deve cair e a ordenação dos aprovados deve se manter estável.</li>"
         "<li><strong>Conferir a taxa de maus inferida:</strong> maior que a dos aprovados em cada faixa, crescente com o risco e "
         "coerente com a evidência de bureau disponível.</li>"
         "<li><strong>Sensibilidade:</strong> repetir com outros fatores e pesos. Se o modelo final muda muito, a inferência "
         "está definindo o resultado e precisa de uma justificativa mais sólida.</li>"
         "<li><strong>Revisão do swap set:</strong> ver quem o modelo novo aprovaria que o antigo recusava, com a mesma taxa de "
         "aprovação. É ali que a inferência importa, e onde se toma a "
         "<a href=\"otimizacao-ponto-de-corte-credito.html\">decisão do ponto de corte</a>.</li></ul>"),
        ("Passo 7: documente a decisão",
         "<p>A validação do modelo vai perguntar por que ele aprova perfis que a política anterior recusava. Registre a "
         "população recusada usada, o score preliminar, o método e seus parâmetros, a taxa de maus inferida por faixa, a "
         "comparação com o modelo só de aprovados e as razões da escolha final, inclusive a de não usar inferência.</p>"),
        ("Como funciona na Thorcast",
         "<p>Na Thorcast, a inferência de rejeitados é uma etapa opcional entre a preparação de dados e a modelagem. Ela aparece "
         "quando o alvo é binário e uma população recusada foi declarada, com uma coluna de status de aprovação. Suporta "
         "parcelling e fuzzy augmentation, com o score preliminar gerado automaticamente ou tirado de um score existente, e "
         "ajustes de faixas, método de faixas, mínimo de registros por faixa, peso da população recusada, limites de "
         "probabilidade e calibração.</p>"
         "<p>Antes de mudar qualquer coisa, uma prévia compara o dataset só de aprovados com o aumentado: registros, maus "
         "observados, maus inferidos, taxas de maus e um resumo por faixa, com avisos. Você decide se usa. As linhas inferidas "
         "servem só para treino, então todas as métricas são calculadas com desempenho real.</p>"),
    ],
    FAQ=[
        ("O que é a análise de inferência de rejeitados?",
         "É o processo de estimar como os proponentes de crédito recusados teriam se comportado e somá-los aos dados de treino, "
         "para corrigir o viés de uma amostra formada só por créditos aprovados."),
        ("Qual método de inferência de rejeitados é melhor?",
         "Nenhum vence sempre. Parcelling e fuzzy augmentation são os mais usados porque podem ser explicados. O desempenho "
         "real, de bureau ou de um teste controlado, supera qualquer inferência quando é possível obtê-lo."),
        ("A inferência de rejeitados sempre melhora o modelo?",
         "Não. Ela substitui desempenhos que faltam por premissas, e a evidência acadêmica sobre os ganhos é mista. Use-a como "
         "uma decisão documentada e testada, comparando com o modelo só de aprovados sobre desempenho real."),
        ("O que significa «recusado pelo score»?",
         "Significa que a proposta foi recusada porque o score de crédito ficou abaixo do ponto de corte da instituição. O score "
         "estima o risco de não pagar a partir dos dados do proponente; cada instituição define seu próprio corte, por isso a "
         "mesma pessoa pode ser recusada numa e aprovada em outra."),
        ("Registros inferidos podem ser usados para medir o modelo?",
         "Não. Eles vão só para o treino. Medir um modelo com desempenhos inferidos é avaliá-lo com as próprias premissas."),
    ],
    MORE=[
        ("otimizacao-ponto-de-corte-credito.html", "Otimização do ponto de corte no crédito"),
        ("como-escolher-software-de-credit-scoring.html", "Como escolher software de credit scoring"),
        ("credit-scoring-com-ia.html", "Credit scoring com IA e dados alternativos"),
        ("blog-12.html", "Reject inference in credit scoring (em inglês)"),
        ("tutorials-pt.html", "Tutoriais em vídeo"),
    ],
)
