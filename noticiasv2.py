import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Dicionário de sites por estado
sites_por_estado = {
    'Acre': {
        'Site 1 - Acre': 'https://agazetadoacre.com/',
        'Site 2 - Acre': 'https://oriobranco.net/'
        
    },
    'Alagoas': {
        'Site 1 - Alagoas': 'https://d.gazetadealagoas.com.br/',
        'Site 2 - Alagoas': 'https://anoticiaalagoas.com.br/'
    },
    'Amapa': {
        'Site 1 - Amapa': 'https://agazetadoamapa.com.br/',
        'Site 2 - Amapa': 'https://www.diariodoamapa.com.br/'
    },
    'Amazonas': {
        'Site 1 - Amazonas': 'https://d24am.com/diario-do-amazonas/',
        'Site 2 - Amazonas': 'https://www.acritica.com/'
    },
    'Bahia': {
        'Site 1 - Bahia': 'https://www.bahianoticias.com.br/',
        'Site 2 - Bahia': 'https://www.correio24horas.com.br/'
    },
    'Ceara': {
        'Site 1 - Ceara': 'https://diariodonordeste.verdesmares.com.br/',
        'Site 2 - Ceara': 'https://www.opovo.com.br/'
    },
    'Distrito Federal': {
        'Site 1 - Bahia': 'https://www.correiobraziliense.com.br/',
        'Site 2 - Bahia': 'https://jornaldebrasilia.com.br/'
    },
    'Espirito Santo': {
        'Site 1 - Espirito Santo': 'https://www.agazeta.com.br/',
        'Site 2 - Espirito Santo': 'https://euamomeubairro.com.br/'
    },
    'Goiania': {
        'Site 1 - Goiania': 'https://www.dm.com.br/?d=1',
        'Site 2 - Goiania': 'https://jornalcomunidadeemdestaque.com/'
    },
    'Maranhao': {
        'Site 1 - Maranhao': 'https://oimparcial.com.br/',
        'Site 2 - Maranhao': 'https://oprogressonet.com/'
    },
    'Mato Grosso': {
        'Site 1 - Mato Grosso': 'https://www.gazetadigital.com.br/',
        'Site 2 - Mato Grosso': 'https://www.diariodecuiaba.com.br/'
    },
    'Mato Grosso do Sul': {
        'Site 1 - Mato Grosso do Sul': 'https://www.acritica.net/',
        'Site 2 - Mato Grosso do Sul': 'https://correiodoestado.com.br/'
    },
    'Minas Gerais': {
        'Site 1 - Bahia': 'https://www.em.com.br/',
        'Site 2 - Bahia': 'https://www.hojeemdia.com.br/'
    },
    'Para': {
        'Site 1 - Para': 'https://carajasojornal.com.br/',
        #'Site 2 - Bahia': 'sem site no momento'
    },
    'Paraiba': {
        'Site 1 - Paraiba': 'https://portalcorreio.com.br/',
        'Site 2 - Bahia': 'https://jornaldaparaiba.com.br/'
    },
    'Pernambuco': {
        'Site 1 - Pernambuco': 'https://www.diariodepernambuco.com.br/',
        'Site 2 - Pernambuco': 'https://jc.ne10.uol.com.br/'
    },
    'Piaui': {
        'Site 1 - Piaui': 'https://www.jornaldogranderecife.com.br/',
        'Site 2 - Piaui': 'https://www.portalcorreiodonorte.com.br/'
    },
    'RJ': {
        'Site 1 - RJ': 'https://oglobo.globo.com/',
        'Site 2 - RJ': 'https://odia.ig.com.br/'
    },
    'Rio Grande do Norte': {
        'Site 1 - Rio Grande do Norte': 'https://agorarn.com.br/',
        'Site 2 - Rio Grande do Norte': 'https://tribunadonorte.com.br/'
    },
    'Rio Grande do Sul': {
        'Site 1 - Rio Grande do Sul': 'https://gauchazh.clicrbs.com.br/',
        'Site 2 - Rio Grande do Sul': 'https://www.correiodopovo.com.br/'
    },
    'Rondonia': {
        'Site 1 - Rondonia': 'https://correiodenoticia.com.br/',
        'Site 2 - Rondonia': 'https://www.diariodaamazonia.com.br/'
    },
    'Santa Catarina': {
        'Site 1 - Santa Catarina': 'https://www.nsctotal.com.br/cidades/florianopolis',
        'Site 2 - Santa Catarina': 'https://www.nsctotal.com.br/veiculos/hora'
    },
    'SP': {
        'Site 1 - SP': 'https://agora.folha.uol.com.br/',
        'Site 2 - SP': 'https://www.metroworldnews.com.br/'
    },
    'Sergipe': {
        'Site 1 - Bahia': 'https://www.jornaldacidade.net/',
        'Site 2 - Bahia': 'https://jornaldodiase.com.br/'
    },
    'Tocantins': {
        'Site 1 - Tocantins': 'https://conexaoto.com.br/',
        'Site 2 - Tocantins': 'https://conexaoto.com.br/'
    }
 }

