import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

const web3 = new Web3(Web3.givenProvider || 'http://localhost:8545');

function App() {
  const [contract, setContract] = useState(null);
  const [storageValue, setStorageValue] = useState(0);

  useEffect(() => {
    const init = async () => {
      const contractAddress = '0xYourContractAddress';
      const contractABI = []; // your contract ABI here
      const contractInstance = new web3.eth.Contract(contractABI, contractAddress);
      setContract(contractInstance);
      const value = await contractInstance.methods.get().call();
      setStorageValue(value);
    };
    init();
  }, []);

  const setValue = async () => {
    const value = Math.floor(Math.random() * 100);
    await contract.methods.set(value).send({ from: '0xYourAccountAddress' });
    const newValue = await contract.methods.get().call();
    setStorageValue(newValue);
  };

  return (
    <div>
      <h1>Simple DApp</h1>
      <p>Storage value: {storageValue}</p>
      <button onClick={setValue}>Set random value</button>
    </div>
  );
}

export default App;
