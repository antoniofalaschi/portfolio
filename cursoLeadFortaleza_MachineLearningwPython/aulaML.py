import logging
                                            
    #Criação e configuração do objeto logger
FORMATACAO_MSG = "%(asctime)s | %(levelname)s -> %(message)s"

logging.basicConfig(filename = 'logs.log',
    level = logging.DEBUG,
    format = FORMATACAO_MSG,
    filemode = 'w'),
logger = logging.getLogger()

#Testando o logger
logger.debug('depuração')
logger.info('informação')
logger.warning('aviso')
logger.error('erro')
logger.critical('critico')

logger.info('O programa foi iniciado')
for i in range(3):
    try:
        logger.debug('Iteração número {0}'.format(i))
        print('Vamos dividir dois números!')

        num_1 = int(input('Digite o primeiro número:'))
        logger.debug('O usuário digitou o primeiro número: {0}'.format(num_1))

        num_2 = int(input('Digite o segundo número:'))
        logger.debug('O usuário digitou o segundo número: {0}'.format(num_2))

        resultado = num_1/num_2
        print('O resultado é',resultado)
        logger.debug('O resultado da operação: {0}'.format(resultado))

    except ZeroDivisionError:
        print('Essa operação é impossível')
        logger.warning('O usuário tentou fazer uma divisão por 0')

    except Exception as erro:
        print('Erro, tente novamente!')
        logger.error('Erro não esperado ->'+str(erro))

    finally:
        print('----------------------')

logger.info('O programa foi finalizado')