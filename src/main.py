import flet as ft
from personagem import Personagem, Atributo
from atributos import Atributo
from classes import Lenhador, Investigador, Estudioso, PopStar, GolpistaEmpresario, AtletaVigor, AtletaForca, Riquinho
from database import Database

def main(page: ft.Page):
    page.scroll = "auto"  # Permitir rolagem na página

    ficha_text = ft.Column()

    # Atualizar exibição das fichas
    def atualizar_fichas():
        db = Database()
        fichas = db.listar_fichas()
        ficha_text.controls.clear()

        for ficha in fichas:
            if isinstance(ficha, dict):  # Garante que ficha é um dicionário
                ficha_text.controls.append(
                    ft.Row(
                        controls=[
                            ft.Text(ficha['nome']),
                            ft.ElevatedButton("Ver Detalhes", on_click=lambda e, ficha=ficha: ver_detalhes(ficha)),
                            ft.ElevatedButton("Editar", on_click=lambda e, ficha=ficha: editar_ficha(ficha)),
                            ft.ElevatedButton("Excluir", on_click=lambda e, id_ficha=ficha['id']: excluir_ficha(id_ficha)),
                        ]
                    )
                )
        page.update()

    # Função para excluir uma ficha
    def excluir_ficha(id_ficha):
        db = Database()
        db.excluir_ficha(id_ficha)
        atualizar_fichas()  # Atualiza a lista de fichas na interface

    # Exibir detalhes da ficha
    def ver_detalhes(ficha):
        detalhes_text = ft.Column()
        detalhes_text.controls.append(ft.Text(f"Nome: {ficha['nome']}"))
        detalhes_text.controls.append(ft.Text(f"Nível: {ficha['nivel']}"))
        detalhes_text.controls.append(ft.Text(f"Classe: {ficha['classe']}"))

        for atributo in ficha['atributos']:
            detalhes_text.controls.append(ft.Text(f"{atributo['nome']}: {atributo['valor']}"))

        detalhes_text.controls.append(ft.Text(f"Vida Rolada: {ficha['vida_rolada']}"))
        detalhes_text.controls.append(ft.Text(f"Vida: {ficha['vida']}"))
        detalhes_text.controls.append(ft.Text(f"Defesa Natural (DN): {ficha['dn']}"))
        detalhes_text.controls.append(ft.Text(f"Proficiências: {ficha['proficiencias']}"))

        voltar_button = ft.ElevatedButton("Voltar", on_click=lambda e: voltar())
        detalhes_view = ft.Column(controls=[detalhes_text, voltar_button])

        page.controls.pop()
        page.add(detalhes_view)
        page.update()

    # Função para editar uma ficha
    def editar_ficha(ficha):
        nome_input = ft.TextField(label="Nome do Personagem", value=ficha['nome'])
        nivel_input = ft.TextField(label="Nível", value=str(ficha['nivel']))

        atributos_inputs = [
            ft.TextField(label=atributo['nome'], value=str(atributo['valor']))
            for atributo in ficha['atributos']
        ]

        vida_rolada_input = ft.TextField(label="Vida Rolada", value=str(ficha['vida_rolada']))

        classe_dropdown = ft.Dropdown(
            label="Classe",
            options=[ft.dropdown.Option("AtletaVigor"),
                     ft.dropdown.Option("AtletaForca"),
                     ft.dropdown.Option("Lenhador"),
                     ft.dropdown.Option("Investigador"),
                     ft.dropdown.Option("Estudioso"),
                     ft.dropdown.Option("PopStar"),
                     ft.dropdown.Option("GolpistaEmpresario"),
                     ft.dropdown.Option("Riquinho")],
            value=ficha['classe']
        )

        classes_disponiveis = {
            "AtletaVigor": AtletaVigor,
            "AtletaForca": AtletaForca,
            "Lenhador": Lenhador,
            "Investigador": Investigador,
            "Estudioso": Estudioso,
            "PopStar": PopStar,
            "GolpistaEmpresario": GolpistaEmpresario,
            "Riquinho": Riquinho
        }

        def salvar_edicao(e):
            db = Database()
            nome = nome_input.value if nome_input.value else ficha['nome']
            nivel = int(nivel_input.value) if nivel_input.value else ficha['nivel']
            classe_nome = classe_dropdown.value if classe_dropdown.value else ficha['classe']

            if not classe_nome:
                page.add(ft.Text("Erro: Selecione uma classe antes de salvar."))
                return

            classe = classes_disponiveis.get(classe_nome)
            if not classe:
                page.add(ft.Text("Erro: Classe inválida."))
                return

            personagem = Personagem(nome, classe, nivel)
            for i, atributo in enumerate(personagem.atributos):
                novo_valor = int(atributos_inputs[i].value) if atributos_inputs[i].value else atributo.valor
                atributo.valor = novo_valor

            personagem.definirVidaRolada(int(vida_rolada_input.value) if vida_rolada_input.value else ficha['vida_rolada'])
            personagem.calcularDN()

            db.editar_ficha(ficha['id'], personagem.to_dict())
            atualizar_fichas()

            page.controls.pop()
            page.add(inicial_view)
            page.update()

        salvar_button = ft.ElevatedButton("Salvar Alterações", on_click=salvar_edicao)
        edicao_view = ft.Column(
            controls=[nome_input, nivel_input, classe_dropdown, *atributos_inputs, vida_rolada_input, salvar_button]
        )

        page.controls.pop()
        page.add(edicao_view)
        page.update()

    # Função para voltar à visão inicial
    def voltar():
        page.controls.pop()
        page.add(inicial_view)
        page.update()

    # Exibir formulário de criação de ficha
    def exibir_formulario(e):
        nome_input = ft.TextField(label="Nome do Personagem", autofocus=True)
        nivel_input = ft.TextField(label="Nível", value="1")
        atributos_inputs = [ft.TextField(label=nome, value="") for nome in ["Força", "Inteligência", "Rapidez", "Vigor", "Aparência", "Daoridade"]]
        vida_rolada_input = ft.TextField(label="Vida Rolada", value="")
        classe_dropdown = ft.Dropdown(label="Classe", options=[ft.dropdown.Option("AtletaVigor"), ft.dropdown.Option("AtletaForca"), ft.dropdown.Option("Lenhador"), ft.dropdown.Option("Investigador"), ft.dropdown.Option("Estudioso"), ft.dropdown.Option("PopStar"), ft.dropdown.Option("GolpistaEmpresario"), ft.dropdown.Option("Riquinho")])

        classes_disponiveis = {
            "AtletaVigor": AtletaVigor,
            "AtletaForca": AtletaForca,
            "Lenhador": Lenhador,
            "Investigador": Investigador,
            "Estudioso": Estudioso,
            "PopStar": PopStar,
            "GolpistaEmpresario": GolpistaEmpresario,
            "Riquinho": Riquinho
        }

        def salvar_personagem(e):
            db = Database()
            nome = nome_input.value
            nivel = int(nivel_input.value)
            classe = classe_dropdown.value
            atributos = [
                {"nome": nome, "valor": int(atributos_inputs[i].value) if atributos_inputs[i].value else 0}
                for i, nome in enumerate(["Força", "Inteligência", "Rapidez", "Vigor", "Aparência", "Daoridade"])
            ]
            vida_rolada = int(vida_rolada_input.value) if vida_rolada_input.value else 0

            classe_obj = classes_disponiveis[classe]
            personagem = Personagem(nome, classe_obj, nivel)
            personagem.atributos = [Atributo(attr['nome']) for attr in atributos]
            for i, atributo in enumerate(personagem.atributos):
                atributo.valor = atributos[i]['valor']

            personagem.definirVidaRolada(vida_rolada)
            personagem.calcularDN()

            db.adicionar_ficha(personagem.to_dict())
            atualizar_fichas()

            page.controls.pop()
            page.add(inicial_view)
            page.update()

        salvar_button = ft.ElevatedButton("Salvar Ficha", on_click=salvar_personagem)
        formulario = ft.Column(controls=[nome_input, nivel_input, classe_dropdown, *atributos_inputs, vida_rolada_input, salvar_button])
        page.controls.pop()
        page.add(formulario)
        page.update()

    criar_ficha_button = ft.ElevatedButton("Criar Ficha", on_click=exibir_formulario)
    inicial_view = ft.Column(controls=[criar_ficha_button, ficha_text])
    page.add(inicial_view)
    atualizar_fichas()
    page.update()

# Executar o aplicativo
ft.app(target=main)
