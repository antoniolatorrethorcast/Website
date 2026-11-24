"""Guia em português: como prever o churn de clientes em bancos, seguros e telecom (2026-11-24). Tradução de churn_guide_content.py.
Números de exemplo = os que thorcast.ai já publica nos vídeos de casos de uso, com a mesma etiqueta
(ilustrativo / simulado / caso). Sem nomes de clientes nem preços."""

FILE = "como-prever-churn-bancos-seguros-telecom.html"
DATE = "2026-11-24"

TITLE = "Como prever o churn de clientes em bancos, seguros e telecom — Thorcast.AI"
DESC = ("Guia de modelos de churn para bancos, seguros e telecom: como definir a perda de clientes, que dados usar, como medir "
        "com a sua capacidade de contato e como levar o score a uma campanha rentável.")
H1 = "Como prever o churn de clientes em bancos, seguros e telecom: guia prático 2026"
TAG = "GUIA"
META = "Thorcast.AI · Atualizado em 24 de novembro de 2026 · 8 min de leitura"
CRUMB = "Como prever o churn de clientes em bancos, seguros e telecom"
ABOUT = "Previsão de churn de clientes"

INTRO = (
    "<p>A maioria dos guias de churn é escrita para empresas de software por assinatura. Em bancos, seguros e "
    "telecomunicações o problema é outro: o cliente raramente avisa que vai sair, o churn nem sempre é um cancelamento "
    "formal e a equipe de retenção tem uma capacidade fixa de ligações, ofertas ou visitas. Este guia é para equipes de "
    "analytics, risco, CRM e retenção desses setores.</p>"
    "<p>A ideia central: um modelo de churn não se mede por quantas saídas prevê, e sim por quanto valor preserva com os "
    "contatos que você já consegue fazer. Os números de exemplo deste guia vêm dos casos que mostramos em vídeo em "
    "thorcast.ai, com a mesma etiqueta que têm lá (caso, exemplo ilustrativo ou simulado).</p>"
)

DEF_H = "Primeiro, defina o que é “sair” no seu setor"
DEF_P = ("<p>A definição do evento (o <em>target</em>) pesa mais no resultado que o algoritmo. Escreva-a antes de olhar os "
         "dados, com um horizonte claro: “sai nos próximos 60 ou 90 dias”, medido a partir da data em que você faria o contato.</p>")
DEFS = [
    ("Bancos e varejo financeiro",
     "Raramente há um encerramento formal: o cliente para de usar o cartão, leva o salário para outro banco ou esvazia a conta. Defina "
     "o churn como encerramento ou como queda sustentada de atividade ou saldo (por exemplo, sem transações por 90 dias), e separe a "
     "saída voluntária do cancelamento por inadimplência, que se trata com um modelo de cobrança."),
    ("Seguros de vida e saúde",
     "O evento é a caducidade ou o resgate da apólice. O momento importa: os primeiros anos de uma apólice concentram boa parte dos "
     "cancelamentos, então vale modelar a persistência por tempo de apólice, e não só “cancela sim ou não”."),
    ("Seguros gerais e corretoras",
     "O churn acontece sobretudo na renovação: o cliente não renova ou muda para outra seguradora. O horizonte natural são as semanas "
     "antes do vencimento, quando a ligação ainda pode mudar a decisão."),
    ("Telecom",
     "No pós-pago, o evento é a portabilidade ou o cancelamento. No pré-pago não há cancelamento: o cliente para de recarregar. Defina "
     "o churn por inatividade (por exemplo, 30 dias sem recarga nem uso) e trate à parte a migração do pós-pago para o pré-pago, que "
     "nem sempre é perda."),
]

