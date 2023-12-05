import PySimpleGUI as psg

from funcao import estacoes_do_ano

layout = [
    [psg.Text('Descubra a Estação')],
    [psg.Text('Digite o Dia: '), psg.InputText(key='data')],
    [psg.Text('Digite o Mês: '), psg.InputText(key='data2')],
    [psg.Text('>>>>'), psg.Text('', key='total'), psg.Text('<<<<')],
    [psg.Button('Resultado')],

]

janela = psg.Window('Descubra a Estação', layout)

while True:
    eventos, valores = janela.read()
    if eventos in (psg.WIN_CLOSED,'Exit'):
        break
    elif eventos == 'Limpar':
        janela['data'].update('')
        janela['data2'].update('')
        janela['total'].update('')
        janela['data'].set_focus()
    elif eventos == 'Resultado':
        data = int(valores['data'])
        data2 = int(valores['data2'])
        janela['total'].update(estacoes_do_ano(data, data2))

janela.close()