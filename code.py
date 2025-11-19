import my_functions as mf

salarios = mf.read_json("data/escalas_salariales.json")
   
def salary(file = salarios):
   for i in range(0,32):
     print(f"{i} | 44 horas: {file['44_horas'][i]} | 40 horas : {file['40_horas'][i]}")

