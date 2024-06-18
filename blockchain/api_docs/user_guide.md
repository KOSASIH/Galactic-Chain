# Blockchain-based Application User Guide

This user guide provides instructions on how to use the blockchain-based application.

## Wallet

The wallet module allows users to create, import, and export wallets, as well as get the wallet address and balance.

### Create a new wallet

To create a new wallet, run the following command:

```
1. $ cli wallet create --password my_password
```


Replace `my_password` with a secure password for the wallet.

### Import an existing wallet

To import an existing wallet, run the following command:

```
1. $ cli wallet import my_private_key
```


Replace `my_private_key` with the private key for the wallet.

### Export the wallet

To export the wallet, run the following command:

```
1. $ cli wallet export --password my_password
```


Replace `my_password` with the password for the wallet.

### Get the wallet address

To get the wallet address, run the following command:

```
1. $ cli wallet get_address
```


### Get the wallet balance

To get the wallet balance, run the following command:

```
1. $ cli wallet get_balance
```


## Send tokens

To send tokens to a recipient address, run the following command:

```
1. $ cli send my_recipient_address 10
```


Replace `my_recipient_address` with the recipient address and `10` with the amount to send.

## Blockchain Explorer

The blockchain explorer module allows users to get block, transaction, and address information.

### Get a block by height

To get a block by height, run the following command:

```
1. $ cli explorer get_block 100
```


Replace `100` with the block height.

### Get a transaction by hash

To get a transaction by hash, run the following command:

```
1. $ cli explorer get_transaction my_transaction_hash
```


Replace `my_transaction_hash` with the transaction hash.

### Get address information

To get address information, run the following command:

```
1. $ cli explorer get_address_info my_address
```


Replace `my_address` with the address.

