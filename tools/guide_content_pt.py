"""Guia em português: como escolher software de credit scoring (2026-11-24). Tradução de guide_content.py.
Fatos de terceiros = os verificados para as comparações (tools/compare_content.py, 23/11/2026).
Fatos da Thorcast = o que thorcast.ai já publica. Sem preços aqui."""

FILE = "como-escolher-software-de-credit-scoring.html"
DATE = "2026-11-24"

TITLE = "Como escolher software de credit scoring: guia 2026 — Thorcast.AI"
DESC = ("Guia prático para escolher software de credit scoring: os cinco tipos de ferramentas, dez critérios de avaliação, "
        "como fazer uma prova de conceito justa e os sinais de alerta.")
H1 = "Como escolher software de credit scoring: guia prático 2026"
TAG = "GUIA"
META = "Thorcast.AI · Atualizado em 24 de novembro de 2026 · 10 min de leitura"
CRUMB = "Como escolher software de credit scoring"
LABELS = ("Vantagem:", "Limite:", "Faz sentido se", ("Critério", "O que perguntar", "Sinal de alerta"))
ABOUT = "Software de credit scoring"

INTRO = (
    "<p>Escolher uma ferramenta de credit scoring é uma decisão que dura anos: define com que rapidez você lança um modelo "
    "novo, quanto risco aceita em cada aprovação e com que facilidade explica cada decisão ao regulador. Este guia é para "
    "equipes de risco, analytics e crédito de bancos, financeiras, fintechs, varejo financeiro, seguradoras e operadoras "
    "de telecom que estão comparando opções.</p>"
    "<p><strong>Transparência:</strong> este guia é escrito pela Thorcast.AI, que é um dos fornecedores. Por isso dizemos "
    "em que casos a Thorcast se encaixa e em quais vale mais a pena outra ferramenta. Os dados de outros fornecedores vêm "
    "dos próprios sites e documentação deles, revisados em novembro de 2026, e as fontes estão nas nossas comparações.</p>"
)

BEFORE_H = "Antes de olhar fornecedores: defina o problema"
BEFORE = [
    ("Qual decisão você quer melhorar", "Originação, comportamento (aumento de limite, renovações), cobrança ou fraude em propostas. Cada uma tem dados, horizontes e métricas diferentes; uma ferramenta boa para uma nem sempre é boa para outra."),
    ("Qual é o seu ponto de partida", "Um score de bureau, um scorecard próprio, regras manuais ou nada. O que você tem hoje é o modelo contra o qual vai comparar tudo o que for novo."),
    ("Quem vai operar a ferramenta", "Uma equipe experiente de ciência de dados, analistas de risco que não programam ou uma mistura. É a pergunta que mais elimina opções."),
    ("Onde os dados devem ficar", "Nuvem do fornecedor, a sua nuvem ou os seus próprios servidores. Se as suas políticas não permitem que os dados saiam, descarte essas opções desde o início."),
    ("O que o regulador exige", "Documentação de desenvolvimento e validação, explicação de cada recusa, monitoramento periódico. Peça exemplos reais desses entregáveis, não só a promessa."),
]

