import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Web3 from 'web3';
import { EllipticCurve } from '../utils/crypto/elliptic_curve';
import { AIContractEngine } from '../core/smart_contracts/ai_contract';

function App() {
  const [account, setAccount] = useState(null);
  const [contracts, setContracts] = useState([]);
  const [transactions, setTransactions] = useState([]);
  const [ellipticCurve, setEllipticCurve] = useState(new EllipticCurve());
  const [aiContractEngine, setAIContractEngine] = useState(new AIContractEngine());

  useEffect(() => {
    // Initialize Web3 provider
    const web3 = new Web3(new Web3.providers.HttpProvider('https://galactic-chain-node.com'));
    setAccount(web3.eth.accounts[0]);

    // Load contracts and transactions
    web3.eth.getContracts().then(contracts => setContracts(contracts));
    web3.eth.getTransactions().then(transactions => setTransactions(transactions));
  }, []);

  const handleDeployContract = async (contractCode, contractName) => {
    try {
      const contract = await aiContractEngine.deployContract(contractCode, contractName);
      setContracts([...contracts, contract]);
    } catch (error) {
      console.error(error);
    }
  };

  const handleExecuteContract = async (contractName, functionName, params) => {
    try {
      const result = await aiContractEngine.executeContract(contractName, functionName, params);
      console.log(result);
    } catch (error) {
      console.error(error);
    }
  };

  const handleCreateTransaction = async (sender, recipient, amount) => {
    try {
      const transaction = await aiContractEngine.createTransaction(sender, recipient, amount);
      setTransactions([...transactions, transaction]);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact>
          <Dashboard
            account={account}
            contracts={contracts}
            transactions={transactions}
            ellipticCurve={ellipticCurve}
            aiContractEngine={aiContractEngine}
            onDeployContract={handleDeployContract}
            onExecuteContract={handleExecuteContract}
            onCreateTransaction={handleCreateTransaction}
          />
        </Route>
        <Route path="/contracts/:contractName" exact>
          <ContractDetails
            contractName={match.params.contractName}
            aiContractEngine={aiContractEngine}
          />
        </Route>
        <Route path="/transactions/:transactionId" exact>
          <TransactionDetails
            transactionId={match.params.transactionId}
            aiContractEngine={aiContractEngine}
          />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
