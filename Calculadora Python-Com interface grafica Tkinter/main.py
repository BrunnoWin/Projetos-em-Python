from calculadora_interface_grafica import Calculadora_Interface_Grafica
from calculadorafatorial import fazer_janela, fazer_display, fazer_label,fazer_buttons
from calculadoratratamento import calcular


def main():
    janela = fazer_janela()
    display = fazer_display(janela, row=1, column=0, columnspan=5, sticky='news')
    display.grid_configure(pady=(0, 10))
    label = fazer_label(janela, row=0, column=0, columnspan=5, sticky='news')
    buttons = fazer_buttons(janela, starting_row=2)

    calculatora_interface_grafica = Calculadora_Interface_Grafica(janela, label, display, buttons, calcular)
    calculatora_interface_grafica.start_interface_grafica()


if __name__ == '__main__':
    main()
