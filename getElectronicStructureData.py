from get_dati import *
from get_file import *
from get_dict import *
from print_latex import *



gs=getdataGSDICT()
es=getdataESDICT()
es_opt=getdataOPTESDICT()
tpa=getdataTPADICT()
PrintDataLaTex(gs, es, es_opt, tpa)
PrintDipolesLatex(es, es_opt, gs)
