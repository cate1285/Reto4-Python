import json

def convert_json(inf_months_dict):
  data = json.loads(inf_months_dict)
  return data


def filter_months(meses_pagos,meses_usuario):
  list_months=[]
  sum_values=0
  for mes in meses_usuario:
    if mes in meses_pagos.keys():
      list_months.append(mes)
      sum_values+=meses_pagos.get(mes)
  return list_months, sum_values


inf_months_dict=(input())
inf_meses_pagos=convert_json(inf_months_dict)
inf_meses_usuario_financiera= (input()).split()
x,y=filter_months(inf_meses_pagos,inf_meses_usuario_financiera)
print(y)
print(" ".join(x))