TYPES_H = "Os cinco tipos de ferramentas"
TYPES_P = "<p>Quase tudo o que você vai encontrar se encaixa em uma destas cinco famílias. Cada uma tem o seu lugar; o erro mais comum é comparar ferramentas de famílias diferentes como se resolvessem o mesmo problema.</p>"
TYPES = [
    ("1. Desenvolvimento próprio em Python ou R",
     "A sua equipe constrói com bibliotecas de código aberto (por exemplo scikit-learn, LightGBM, XGBoost ou OptBinning para scorecards).",
     "Controle total e custo zero de licenças.",
     "Tudo depende das pessoas: preparação de dados, documentação, implantação e monitoramento precisam ser construídos e mantidos. Os prazos se medem em meses.",
     "você tem uma equipe de ciência de dados sólida e estável, e tempo para construir a plataforma em torno dos modelos."),
    ("2. Suítes estatísticas tradicionais",
     "O exemplo mais conhecido é o SAS (Viya e Risk Modeling), com agrupamento interativo, weight of evidence, inferência de rejeitados e documentação automática.",
     "O padrão que muitos validadores e reguladores conhecem; controle máximo sobre o scorecard clássico.",
     "Exige uma equipe treinada na ferramenta; o ciclo completo de um modelo novo costuma levar semanas ou meses.",
     'a sua governança de modelos já está construída sobre essa suíte. Veja <a href="thorcast-vs-sas-pt.html">Thorcast.AI vs SAS Viya</a>.'),
    ("3. Plataformas de AutoML e machine learning corporativo",
     "Por exemplo DataRobot e H2O.ai: treinam e comparam muitos algoritmos, explicam previsões e implantam modelos para muitos casos de uso.",
     "Muito poder de modelagem e governança para equipes de ciência de dados que conduzem vários projetos de IA.",
     "São pensadas sobretudo para cientistas de dados, e não encontramos na documentação delas dados de terceiros incluídos: os dados você traz.",
     'você tem uma equipe experiente de ciência de dados e pipelines de dados existentes. Veja <a href="thorcast-vs-datarobot-pt.html">vs DataRobot</a> e <a href="thorcast-vs-h2o-pt.html">vs H2O.ai</a>.'),
    ("4. Scores e motores de decisão de bureaus e fornecedores de originação",
     "Scores genéricos de bureau e motores de regras para executar a política de crédito em tempo real.",
     "Rápidos de colocar em funcionamento e com dados de bureau incluídos.",
     "Um score genérico não aprende com a sua carteira nem com os seus clientes; personalizá-lo costuma ser um projeto à parte.",
     "você precisa começar a decidir já, com pouco histórico próprio, ou já tem o modelo e falta o motor para executá-lo."),
    ("5. Plataformas de análise preditiva com agentes de IA e dados incluídos",
     "A categoria mais nova, onde está a Thorcast.AI: agentes de IA que preparam os dados e constroem os modelos a partir de instruções em linguagem natural, com dados alternativos incluídos e camadas de decisão com impacto econômico.",
     "Do dado bruto a um modelo em produção em horas, sem precisar de uma grande equipe de ciência de dados.",
     "São mais novas que as suítes tradicionais; peça para ver os relatórios técnicos e teste com os seus próprios dados antes de decidir.",
     'você quer modelos próprios de nível produtivo, somar dados alternativos e cobrir mais casos com a mesma equipe. Veja <a href="para-quem-e.html">para quem é a Thorcast.AI</a>.'),
]

CRIT_H = "Dez critérios para avaliar, e o que perguntar a cada fornecedor"
CRIT = [
    ("Desempenho fora da amostra", "Que Gini e KS obtém em uma partição temporal (safras posteriores ao treinamento), e não só em uma amostra aleatória?",
     "Só mostram resultados de treinamento ou de uma partição aleatória."),
    ("Dados alternativos", "Que dados além dos meus pode somar, com que cobertura no meu país e com que base legal?",
     "Falam em “milhares de variáveis” sem dizer a cobertura no seu país."),
    ("Explicabilidade", "Como explico uma recusa específica? O que entrega para a validação do modelo?",
     "Não há um relatório técnico de exemplo que você possa ver antes de comprar."),
    ("Reprodutibilidade", "Se eu treinar duas vezes com os mesmos dados, obtenho o mesmo modelo? O código ou o plano fica versionado?",
     "Resultados que mudam entre execuções sem explicação."),
    ("Do score à decisão", "Posso ver aprovação, risco e lucro para cada ponto de corte?",
     "Entregam um score e a política “fica com você” em uma planilha à parte."),
    ("Preparação de dados", "Quem une e limpa as tabelas de origem, e quanto tempo isso leva?",
     "A demo começa sempre com um dataset já limpo, nunca com as suas tabelas reais."),
    ("Implantação e onde ficam os dados", "Nuvem do fornecedor, a sua nuvem ou os seus servidores? O scoring pode rodar na minha infraestrutura?",
     "Uma única opção de implantação que não cumpre as suas políticas."),
    ("Monitoramento e recalibração", "Como detecto que o modelo se degradou e quanto custa recalibrá-lo?",
     "O monitoramento é um módulo à parte ou um projeto de integração."),
    ("Quem opera", "Um analista de risco que não programa consegue construir e manter um modelo?",
     "Cada mudança exige um cientista de dados ou o fornecedor."),
    ("Custo total", "Licenças, dados, integração, infraestrutura e horas da sua equipe ao longo de três anos.",
     "Só cotam a licença, e os dados são cobrados à parte, fornecedor por fornecedor."),
]

