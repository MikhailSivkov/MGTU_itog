import pickle

print('Введите входящие параметры, а я попрубую предсказать глубину и ширину шва (вводим только числа)')
IW = int(input('Введите IW(46) : '))
IF = int(input('Введите IF(140) : '))
VW = int(input('Введите VW(8) : '))
FP = int(input('Введите FP(80) : '))
load_model = pickle.load(open('model_rfc_pkl.pkl', 'rb'))

# Выполняем вычисления для глубины шва и ширины шва
predicted_result = load_model.predict([[IW, IF, VW, FP]])
depth = round(predicted_result[0][0], 2)
width = round(predicted_result[0][1], 2)
print (f'Глубина шва: {depth}\nШирина шва: {width}')

