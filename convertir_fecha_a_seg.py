# agregar columna de timepo en segundos time(s) siendo que la primera columna es un string con la fecha y hora
    
timestr = '01:01:01.33333'
ftr = [3600,60,1]
time_seg = sum([a*b for a,b in zip(ftr, map(int,timestr.split(':')))])

print(time_seg)