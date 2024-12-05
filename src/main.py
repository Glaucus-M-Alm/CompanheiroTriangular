import flet as ft
from sistema_rpg import SistemaRPG

if __name__ == "__main__":
    app = SistemaRPG()
    ft.app(target=app.iniciar)  # A função 'iniciar' será chamada com o argumento 'page' automaticamente.
