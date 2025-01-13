import flet as ft
from personagem import Personagem
from classes import Lenhador, Investigador, Estudioso, PopStar, GolpistaEmpresario, Atleta, Riquinho
from database import Database

def main(page: ft.Page):
    # Criar os campos de entrada para o formulário
    nome_input = ft.TextField(label="Nome do Personagem", autofocus=True)  # Usando TextField para nome
    nivel_input = ft.TextField(label="Nível", value="1")  # Usando TextField para nível

    # Campos para os atributos
    forca_input = ft.TextField(label="Força", value="0")
    inteligencia_input = ft.TextField(label="Inteligência", value="0")
    rapidez_input = ft.TextField(label="Rapidez", value="0")
    vigor_input = ft.TextField(label="Vigor", value="0")
    aparencia_input = ft.TextField(label="Aparência", value="0")
    daoridade_input = ft.TextField(label="Daoridade", value="0")
    
    # Dropdown para selecionar a classe do personagem
    classe_dropdown = ft.Dropdown(
        label="Classe",
        options=[
            ft.dropdown.Option("Atleta"),
            ft.dropdown.Option("Lenhador"),
            ft.dropdown.Option("Investigador"),
            ft.dropdown.Option("Estudioso"),
            ft.dropdown.Option("PopStar"),
            ft.dropdown.Option("GolpistaEmpresario"),
            ft.dropdown.Option("Riquinho"),
        ]
    )
    
    # Exibir as fichas salvas
    ficha_text = ft.Column()

    # Função para salvar e criar o personagem
    def salvar_personagem(e):
        nome = nome_input.value
        nivel = int(nivel_input.value)  # Convertendo para inteiro
        classe_nome = classe_dropdown.value
        
        # Mapeamento das classes
        if classe_nome == "Atleta":
            classe = Atleta()
        elif classe_nome == "Lenhador":
            classe = Lenhador()
        elif classe_nome == "Investigador":
            classe = Investigador()
        elif classe_nome == "Estudioso":
            classe = Estudioso()
        elif classe_nome == "PopStar":
            classe = PopStar()
        elif classe_nome == "GolpistaEmpresario":
            classe = GolpistaEmpresario()
        elif classe_nome == "Riquinho":
            classe = Riquinho()
        else:
            page.add(ft.Text("Classe inválida"))  # Caso de erro
            return
        
        # Criar personagem
        personagem = Personagem(nome, classe, nivel)
        
        # Atribuir os valores dos atributos
        personagem.atributos[0].valor = int(forca_input.value)
        personagem.atributos[1].valor = int(inteligencia_input.value)
        personagem.atributos[2].valor = int(rapidez_input.value)
        personagem.atributos[3].valor = int(vigor_input.value)
        personagem.atributos[4].valor = int(aparencia_input.value)
        personagem.atributos[5].valor = int(daoridade_input.value)
        
        # Atribuir vida rolada
        personagem.definirVidaRolada(20)  # Atribua a vida rolada de forma adequada
        personagem.calcularDN()
        
        # Salvar no banco de dados
        db = Database()
        db.adicionar_ficha(personagem.__dict__)  # Adicionando o personagem como um dicionário

        # Atualizar exibição das fichas
        fichas = db.listar_fichas()
        ficha_text.controls.clear()  # Limpar exibição anterior
        for ficha in fichas:
            ficha_text.controls.append(ft.Text(str(ficha)))

        # Atualizar a tela
        page.update()

    # Criar o botão de salvar
    salvar_button = ft.ElevatedButton("Salvar Ficha", on_click=salvar_personagem)

    # Adicionar os componentes na tela
    page.add(
        nome_input,
        nivel_input,
        classe_dropdown,
        forca_input,
        inteligencia_input,
        rapidez_input,
        vigor_input,
        aparencia_input,
        daoridade_input,
        salvar_button,
        ficha_text
    )

# Executar o aplicativo
ft.app(target=main)
