n, k, l, c, d, p, nl, np = map(int, input().split()) # l mililitros c limones d rodajas 
#nl mls que nesecita un compa 1 rodaja np sal 
rodajas = c*d
mls = k*l//nl
sal = p//np
print(min(mls,rodajas,sal)//n)









