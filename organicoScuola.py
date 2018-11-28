import pandas as pd
import numpy as np

df_maestre = pd.read_csv('/home/gabriele/Documenti/Università/Statistica/Dataset/ORGANICO_VIA_LIBERTA.csv', sep = ';')
#print(df_maestre)

maestre_ruolo = df_maestre[df_maestre['QUALIFICA'] == 'RUOLO']

#print(maestre_ruolo)
posto_normale_comune_ruolo = maestre_ruolo[(maestre_ruolo['TIPO POSTO'] == 'COMUNE') | (maestre_ruolo['TIPO POSTO'] == 'NORMALE')]
#print(posto_normale_comune_ruolo)
full_ruolo = posto_normale_comune_ruolo[((posto_normale_comune_ruolo['SCUOLA'] == 'PRIMARIA') & (posto_normale_comune_ruolo['ORE'] == '24')) |
                            ((posto_normale_comune_ruolo['SCUOLA'] == 'INFANZIA') & (posto_normale_comune_ruolo['ORE'] == '25')) |
                            ((posto_normale_comune_ruolo['SCUOLA'] == 'SECONDARIA PRIMO GRADO') & (posto_normale_comune_ruolo['ORE'] == '18'))]
#print(full_ruolo)

posto_sostegno_ruolo = maestre_ruolo[maestre_ruolo['TIPO POSTO'] == 'SOSTEGNO']
#print(posto_sostegno_ruolo)
#print(posto_sostegno_ruolo.count())
posto_normale_comune = df_maestre[(df_maestre['TIPO POSTO'] == 'NORMALE') | (df_maestre['TIPO POSTO'] == 'COMUNE')]
#print(posto_normale_comune)
posto_normale_comune_annuale = posto_normale_comune[(posto_normale_comune['QUALIFICA'] == 'FIT 31-08') |
                                                    (posto_normale_comune['QUALIFICA'] == '31-ago')]
#print(posto_normale_comune_annuale)
posto_sostegno = df_maestre[df_maestre['TIPO POSTO'] == 'SOSTEGNO']
#print(posto_sostegno)
posto_normale_comune_30_giugno = posto_normale_comune[posto_normale_comune['QUALIFICA'] == '30-giu']
#print(posto_normale_comune_30_giugno)

posto_sostegno_30_giugno = posto_sostegno[posto_sostegno['QUALIFICA'] == '30-giu']
#print(posto_sostegno_30_giugno)

maestre_religione = df_maestre[df_maestre['MATERIA'] == 'RELIGIONE']
print(maestre_religione)

posto_normale_comune_no_ruolo =posto_normale_comune[posto_normale_comune['QUALIFICA'] != 'RUOLO']
#print(posto_normale_comune_no_ruolo)