DATA_H = "Que dados preveem o churn"
DATA = [
    "<strong>Comportamento recente.</strong> Mudanças mais que níveis: a queda de uso, saldo, recargas ou transações nas últimas semanas diz mais que a média do ano.",
    "<strong>Relacionamento com a empresa.</strong> Tempo de casa, produtos contratados, reclamações, ligações ao atendimento, falhas de serviço e mudanças de plano ou de cobertura.",
    "<strong>Preço e condições.</strong> Reajustes de tarifa ou de prêmio, fim de um período promocional, vencimento de um contrato ou de uma fidelização.",
    "<strong>Contexto externo.</strong> O perfil da região onde o cliente mora, a qualidade do e-mail e do telefone e a pegada digital são sinais que os seus sistemas não têm e que ajudam sobretudo quando o histórico próprio é curto.",
    "<strong>Cuidado com o vazamento de informação.</strong> Qualquer variável registrada depois que o cliente decidiu sair (um pedido de portabilidade, uma ligação para cancelar) faz o modelo parecer perfeito no laboratório e falhar em produção.",
]

MEASURE_H = "Meça o modelo com a sua capacidade de contato"
MEASURE = (
    "<p>A acurácia engana: se 3% dos clientes saem, um modelo que diz “ninguém sai” acerta 97%. O que importa é quantos churns reais "
    "você encontra dentro da capacidade que a sua equipe consegue contatar. Ordene a carteira pelo score, pegue os primeiros N (a sua "
    "capacidade) e conte quantos deles realmente saíram na amostra de teste, separada por tempo.</p>"
    "<p>É assim que as diferenças aparecem nos casos que publicamos:</p>"
)
CASES = [
    ("Telecom móvel (caso em vídeo)", "Com os mesmos 200.000 contatos, o modelo da Thorcast encontra 132.000 dos clientes que sairiam, contra 102.000 do modelo atual. O Gini sobe de 0,44 para 0,60."),
    ("Seguros de vida (exemplo simulado)", "Nos 20% de maior risco, o modelo atual encontrou 12,5 cancelamentos reais a cada 100; a Thorcast, 16,5 com dados internos e 18,5 somando dados enriquecidos."),
    ("Corretoras de seguros (exemplo)", "Com a mesma capacidade de 240.000 contatos, o modelo atual encontra 88.000 das 160.000 apólices que sairiam; a Thorcast encontra 105.000."),
    ("Seguro auto, renovação (cenário ilustrativo)", "Com a mesma capacidade de 50.000 ligações, dos clientes escolhidos pelo método atual sairiam 40%; dos escolhidos pela Thorcast, 60%. Isso preserva cerca de US$ 2,8 milhões a mais em prêmios por ano."),
]

VALUE_H = "Nem todos os clientes valem o mesmo, nem todos podem ser retidos"
VALUE = [
    "<strong>Priorize por valor, não só por risco.</strong> Combinar a probabilidade de churn com o valor futuro do cliente (CLTV) coloca "
    "primeiro quem levaria mais valor. Em um exemplo ilustrativo de banco, com os mesmos 30.000 contatos a oferta retém 1.500 clientes com "
    "a Thorcast contra 900 com o modelo atual: cerca de US$ 270 mil de CLTV preservado por ano.",
    "<strong>Procure quem a ação realmente muda.</strong> Há clientes que vão sair de qualquer jeito e outros que ficariam de qualquer forma. "
    "O melhor uso da capacidade é contatar quem uma ligação ou oferta consegue reter, e prever qual incentivo funciona com cada um.",
    "<strong>Meça com um grupo de controle.</strong> Deixe uma parte dos clientes de alto risco sem contato. Sem esse grupo você não sabe "
    "quantos ficaram graças à campanha e quantos teriam ficado de qualquer forma.",
]

DEC_H = "Do score à campanha: camadas de decisão"
DEC = (
    "<p>Um modelo de churn só gera valor se muda quem é contatado. Por isso a última peça é a regra de decisão: com uma capacidade fixa, "
    "quantos contatos fazer, com quem e com qual oferta, e quanto valor cada alternativa preserva.</p>"
    "<p>Na Thorcast isso é resolvido pelas <strong>camadas de decisão</strong>. As <strong>Thorcast Decision Layers</strong> vêm "
    "pré-configuradas no app: você informa a economia da sua campanha e vê o impacto em cada ponto de corte. Quando a regra é própria da "
    "sua operação (um número fixo de ligações por agência, ofertas diferentes por segmento, custos de contato por canal), as "
    "<strong>Customized Decision Layers</strong> permitem descrevê-la ao MJÖ em linguagem natural para que ele monte uma camada sob medida, "
    "que você revisa e aprova. O resultado fica na linguagem do negócio: quantos clientes você retém e quanto valor preserva.</p>"
)

