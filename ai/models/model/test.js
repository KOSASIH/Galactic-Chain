const tf = require('@tensorflow/tfjs');
const model = require('./galactic_chain_model');

async function test() {
  const inputData = tf.tensor2d([5], [1, 1]);
  const output = model.predict(inputData);

  console.log(`Output: ${output.dataSync()[0]}`);
}

test();
