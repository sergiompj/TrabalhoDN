import tensorflow as tf

v = tf.Variable([0.0])
with tf.GradientTape() as g:
    loss = tf.constant(v + v)
g.gradient(loss, v).numpy()

print(loss)