MISTAKES_H = "Erros comuns"
MISTAKES = [
    "Treinar com uma partição aleatória em vez de temporal: o modelo parece melhor do que vai funcionar.",
    "Definir o churn com dados que chegam tarde (o cancelamento formal) quando o cliente já tinha saído meses antes.",
    "Medir só com acurácia ou com o Gini, sem olhar quantos churns caem dentro da capacidade de contato.",
    "Contatar todos os de alto risco com a mesma oferta, sem olhar valor nem probabilidade de resposta.",
    "Lançar a campanha sem grupo de controle e depois não conseguir demonstrar o resultado.",
    "Não monitorar o modelo: mudanças de preço, de concorrência ou de perfil de clientes o degradam em poucos meses.",
]

FIT_H = "Como a Thorcast faz"
FIT = [
    "<strong>NORA</strong> prepara os dados: você diz em linguagem natural o que precisa (limpar, unir tabelas, construir o target) e ela propõe um plano que você aprova; cada etapa passa por um motor de validação determinístico.",
    "<strong>A Data Enrichment Network</strong> transforma um e-mail, um telefone ou um endereço em sinais novos: mais de 3.000 data points, condensados em 261 sinais prontos para o modelo.",
    "<strong>MJÖ</strong> constrói e compara os modelos e apresenta o melhor, com métricas padrão e um relatório técnico pronto para auditoria.",
    "<strong>As camadas de decisão</strong> transformam o score em uma campanha com impacto econômico, pré-configuradas ou sob medida.",
    "<strong>Implantação e monitoramento</strong> na Thorcast Cloud, nas suas instalações ou no app, com recalibração quando a população muda.",
]

FAQ_H = "Perguntas frequentes"
FAQ = [
    ("O que é um modelo de churn?",
     "É um modelo preditivo que estima, para cada cliente, a probabilidade de sair em um horizonte definido (por exemplo, os próximos 90 dias). Serve para ordenar a carteira e decidir quem contatar primeiro com as ações de retenção disponíveis."),
    ("Com quanta antecedência dá para prever o churn?",
     "Depende do setor e dos dados, mas o objetivo é chegar antes de o cliente tomar a decisão: semanas antes em telecom e bancos, e antes do vencimento em seguros gerais. Um horizonte curto demais deixa pouca margem para agir; um longo demais perde precisão."),
    ("Funciona para pré-pago em telecom?",
     "Sim, mas o churn é definido por inatividade (parar de recarregar ou de usar), porque não há cancelamento formal. Os dados de uso recente e os sinais externos são especialmente úteis quando a operadora tem pouca informação sobre o cliente."),
    ("O que é uma camada de decisão em uma campanha de retenção?",
     "É a regra que transforma o score em quem contatar, com qual oferta e com que impacto econômico. Na Thorcast você pode usar camadas pré-configuradas (Thorcast Decision Layers) ou pedir ao MJÖ uma sob medida para a sua operação (Customized Decision Layers)."),
]

MORE_H = "Continue lendo"
MORE = [
    ("modelo-de-churn-clientes.html", "Modelo de churn com IA (com vídeos por setor)"),
    ("como-escolher-software-de-credit-scoring.html", "Como escolher software de credit scoring: guia prático"),
    ("perguntas-frequentes.html#gini-uplift", "Resultados dos dados alternativos por país"),
    ("para-quem-e.html", "Para quem é a Thorcast.AI"),
    ("tutorials-pt.html", "Tutoriais em vídeo"),
]
