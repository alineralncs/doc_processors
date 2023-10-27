import spacy

# Carregue o modelo linguístico do spaCy
nlp = spacy.load("pt_core_news_sm")

# Texto de exemplo
texto = """
Art. 1° - Atender a necessidades temporárias de relevante interesse acadêmico e/ou 
institucional, objetivando apoiar o desenvolvimento de projetos de excelência no ensino de 
graduação e pós-graduação e as atividades de pesquisa e extensão. O colegiado das Pró-Reitorias 
poderá indicar ao Reitor a contratação, por tempo determinado, de professores com atividades 
didáticas e de pesquisa e extensão, denominados professores visitantes. De acordo com as 
condições e prazos previstos nesta resolução, os professores visitantes podem ser enquadrados 
nas seguintes modalidades: 
I. Professor visitante brasileiro; 
II. Professor visitante estrangeiro. 
 § 1° O contrato de professor visitante será por tempo determinado de, no máximo, 
12(doze) meses, em regime de trabalho de 40 (quarenta) horas semanais com dedicação 
exclusiva, podendo: 
I. no caso de professor visitante brasileiro, ser renovado por um único período pelo 
prazo de até 12 (doze) meses; 
II. no caso de professor visitante estrangeiro, ser renovado por até três períodos 
consecutivos de, no máximo, 12 (doze) meses cada um. 
 § 2° Para ser contratado requere-se do candidato como qualificação mínima o 
título de doutor, reconhecido no País. 
Art. 2° - A contratação de professor visitante prescinde de concurso público e é efetivada 
através de um processo seletivo simplificado, que deve ser precedido de ampla divulgação 
nacional em Diário Oficial da União, sujeito à análise de notória capacidade técnica, científica ou 
artística do candidato, baseada em seu Curriculum Vitae devidamente comprovado e em projeto 
de pesquisa a ser desenvolvido, relacionado com a área do conhecimento objeto de seleção. 
 Art. 3° - A solicitação de contratação de professor visitante é de iniciativa dos Colegiados 
de Curso e/ou do Colegiado das Pró-Reitorias, devendo conter um único pedido de contratação 
por processo, com as seguintes informações e documentos: 
I. Justificativa detalhada e circunstanciada da necessidade da contratação do professor 
visitante, com indicação da área do conhecimento de atuação do visitante; 
II. Plano de trabalho contendo necessariamente a descrição detalhada das atividades de 
ensino (disciplinas que o professor se propõe a ministrar), pesquisa e extensão (projetos 
que especifiquem a relevância e justificativa, objetivos, metodologia, resultados esperados, 
agência de fomento, caso houver, e cronograma) a serem exercidas pelo professor visitante, 
podendo ainda incluir orientação acadêmica; 
III. Cronograma de execução do plano de trabalho proposto; 
IV. Cópia da ata de reunião do Colegiado de Curso e/ou do Colegiado das Pró-Reitorias; 
V.Datas do início e término do período de contratação; 
VI. Aprovação do pedido de contratação de professor visitante pela Direção do Campus 
e/ou pelo Colegiado das Pró-Reitorias, com parecer circustanciado e conclusivo; 
VII. Texto a ser divulgado no Diário Oficial da União (modelo em anexo). 
 
 Art. 4° - Cabe ao Conselho de Ensino, Pesquisa e Extensão – CONSEPE, apreciar e 
decidir quanto à solicitação de contrato do professor visitante, indicando ao Reitor a efetivação 
da contratação como o resultado do processo seletivo, baseada nos documentos e informações 
descritos no Artigo 3°, além da ata do processo seletivo, Curriculum Vitae e projeto de pesquisa 
do candidato selecionado. 
 
 Art. 5° - Ao final do contrato, o professor deve apresentar, à Direção do Campus, um 
relatório detalhado das atividades realizadas previstas no Artigo 3°, itens II e III, acompanhado 
de aprovação do Colegiado de Curso ou do Colegiado das Pró-Reitorias. 
 Parágrafo Único - As publicações científicas e outros produtos ou documentos relativos 
à pesquisa desenvolvida durante o período do contrato deverão, necessariamente, conter a 
associação do nome do professor visitante à UFT e serem anexados ao relatório. 
 
 Art. 6° - A solicitação de renovação de contrato, quando couber, é de iniciativa dos 
Colegiados de Curso e/ou Pró-Reitorias, devendo conter um único pedido por solicitação e 
incluir os mesmos documentos listados no Artigo 3°, porém relativos à renovação de contrato. 
§ 1°. Não deve ser incluído o documento citado no inciso VII do Artigo 3°. 
§ 2°. Deve ser apresentado relatório detalhado das atividades realizadas (segundo o 
previsto no Artigo 5°). 
 Art. 7° - Cabe ao Colegiado das Pró-Reitorias apreciar e decidir quanto à homologação 
da contratação do professor visitante, baseado nos documentos e informações descritos no Artigo 
6°, indicando ao Reitor a renovação. 
 Art. 8° - É vedada a contratação de servidores da administração direta ou indireta da 
União, dos Estados, do Distrito Federal e dos Municípios, bem como empregados ou servidores 
das suas subsidiárias ou controladas (Art.6° da Lei n° 8.745). 
 Art 9° - As contratações de que trata esta resolução serão realizadas em regime de 
dedicação exclusiva. 
§ 1°. Em caso excepcional e devidamente justificado, a critério do Colegiado das Pró-Reitorias, 
pode ocorrer contratação em regime de 40 (quarenta) horas. 
§ 2°. No caso previsto no §1°, o Colegiado de Curso deverá solicitar autorização prévia 
do Colegiado das Pró-Reitorias para publicação do edital. 
 
 Art. 10 - O nível de remuneração dos professores visitantes contratados nos termos desta 
resolução é fixado pela Gerência de Recursos Humanos, a partir da análise do Curriculum Vitae 
do candidato, obedecendo à equivalência atualizada com os níveis salariais da carreira do 
Magistério Superior Federal. 
 Art. 11 - Os processos de contratação, ou de renovação de contrato, previstos nesta 
resolução, devem ser encaminhados pelo Diretor do Campus ao Colegiado das Pró-Reitorias e 
este encaminhará ao Reitor, com antecedência mínima de 30 (trinta) dias da data prevista para o 
início do contrato ou renovação do mesmo. O Colegiado das Pró-Reitorias também poderá 
encaminhar ao Reitor um pedido de contratação e/ou renovação que julgar necessário, com 
antecedência mínima de 30 (trinta) dias da data prevista para o início do contrato ou renovação 
do mesmo. 
 Art. 12 - Ao professor visitante ficam vedadas as atividades administrativas e de 
representação na UFT. 
 Art. 13 - Os casos omissos serão analisados pelo Conselho de Ensino, Pesquisa e 
Extensão – CONSEPE. 
 Art. 14 - A presente Resolução entra em vigor a partir desta data, revogando-se as 
disposições em contrário.
"""

# Processamento do texto com spaCy
doc = nlp(texto)


# Função para extrair triplas SPO
def extrair_triplas(doc):
    triplas = []
    sujeito = None
    predicado = None
    objeto = None

    for token in doc:
        if token.text == '-' and sujeito and predicado and objeto:
            triplas.append((sujeito, predicado, objeto))
            sujeito = None
            predicado = None
            objeto = None
        elif sujeito is None:
            sujeito = token.text
        elif predicado is None:
            predicado = token.text
        else:
            if objeto is None:
                objeto = token.text
            else:
                objeto += " " + token.text

    return triplas

# Extrair triplas do texto
triplas_extraidas = extrair_triplas(doc)

# Imprimir as triplas
for tripla in triplas_extraidas:
    print(tripla)
