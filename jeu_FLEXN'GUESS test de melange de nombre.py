tab1=[1,5,9,11,15,19]
tab3=[16,3,12,7,8,13]
tab2=[2,6,10,14,18,20]
tan_princi=[None]*(len(tab1)+len(tab2))
tan_princi[::1]=tab1
#tan_princi[1::2]=tab2
print(tan_princi)
