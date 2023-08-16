from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


red_bayes = BayesianNetwork([('Lluvia','Mantenimiento'),('Lluvia', 'Tren'),
                            ('Mantenimiento','Tren'),
                            ('Tren','Reunion')])

lluvia_cpd = TabularCPD(variable = 'Lluvia',
                        variable_card=3,
                        values=[[0.7],[0.2],[0.1]],
                        state_names={'Lluvia':['nula','ligera','fuerte']})

mantenimiento = {'si':[0.4, 0.2 , 0.1] ,'no':[0.6, 0.8, 0.9]}
 
mantenimiento_cpd = TabularCPD(variable='Mantenimiento',
                            variable_card= len(mantenimiento.keys()),
                            values=[mantenimiento[key] for key in mantenimiento.keys()],
                            evidence= ['Lluvia'],
                            evidence_card=[3],                                        
                            state_names={'Mantenimiento': list(mantenimiento.keys()),
                                        'Lluvia':['nula','ligera','fuerte'],
                                        },
                            )

tren= {'a tiempo':[0.8,0.9,0.6,0.7,0.4,0.5],'demorado':[0.2,0.1,0.4,0.3,0.6,0.5]}

tren_cpd = TabularCPD(variable='Tren',
                            variable_card= len(tren.keys()),
                            values=[tren [key] for key in tren.keys()],
                            evidence= ['Lluvia','Mantenimiento'],
                            evidence_card=[3,2],                                        
                            state_names= {'Tren': list(tren.keys()),
                                        'Lluvia':['nula','ligera','fuerte'],
                                        'Mantenimiento': list(mantenimiento.keys())
                                        }
                            )

reunion={'asistir':[0.9,0.6], 'no asistir':[0.1,0.4]}
reunion_cpd=TabularCPD(variable='Reunion',
                            variable_card= len(reunion.keys()),
                            values=[reunion[key] for key in reunion.keys()],
                            evidence= ['Tren'],
                            evidence_card=[2],                                        
                            state_names={'Reunion': list(reunion.keys()),
                                        'Tren': list(tren.keys())
                                        },
                            )

red_bayes.add_cpds(lluvia_cpd,mantenimiento_cpd,tren_cpd,reunion_cpd)
inferencia = VariableElimination(red_bayes)
consulta_1= inferencia.query(variables=['Lluvia'],
                            evidence={'Reunion':'asistir'})

print(consulta_1)