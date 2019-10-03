#Определите принадлежность хотя бы одной точки заданного множества точек на плоскости внутренней области круга радиуса r, с центром в начале координат.
fTupX=[10,15,6,1,0]
fTupY=[10,15,6,1,0]
print(fTupX,fTupY)
nFin1=len(fTupX) #длина массива X
nFin2=len(fTupY) #длина массива Y
i=0 #старт. знач. счетчик итераций
flag=True #Еще ни одна точка не попала

fR=float(input('Введите радиус круга '))
if nFin1==nFin2 and fR>0:
    while flag and i<=nFin1-1:
        flagF=(fR*fR>fTupX[i]*fTupX[i]+fTupY[i]*fTupY[i])
        if flagF:
            flag=False #Точка попала
            print('Точка с координатами', str(fTupX[i]),str(fTupY[i]),'попадает')
        else
            print('Точка с координатами', str(fTupX[i]),str(fTupY[i]),'не попадает')
        i+=1
else:
    print ('Введите массивы равной длины и положительный радиус')
    
if flag:
    print('Ни одной точки не попадает')
else:
    print('Хотя бы 1 точка попадает')
