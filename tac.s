i = 1
L0:
l = 2
t0 = l + 1
x = t0
pp = 1
L1:
aa = 2
t1 = l + 1
bb = t1
d = 1
L2:
dd = 100
t2 = d + 1
d = t2
if d <= 2 goto L2
t3 = pp + 1
pp = t3
if pp <= 2 goto L1
t4 = i + 1
i = t4
if i <= 2 goto L0
