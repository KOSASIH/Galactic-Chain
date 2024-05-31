# Blockchain Project Architecture

This document describes the architecture of our advanced high-tech blockchain project.

## Overview
Our blockchain project consists of the following main components:

- **Core**: The core module contains the fundamental components of the blockchain, including the block and transaction structures, consensus algorithm, and cryptographic functions.
- **Contracts**: The contracts module contains the smart contract templates for various use cases, including ERC20 and ERC721 tokens.
- **Network**: The network module contains the components for peer-to-peer communication, RPC server, and node management.
- **Storage**: The storage module contains the database and levelDB components for storing the blockchain data.
- **Utils**: The utils module contains the math and string utility functions.
- **Infrastructure**: The infrastructure module contains the configuration files, genesis block, and network settings.
- **Tools**: The tools module contains the command-line tools for generating genesis blocks and managing network nodes.

## Components

### Core

#### Blockchain
- [block.go](../core/blockchain/block.go)
- [blockchain.go](../core/blockchain/blockchain.go)

#### Transaction
- [transaction.go](../core/transaction.go)

#### Consensus
- [pos.go](../consensus/pos.go)
- [poa.go](../consensus/poa.go)
- [hybrid.go](../consensus/hybrid.go)

#### Crypto
- [hash.go](../crypto/hash.go)
- [signature.go](../crypto/signature.go)
- [encryption.go](../crypto/encryption.go)

### Network

#### Node
- [node.go](../network/node.go)

#### Peer
- [peer.go](../network/peer.go)

#### RPC
- [rpc.go](../network/rpc.go)

### Storage

#### DB
- [db.go](../storage/db.go)

#### LevelDB
- [leveldb.go](../storage/leveldb.go)

### Utils

#### Math
- [math.go](../utils/math.go)

#### String
- [string.go](../utils/string.go)

### Infrastructure

#### Config
- [config.json](../infrastructure/config.json)

#### Genesis
- [genesis.json](../infrastructure/genesis.json)

#### Network
- [network.json](../infrastructure/network.json)

### Tools

#### Genesis Tool
- [genesis_tool.go](../tools/genesis_tool.go)

#### Network Tool
- [network_tool.go](../tools/network_tool.go)
