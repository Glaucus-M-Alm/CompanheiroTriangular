import flet as ft
from database import Database
from personagem import Personagem

class SistemaRPG:
    def __init__(self):
        self.database = Database()

    def iniciar(self, page: ft.Page):
        page.title = "Sistema RPG"
        page.scroll = "adaptive"

        def atualizar_lista_fichas():
            fichas = self.database.listar_fichas()
            lista.controls.clear()
            for ficha in fichas:
                lista.controls.append(
                    ft.ListTile(
                        title=ft.Text(ficha["nome"]),
                        subtitle=ft.Text(f'Classe: {ficha["classe"]}, Nível: {ficha["nivel"]}'),
                        trailing=ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    tooltip="Editar",
                                    on_click=lambda e, ficha=ficha: abrir_formulario(ficha),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE,
                                    tooltip="Excluir",
                                    on_click=lambda e, nome=ficha["nome"]: excluir_ficha(nome),
                                ),
                            ]
                        ),
                    )
                )
            page.update()

        def criar_ficha(event=None):
            ficha = Personagem(
                nome=input_nome.value,
                classe=input_classe.value,
                nivel=int(input_nivel.value),
                atributos={
                    "inteligência": int(input_inteligencia.value),
                    "vigor": int(input_vigor.value),
                    "carisma": int(input_carisma.value),
                    "destreza": int(input_destreza.value),
                    "aparência": int(input_aparencia.value),
                    "força": int(input_forca.value),
                },
                habilidades=input_habilidades.value.split(","),
            )
            self.database.adicionar_ficha(ficha.to_dict())
            fechar_formulario()

        def excluir_ficha(nome):
            self.database.remover_ficha(nome)
            atualizar_lista_fichas()

        def abrir_formulario(ficha=None):
            if ficha:
                input_nome.value = ficha["nome"]
                input_classe.value = ficha["classe"]
                input_nivel.value = str(ficha["nivel"])
                input_inteligencia.value = str(ficha["atributos"]["inteligência"])
                input_vigor.value = str(ficha["atributos"]["vigor"])
                input_carisma.value = str(ficha["atributos"]["carisma"])
                input_destreza.value = str(ficha["atributos"]["destreza"])
                input_aparencia.value = str(ficha["atributos"]["aparência"])
                input_forca.value = str(ficha["atributos"]["força"])
                input_habilidades.value = ",".join(ficha["habilidades"])
            else:
                limpar_formulario()

            formulario.visible = True
            page.update()

        def fechar_formulario(event=None):
            formulario.visible = False
            atualizar_lista_fichas()

        def limpar_formulario():
            input_nome.value = ""
            input_classe.value = ""
            input_nivel.value = "1"
            input_inteligencia.value = "0"
            input_vigor.value = "0"
            input_carisma.value = "0"
            input_destreza.value = "0"
            input_aparencia.value = "0"
            input_forca.value = "0"
            input_habilidades.value = ""

        lista = ft.Column()

        input_nome = ft.TextField(label="Nome")
        input_classe = ft.TextField(label="Classe")
        input_nivel = ft.TextField(label="Nível", value="1", keyboard_type=ft.KeyboardType.NUMBER)
        input_inteligencia = ft.TextField(label="Inteligência", value="0", keyboard_type=ft.KeyboardType.NUMBER)
        input_vigor = ft.TextField(label="Vigor", value="0", keyboard_type=ft.KeyboardType.NUMBER)
        input_carisma = ft.TextField(label="Carisma", value="0", keyboard_type=ft.KeyboardType.NUMBER)
        input_destreza = ft.TextField(label="Destreza", value="0", keyboard_type=ft.KeyboardType.NUMBER)
        input_aparencia = ft.TextField(label="Aparência", value="0", keyboard_type=ft.KeyboardType.NUMBER)
        input_forca = ft.TextField(label="Força", value="0", keyboard_type=ft.KeyboardType.NUMBER)
        input_habilidades = ft.TextField(label="Habilidades (separadas por vírgula)")

        formulario = ft.Column(
            [
                input_nome,
                input_classe,
                input_nivel,
                input_inteligencia,
                input_vigor,
                input_carisma,
                input_destreza,
                input_aparencia,
                input_forca,
                input_habilidades,
                ft.Row(
                    [
                        ft.ElevatedButton("Salvar", on_click=criar_ficha),
                        ft.ElevatedButton("Cancelar", on_click=fechar_formulario),
                    ]
                ),
            ],
            visible=False,
        )

        page.add(
            ft.Column(
                [
                    ft.Text("Fichas Cadastradas", style="headlineMedium"),
                    lista,
                    ft.ElevatedButton("Criar Ficha", on_click=lambda e: abrir_formulario()),
                    formulario,
                ]
            )
        )

        atualizar_lista_fichas()


if __name__ == "__main__":
    app = SistemaRPG()
    ft.app(target=app.iniciar)
