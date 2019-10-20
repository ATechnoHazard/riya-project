import numpy as np
from keras import Sequential
from keras.layers import Dense, Activation

from xor_utils import encrypt, decrypt

x_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([0, 1, 1, 0])

model = Sequential()
model.add(Dense(8, input_dim=2))
model.add(Activation('tanh'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.summary()

# compile the model with binary crossentropy as a loss function, and adam optimizer
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=8, epochs=400, verbose=1)
accuracy = model.evaluate(np.array([[0, 1]]), np.array([1]), verbose=1)
model.save("./model/xor.h5")
print('\n', 'Test_Accuracy: ', accuracy[1])

text = input("Enter message to be encrypted: ")
key = input("Enter a key: ")

cipher_text, finalkey = encrypt(text, key)
print("Encrypted text: ", cipher_text)

plaintext = decrypt(cipher_text, finalkey)
print("Decrypted text: ", plaintext)