def get_all_links(url):
    # Faz a solicitação HTTP para obter o conteúdo da página
    response = requests.get(url)

    # Verifica se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Analisa o conteúdo HTML da página usando BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontra todos os elementos <a> (links) na página
        links = soup.find_all('a', href=True)

        # Lista para armazenar os links absolutos
        absolute_links = []
        for link in links:
            # Converte os links relativos para links absolutos
            absolute_link = urljoin(url, link['href'])
            absolute_links.append(absolute_link)

        return absolute_links
    else:
        # Se a solicitação falhar, imprime uma mensagem de erro
        print(f"Failed to fetch content from {url}")
        return []
while True:
    # Mostra os estados disponíveis para o usuário escolher
    print("Estados disponíveis:")
    for idx, estado in enumerate(sites_por_estado, start=1):
        print(f"{idx}. {estado}")

    # Solicita ao usuário que escolha um estado
    opcao_estado = int(input("Escolha o número correspondente ao estado que deseja analisar: "))

    # Verifica se a opção do estado escolhido é válida
    if 1 <= opcao_estado <= len(sites_por_estado):
        estado_selecionado = list(sites_por_estado.keys())[opcao_estado - 1]
        print(f"Você escolheu o estado de {estado_selecionado}")

        # Mostra os sites disponíveis para o estado selecionado
        print(f"Sites disponíveis em {estado_selecionado}:")
        sites_estado = sites_por_estado[estado_selecionado]
        for idx, (site_nome, _) in enumerate(sites_estado.items(), start=1):
            print(f"{idx}. {site_nome}")

        # Solicita ao usuário que escolha um site
        opcao_site = int(input("Escolha o número correspondente ao site que deseja analisar: "))

        # Verifica se a opção do site escolhido é válida
        if 1 <= opcao_site <= len(sites_estado):
            site_escolhido = list(sites_estado.values())[opcao_site - 1]
            print(f"Você escolheu analisar o site: {list(sites_estado.keys())[opcao_site - 1]}")

            # Obtém todos os links da página escolhida pelo usuário
            all_links = get_all_links(site_escolhido)

            # Nome do arquivo para salvar os links
            file_name = f'links_{estado_selecionado.lower().replace(" ", "_")}_{list(sites_estado.keys())[opcao_site - 1].lower().replace(" ", "_")}.txt'

            # Escreve os links no arquivo de texto
            with open(file_name, 'w') as file:
                for link in all_links:
                    file.write(link + '\n')

            print(f"Os links foram salvos com sucesso no arquivo '{file_name}'")
        else:
            print("Opção inválida. Escolha um número correspondente a um dos sites listados.")
    else:
        print("Opção inválida. Escolha um número correspondente a um dos estados listados.")

    continuar = input("Deseja fazer uma nova pesquisa? (Digite 's' para sim ou qualquer outra tecla para sair): ")
    if continuar.lower() != 's':
        break
