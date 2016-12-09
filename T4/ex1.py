# Exercício 1: Simular SI, SIR e SIS nos modelos BA e ER, usando transmissão reativa

import constantes as const
import epidemia
import matplotlib.pyplot as plt

def ex1 (BA, ER):
    for modelo in ['si', 'sis', 'sir']:
        nome = 'BA-reativo-' + modelo
        print ('ex1 - Processando: ' + nome)
        inf, _, _ = epidemia.reativo (BA, modelo, const.num_iter_reativo, const.beta_reativo, const.mi_reativo)
        # plot da proporção de infectados no reativo
        plt.figure (nome)
        plt.clf ()
        plt.plot (inf, 'b-')
        plt.title ('Simulação reativa de epidemia na rede BA usando modelo ' + modelo)
        plt.xlabel ('t')
        plt.ylabel ('Infectados')
        plt.savefig ('figuras/{}.png'.format (nome))

        nome = 'ER-reativo-' + modelo
        print ('ex1 - Processando: ' + nome)
        inf, _, _ = epidemia.reativo (ER, modelo, const.num_iter_reativo, const.beta_reativo, const.mi_reativo)
        # plot da proporção de infectados no reativo
        plt.figure (nome)
        plt.clf ()
        plt.plot (inf, 'b-')
        plt.title ('Simulação reativa de epidemia na rede ER usando modelo ' + modelo)
        plt.xlabel ('t')
        plt.ylabel ('Infectados')
        plt.savefig ('figuras/{}.png'.format (nome))
    