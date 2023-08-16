from pgmpy.sampling import BayesianModelSampling
from red_bayesiana import red_bayes

inferencia = BayesianModelSampling(red_bayes)
muestras = inferencia.forward_sample(size=100000)

prob_marginales = muestras['Reunion'].value_counts(normalize=True).reset_index()
prob_marginales.columns = ['Estado', 'Probabilidad']
print()
print(prob_marginales)


inferencia_2 = BayesianModelSampling(red_bayes)
muestras_2 = inferencia_2.forward_sample(size=10000)
muestras_envidencia = muestras_2[muestras_2['Tren'] == 'demorado']
#muestras_envidencia_multiple  = muestras_2[(muestras_2['Tren'] == 'demorado')and(muestras_2['Lluvia'] == 'ligera')]

ocurrencias = muestras_envidencia['Reunion'].value_counts(normalize=True)
print()
print(ocurrencias)