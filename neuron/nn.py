import numpy
from keras.models import Sequential
from keras.layers import Dense


dataset = numpy.loadtxt('trainset.csv',delimiter=',')

X = dataset[:,0:4]
Y = dataset[:,4]

# create model
model = Sequential()
model.add(Dense(4, input_dim=4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(2, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=150, batch_size=10)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))