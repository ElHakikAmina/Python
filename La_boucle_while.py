p_age= 500000
p_kech=1000000
nbr_ans =0
while p_kech>p_age:
    p_age= p_age*1.08
    p_kech= p_kech+50000
    nbr_ans = nbr_ans+1
print("Agadir dépassera marrakech aprés",nbr_ans,"ans")