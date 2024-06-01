const Contract1 = artifacts.require('Contract1');
const { expect } = require('chai');

describe('Contract1', function () {
  let contract;

  beforeEach(async function () {
    contract = await Contract1.new();
  });

  describe('set()', function () {
    it('should set the stored data', async function () {
      await contract.set(42);
      expect(await contract.get()).to.equal(42);
    });
  });
});
