from get_dati import *
from get_file import *
from get_dict import *
from print_latex import *

path='/Users/salvatoreprioli/Desktop/sdu/nilered_PROJ/ElectrStr/'


gs=getdataGSDICT(path)
es=getdataESDICT(path)
es_opt=getdataOPTESDICT(path)
tpa=getdataTPADICT(path)
PrintDataLaTex(gs, es, es_opt, tpa)
PrintDipolesLatex(es, es_opt, gs)
