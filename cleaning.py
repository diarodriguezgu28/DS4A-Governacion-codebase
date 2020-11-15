import pandas as pd

############# Cleaning Camaras de Comercio Municipios

# CC Buenaventura
df_c_c_btura_A_M = pd.read_excel(r"c.c. btura A M.xls")
df_Buenaventura = df_c_c_btura_A_M.dropna(how="all",axis=1)

# CC Cartago
df_CARTAGOAM = pd.read_excel(r"CARTAGO A M.xlsx")
df_Cartago = df_CARTAGOAM.dropna(how="all",axis=1)

# CC Cartago PyG
df_CCCARTAGOCONPYGAM = pd.read_excel(r"CC CARTAGO CON PYG A M.xlsx")
df_Cartago_pyg = df_CCCARTAGOCONPYGAM.dropna(how="all",axis=1)

# CC Buga
df_CCBUGAAM = pd.read_excel(r"CC BUGA A M.xlsx")
df_Buga = df_CCBUGAAM.dropna(how="all",axis=1)

# CC Cali
df_ccCaliAM = pd.read_excel(r"cc Cali AM.xlsx")
df_Cali = df_ccCaliAM.dropna(how="all",axis=1)

# CC Palmira
df_ccpalmiraAM = pd.read_excel(r"cc palmira A M.xlsx", skiprows=1)
df_Palmira = df_ccpalmiraAM.dropna(how="all",axis=1)

# CC Sevilla
df_CCSEVILLAAM = pd.read_excel(r"CC SEVILLA A M.xlsx")
df_Sevilla = df_CCSEVILLAAM.dropna(how="all",axis=1)

# CC Sevilla PyG
df_sevillaconAMconpyg = pd.read_excel(r"sevilla con A M  con pyg.xlsx")
df_Sevilla_pyg = df_sevillaconAMconpyg.dropna(how="all",axis=1)

# CC Tulua
df_cctuluaAM = pd.read_excel(r"cc tulua A M.xlsx")
df_Tulua = df_cctuluaAM.dropna(how="all",axis=1)

########### Cleaning Actividades economicas y estampillas

#Contribucion al deporte
df_contribucionAM = pd.read_excel(r"contribucion  A M.xlsx")
df_Contrib_deporte = df_contribucionAM.dropna(how="all",axis=1)

#Licores
df_DECLARACIONNaleImportado2015al2019AM = pd.read_excel(r"DECLARACION Nal e Importado 2015 al 2019  AM.xlsx", skiprows=5)
df_Licores = df_DECLARACIONNaleImportado2015al2019AM.dropna(how="all",axis=1)

#Deguello
df_deguelloAM= pd.read_excel(r"deguello  A M.xlsx")
df_Deguello = df_deguelloAM.dropna(how="all",axis=1)

#Formato 240
df_form240AM = pd.read_excel(r"form 240 AM.xlsx")
df_240 = df_form240AM.dropna(how="all",axis=1)

#Formato 110
df_formato110AM = pd.read_excel(r"formato 110 AM.xlsx")
df_110 = df_formato110AM.dropna(how="all",axis=1)

#Formato 210
df_formato210AM = pd.read_excel(r"formato 210 A M.xlsx")
df_210  = df_formato210AM.dropna(how="all",axis=1)

#Formato 210
df_formato230AM = pd.read_excel(r"formato 230 AM.xlsx")
df_230 = df_formato230AM.dropna(how="all",axis=1)

#Loterias
df_loterias_A_M = pd.read_excel(r"loterias  A M.xlsx")
df_Loterias = df_loterias_A_M.dropna(how="all",axis=1)

#Relacion de Ventas
df_RELACIONDEVEntasyPD2015AL2019am = pd.read_excel(r"RELACION DE VEntas y PD 2015 AL 2019 a m.xlsx")
df_Relacion_ventas = df_RELACIONDEVEntasyPD2015AL2019am.dropna(how="all",axis=1)

#Sobretasa Gasolina
df_sobretasaalagasolinaAM= pd.read_excel(r"sobretasa a la gasolina  A M.xlsx")
df_Gasolina = df_sobretasaalagasolinaAM.dropna(how="all",axis=1)

#Ventas
df_ventas300AM = pd.read_excel(r"ventas 300 A M.xlsx")
df_Ventas = df_ventas300AM.dropna(how="all",axis=1)
