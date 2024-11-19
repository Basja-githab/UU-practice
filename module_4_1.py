from true_math import divide as inf_div
from fake_math import divide as error_div
res1 = error_div(50,10)
res2 = error_div(44,0)
res3 = inf_div(60,3)
res4 = inf_div(78,0)
print(res1, res2, res3, res4)
