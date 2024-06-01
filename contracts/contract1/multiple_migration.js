const Contract1 = artifacts.require('Contract1');
const Contract2 = artifacts.require('Contract2');

module.exports = function (deployer) {
  deployer.deploy(Contract1)
    .then(() => {
      return deployer.deploy(Contract2, Contract1.address);
    });
};

module.exports.tags = ['Contract1', 'Contract2'];
