
#Faça uma função retira_pontuacao que, dada uma frase, retorne a frase onde todos os caracteres de pontuação 
(incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase) tenham sido substituídos por espaço.


def retira_pontuacao(f):
'''Função que substitui as pontuaçoes por espaço'''
    
    t= f.split(',')
    f= ' '.join(t)
    
    t= f.split('.')
    f= ' '.join(t)
    
    t= f.split(';')
    f= ' '.join(t)
    
    t= f.split('!')
    f=' '.join(t)
    
    t= f.split('-')
    f= ' '.join(t)
    
    t= f.split(':')
    f= ' '.join(t)
    
    t= f.split('?')
    f= ' '.join(t)
    
    return f
