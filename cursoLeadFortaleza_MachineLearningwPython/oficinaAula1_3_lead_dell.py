from datetime import date, datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')
hoje = date.today()
#print(hoje)  # 2021-05-14

aniversarios = ['01/02/1990', '22 de Maio de 1991', '04/Abr/1995', '1995-Outubro-10', '12 Julho 1989', '16 de Junho de 1987', '04/07/1990']
niverFormatados = []
for niver in aniversarios:
    try:
        data = datetime.strptime(niver, '%d/%m/%Y')
        #print(data.strftime('%d/%m/%Y'))
        niverFormatados.append(data)
    except ValueError:
        try:
            data = datetime.strptime(niver, '%d de %B de %Y')
            #print(data.strftime('%d/%m/%Y'))
            niverFormatados.append(data)
        except ValueError:
            try:
                data = datetime.strptime(niver, '%d/%m/%Y')
                #print(data.strftime('%d/%m/%Y'))
                niverFormatados.append(data)
            except ValueError:
                try:
                    data = datetime.strptime(niver, '%d/%b/%Y')
                    #print(data.strftime('%d/%m/%Y'))
                    niverFormatados.append(data)
                except ValueError:
                    try:
                        data = datetime.strptime(niver, '%Y-%B-%d')
                        #print(data.strftime('%d/%m/%Y'))
                        niverFormatados.append(data)
                    except ValueError:
                        try:
                            data = datetime.strptime(niver, '%d %B %Y')
                            #print(data.strftime('%d/%m/%Y')) #data
                            niverFormatados.append(data)
                        except Exception as e:
                            print(e)
                            
#print(niverFormatados[4].strftime('%m')) #mês
#print(niverFormatados[4].month)
print(sorted(niverFormatados, key=lambda d: (d.month, d.day)))
if hoje.month and hoje.day in niverFormatados:
    print(f'Hoje, {diaSemana} {dia} de {mes} de {anoAtual}, tem aniversário!')