POC_H = "Como fazer uma prova de conceito justa"
POC = [
    "<strong>Use a sua própria amostra.</strong> Com um identificador, o resultado real (por exemplo, atraso de 90 dias) e o seu score atual. Se incluir e-mail, telefone e endereço, também dá para medir a contribuição dos dados alternativos.",
    "<strong>Particione por tempo, não ao acaso.</strong> Treine com as propostas mais antigas e meça nas mais recentes. É o mais parecido com o funcionamento do modelo em produção.",
    "<strong>Compare com o que você tem hoje.</strong> O desafiante precisa vencer o seu score atual na mesma amostra de teste (Campeão–Desafiante), e não um modelo de referência escolhido pelo fornecedor.",
    "<strong>Revise as variáveis.</strong> Qualquer variável conhecida só depois da concessão do crédito (pagamentos, cobrança, status da conta) é vazamento de informação e infla o resultado.",
    "<strong>Meça em dinheiro.</strong> Além do Gini, peça a taxa de aprovação e a inadimplência esperada no ponto de corte que você usaria, e o que isso significa em lucro.",
    "<strong>Peça os entregáveis.</strong> O relatório técnico, o código ou plano reproduzível e como seria a implantação. Se não passar na validação interna, o melhor Gini não serve.",
]

DEC_H = "Do score à decisão: camadas de decisão"
DEC = (
    "<p>Um score, por melhor que seja, não decide nada sozinho. A pergunta do negócio é outra: quem eu aprovo, quanta "
    "inadimplência aceito e quanto ganho ou perco com essa política. Peça a cada fornecedor que mostre essa ponte entre a "
    "estatística e a decisão, com os seus números, e não só um Gini.</p>"
    "<p>Na Thorcast essa ponte são as <strong>camadas de decisão</strong>: elas pegam a estatística preditiva que a "
    "plataforma produz e a transformam em decisões de negócio concretas, com o impacto econômico calculado. Há duas formas de usá-las:</p>"
    "<ul>"
    "<li><strong>Thorcast Decision Layers.</strong> Camadas pré-configuradas no app para as decisões mais comuns, como o "
    "ponto de corte de originação. Você informa a economia da sua política (por exemplo, o que ganha com um crédito pago e "
    "o que perde com um inadimplente) e vê aprovação, risco e lucro para cada ponto de corte, lado a lado.</li>"
    "<li><strong>Customized Decision Layers.</strong> Quando a sua decisão não se encaixa em uma camada padrão (um número "
    "fixo de contatos, regras diferentes por segmento ou custos próprios da sua operação), você descreve a regra ao MJÖ em "
    "linguagem natural e o agente constrói uma camada sob medida. Você a revisa e aprova antes de usá-la.</li>"
    "</ul>"
    "<p>O resultado fica na linguagem do negócio: quantas propostas você aprova, quanta inadimplência espera e quanto lucro "
    "gera cada alternativa. Assim a decisão não depende de interpretar métricas estatísticas, e quem decide pode comparar "
    "cenários e escolher por conta própria.</p>"
)

