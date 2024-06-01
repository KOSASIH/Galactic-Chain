const Contract1 = artifacts.require('Contract1');

module.exports = function (deployer) {
  deployer.deploy(Contract1);
};

module.exports.tags = ['Contract1'];
