import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#CELSIUS TO FAHRENHEIT 

def regurlar_algorithm(c): #regular algorithm to solve the conversion
    f = c* 1.8 + 32
    return f


#---------------------------------------------------------------------------------------Naural Network


#preparing input (celsius), output (fahrenheit) to train the model
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float) 
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

#seting layers. unit is a neuron
#input_shape the input of a neron

#capa = tf.keras.layers.Dense(units=1, input_shape=[1])

#setiing model 
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
theoutput = tf.keras.layers.Dense(units=1) 

myModel = tf.keras.Sequential([oculta1, oculta2, theoutput]) #seting 3 neurons to the model 

#training
myModel.compile(          #model Adam to optimize leanning with 0,1 whight of learning (this weight is used to adjust weight and bias)
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Training model. . .")
historial= myModel.fit(celsius, fahrenheit, epochs=1000, verbose=False) #epochs are the iterations of how many times it will be compiled to lean about each iteartion

print("¡Model already trained!")


plt.xlabel(" #Epoca")
plt.ylabel("magnitud de perdida")
plt.plot(historial.history["loss"])
plt.show()


print(f"\n\n\n regular algorithm: {regurlar_algorithm(100.0)} fahrenheit")
print("prediction--------------------")
result = myModel.predict([100.0])
print(f"prediction: {result} fahrenheit")

# print(f"variables of the model: \n{capa.get_weights()}")
print(f"variables of the oculta1: \n{oculta1.get_weights()}")
print(f"variables of the oculta1: \n{oculta2.get_weights()}")
print(f"variables of the oculta1: \n{theoutput.get_weights()}")