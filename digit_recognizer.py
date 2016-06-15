import timeit
from bn_data import bn_transformar
from ampliador import ampliar_set
from RF import rf
from KNN import knn
from democratizador import democratizar


print "Iniciando digit_recognizer"
a = timeit.default_timer()

TRAIN = "train.csv"
TEST = "test.csv"

TRAIN_BN = "_train_bn.csv"
TEST_BN = "_test_bn.csv"

TRAIN_AMPLIADO = "_train_amp.csv" 
TRAIN_AMPLIADO_BN = "_train_amp_bn.csv"

RF_TRAIN_AMPLIADO = "_SUBMIT_RF.csv"
RF_TRAIN_AMPLIADO_BN = "_SUBMIT_RF_BN.csv"

KNN_TRAIN = "_SUBMIT_KNN.csv"
KNN_TRAIN_BN = "_SUBMIT_KNN_BN.csv"

RESULTADO = "Prediccion.csv"

bn_transformar(TRAIN,TRAIN_BN)
bn_transformar(TEST, TEST_BN)

ampliar_set(TRAIN, TRAIN_AMPLIADO)
ampliar_set(TRAIN_BN, TRAIN_AMPLIADO_BN)

rf(TRAIN_AMPLIADO, TEST, RF_TRAIN_AMPLIADO)
rf(TRAIN_AMPLIADO_BN, TEST_BN, RF_TRAIN_AMPLIADO_BN)

knn(TRAIN, TEST, KNN_TRAIN)
knn(TRAIN_BN, TEST_BN, KNN_TRAIN_BN)

submits = [KNN_TRAIN, KNN_TRAIN_BN, RF_TRAIN_AMPLIADO_BN, RF_TRAIN_AMPLIADO]
i_mejorPredictor = 0

democratizar(submits, RESULTADO, i_mejorPredictor)

b = timeit.default_timer()
secs = b - a
m, s = divmod(secs,60)
m = int(m)
s = int(s)

print "Fin digit_recognizer (" + str( m) + ":" + str(s ) + ")"
