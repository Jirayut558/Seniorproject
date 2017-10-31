import functools
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import keras.backend as K
from keras.callbacks import ModelCheckpoint

def mean_pred(y_true, y_pred):
    print (y_pred)
    return K.mean(y_pred)
def f1_score(y_true, y_pred, threshold_shift=0):

    # just in case of hipster activation at the final layer
    y_pred = K.clip(y_pred, 0, 1)

    # shifting the prediction threshold from .5 if needed
    y_pred_bin = K.round(y_pred + threshold_shift)

    tp = K.sum(K.round(y_true * y_pred_bin)) + K.epsilon()
    fp = K.sum(K.round(K.clip(y_pred_bin - y_true, 0, 1)))
    fn = K.sum(K.round(K.clip(y_true - y_pred, 0, 1)))

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return 2 * (precision * recall) / (precision + recall +K.epsilon())

def train_model():
    seed = 7
    numpy.random.seed(seed)

    dataset = numpy.loadtxt('trainset.csv',delimiter=',')

    X = dataset[:,0:16]
    Y = dataset[:,16]


    # create model
    model = Sequential()
    model.add(Dense(10, input_dim=16,init='uniform', activation='relu'))
    model.add(Dense(8,init='uniform', activation='relu'))
    model.add(Dense(1,init='uniform', activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy',mean_pred,f1_score])

    filepath = "weights.best.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='accuracy', verbose=1, save_best_only=True, mode='max')
    callbacks_list = [checkpoint]

    model.fit(X, Y, epochs=5000, batch_size=10,shuffle=True,callbacks=callbacks_list)


    scores = model.evaluate(X, Y)
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    #Save model
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model.h5")
    print("Saved model to disk")


def test_model():
    dataset = numpy.loadtxt('trainset.csv', delimiter=',')

    X = dataset[:, 0:4]

    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

    output = loaded_model.predict(X, batch_size=10)
    print (output)
if __name__ == '__main__':
    train_model()