const tf = require('@tensorflow/tfjs');
const model = require('./galactic_chain_model');

async function train() {
  const xs = tf.tensor2d([-1, 0, 1, 2, 3, 4], [6, 1]);
  const ys = tf.tensor2d([-3, -1, 1, 3, 5, 7], [6, 1]);

  model.compile({ optimizer: tf.optimizers.sgd(), loss: 'eanSquaredError' });

  await model.fit(xs, ys, { epochs: 100 });

  console.log('Model trained!');
}

train();