FLAGS_H = "Sinais de alerta"
FLAGS = [
    "Um Gini muito acima do habitual na sua carteira: na maioria das vezes é vazamento de informação, não um modelo extraordinário.",
    "Resultados sem partição temporal nem comparação com o seu modelo atual.",
    "Dados alternativos sem cobertura documentada no seu país.",
    "Uma caixa-preta sem explicação por proposta nem documentação para o validador.",
    "Rankings de “os 10 melhores” sem metodologia: alguns sites cobram pela posição e não indicam quais produtos pagaram. Use-os como lista inicial, nunca como avaliação.",
]

FIT_H = "Onde a Thorcast.AI se encaixa, e onde não"
FIT_P = "<p>A Thorcast.AI é uma plataforma de análise preditiva com agentes de IA. Para credit scoring, é isto que ela oferece:</p>"
NOT_FIT = [
    "A sua governança de modelos está construída sobre o SAS e os seus validadores esperam os entregáveis dele: aí o SAS é o mais natural.",
    "A sua equipe de ciência de dados quer uma plataforma para construir e governar muitos tipos de IA e agentes próprios: veja DataRobot ou H2O.ai.",
    "Você só precisa de um score genérico e um motor de regras para decidir amanhã, sem construir um modelo próprio.",
]
NOT_FIT_P = "<p>Pode não ser a melhor opção se:</p>"

FAQ_H = "Perguntas frequentes"
FAQ = [
    ("O que é um software de credit scoring?",
     "É a ferramenta com a qual se constrói, valida, implanta e monitora o modelo que estima a probabilidade de um cliente não pagar. Vai desde bibliotecas de código aberto até plataformas que cobrem todo o ciclo, dos dados à decisão."),
    ("Machine learning ou scorecard tradicional?",
     "Depende do que a validação exige. Os modelos de machine learning costumam discriminar melhor; um scorecard é mais fácil de explicar variável por variável. O prático é testar os dois com os seus dados e escolher com o desempenho fora da amostra e os requisitos de explicabilidade na mesa."),
    ("Quanto os dados alternativos melhoram um modelo de crédito?",
     "Depende do país, do segmento e dos dados que você já tem. Na experiência da equipe fundadora da Thorcast, em 68 modelos de 12 países, somar dados alternativos aumentou o Gini em uma mediana de 35%. A única forma de saber para a sua carteira é medir em uma prova de conceito."),
    ("O que é uma camada de decisão?",
     "É a parte que transforma o score de um modelo em uma decisão de negócio com impacto econômico: para cada ponto de corte mostra quantas propostas são aprovadas, quanta inadimplência se espera e quanto lucro fica. Na Thorcast você pode usar camadas pré-configuradas (Thorcast Decision Layers) ou pedir ao MJÖ uma camada sob medida para o seu negócio (Customized Decision Layers)."),
    ("Quanto tempo leva uma prova de conceito?",
     "Com ferramentas tradicionais costuma ser um projeto de semanas. Com a Thorcast, uma prova de conceito com a sua própria amostra leva cerca de uma hora: a amostra é enriquecida, um modelo desafiante é treinado e comparado com o seu score atual."),
]

MORE_H = "Continue lendo"
MORE = [
    ("faq.html#gini-uplift", "Resultados dos dados alternativos por país (em inglês)"),
    ("thorcast-vs-datarobot-pt.html", "Thorcast.AI vs DataRobot"),
    ("thorcast-vs-h2o-pt.html", "Thorcast.AI vs H2O.ai"),
    ("thorcast-vs-sas-pt.html", "Thorcast.AI vs SAS Viya"),
    ("como-prever-churn-bancos-seguros-telecom.html", "Como prever o churn de clientes em bancos, seguros e telecom"),
    ("para-quem-e.html", "Para quem é a Thorcast.AI"),
    ("tutorials-pt.html", "Tutoriais em vídeo"),
]
