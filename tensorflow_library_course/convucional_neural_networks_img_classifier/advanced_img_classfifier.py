import tensorflow as tf


#simple neuron-------------------------------------------------------------------------------------------------------------------------------
#add convulotion layer
 #convolution (conv(cores, size, inputshape(image-size, chanels//colors)))
#black and white image example:
model = tf.keras.layers.Conv2D(32, (3,3), input_shape(28,28, 1)) #generates 32 resulsts


#color image example
model1 = tf.keras.layers.Conv2D(32, (3,3), input_shape(28,28, 3)) #generates 32 resulsts, chanels are 3, red, green, blue



#Complex Neuron------------------------------------------------------------------------------------------------------------------------------
#this layer has the objective of agroup and reduce the image by it's cores