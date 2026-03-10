# CS216 --- Bitcoin Transaction Analysis Lab

## Overview

This project demonstrates how **Bitcoin transactions are created,
signed, validated, and analyzed** using both **Legacy (P2PKH)** and
**SegWit (P2SH-P2WPKH)** transaction formats.

The experiment focuses on understanding the **Bitcoin scripting
system**, transaction structure, and comparing the **transaction size
and efficiency between Legacy and SegWit formats**.

The project uses **Bitcoin Core in regtest mode**, which provides a
private local blockchain environment for safe experimentation and
testing.

------------------------------------------------------------------------

## Team

| Name | Roll No | Responsibility |
|-----|-----|-----|
| Sakshya Singh Kasera | 240021015 | Analysis and Documentation |
| Ramanuj Kartik | 240041030 | Creat Transaction and  Implementation of main file |
| Sana Tejasri | 240041033 | Decoding , extracting and comparing Transaction Implementation |
| Vaghasiya Parl | 240041037 | Bitcoin RPC Setup and Environment |
# Objectives

1.  Understand how Bitcoin transactions work.
2.  Implement **Legacy P2PKH transactions**.
3.  Implement **SegWit P2SH-P2WPKH transactions**.
4.  Decode and analyze transaction scripts.
5.  Validate scripts using the **btcdeb debugger**.
6.  Compare transaction sizes between **Legacy and SegWit formats**.

------------------------------------------------------------------------
## ⚙️ Tools & Dependencies  
- **Bitcoin Core (bitcoind)** – Full Bitcoin node  
- **Bitcoin CLI (`bitcoin-cli`)** – Command-line interface  
- **Python (`python-bitcoinlib`, `bitcoinrpc`)** – Bitcoin scripting  
- **Bitcoin Debugger (`btcdeb`)** – Script validation  
- **C (`libbitcoin`, `curl` for RPC calls)** – Alternative implementation  

---

# Project Structure

    bitcoin-script-analysis-lab/

    ├── src/
    │   ├── config.py        # Configuration for RPC connection and environment
    │   ├── main.py          # Entry point of the program (runs the experiment)
    │   ├── transactions.py  # Functions for creating and decoding transactions
    │   └── wallet.py        # Wallet creation and address generation utilities
    │
    ├── Report.pdf           # Final lab report with screenshots and results
    └── README.md            # Project overview and setup instructions

------------------------------------------------------------------------

# Prerequisites

## 1. Bitcoin Core

Download Bitcoin Core from: https://bitcoin.org/en/download

Verify installation:

    bitcoind --version
    bitcoin-cli --version

## 2. Python

Python **3.8 or higher** is required.

    python3 --version

## 3. Python Bitcoin RPC Library

Install the RPC library:

    pip install python-bitcoinrpc

## 4. btcdeb Script Debugger

    git clone https://github.com/bitcoin-core/btcdeb.git
    cd btcdeb
    make

------------------------------------------------------------------------

# Bitcoin Regtest Setup

Start Bitcoin node (linux):

    bitcoind -regtest -daemon

Start Bitcoin node (windows):

    bitcoind -regtest



## Configure bitcoin.conf for Regtest:
```python
    # Step 1: Locate the Bitcoin data directory
    # Windows: C:\Users\YourUsername\AppData\Roaming\Bitcoin\
    # Linux/macOS: ~/.bitcoin/

    # Step 2: If `bitcoin.conf` doesn’t exist, create it
    touch ~/.bitcoin/bitcoin.conf
```

   ```ini
# Step 3: Edit `bitcoin.conf` with the following settings
[regtest]
regtest=1
server=1
rpcuser=your_username
rpcpassword=your_password
rpcallowip=127.0.0.1
rpcport=18443
txindex=1
paytxfee=0.0001
fallbackfee=0.0002
mintxfee=0.00001
txconfirmtarget=6
```

⚠️ Note: Replace your_username and your_password with your own values.

##  Update Python Script with RPC Credentials
```python
# Update the Python script with RPC credentials from bitcoin.conf
rpc_user = 'your_username'
rpc_password = 'your_password'
rpc_port = 18443

# Example: Connect to Bitcoin RPC using requests
import requests

url = f"http://127.0.0.1:{rpc_port}"
headers = {"content-type": "application/json"}
auth = (rpc_user, rpc_password)

response = requests.get(url, auth=auth)
print(response.json())
```
## Useful Commands to Verify Bitcoin Node is Running
```
bash
# Check Bitcoin balance
bitcoin-cli -regtest getbalance

# Mine a block
bitcoin-cli -regtest generatetoaddress 1 <your_regtest_address>

# List transactions
bitcoin-cli -regtest listtransactions
```

------------------------------------------------------------------------

# Running the Project

Run:

    python src/main.py

The program automatically:

1.  Loads wallet
2.  Generates Legacy addresses
3.  Creates transactions
4.  Decodes scripts
5.  Performs SegWit transactions
6.  Compares transaction sizes

------------------------------------------------------------------------

# Bitcoin Script Structure

### Locking Script (scriptPubKey)

    OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG

### Unlocking Script (scriptSig)

    <signature> <public key>

------------------------------------------------------------------------

# SegWit Advantages

-   Lower transaction fees
-   Reduced transaction size
-   Fixes transaction malleability
-   Increases effective block capacity
-   Enables Lightning Network

------------------------------------------------------------------------

# Report

Full results are documented in:

    Report.pdf

------------------------------------------------------------------------

# References

Bitcoin Developer Documentation\
https://developer.bitcoin.org

Mastering Bitcoin --- Andreas Antonopoulos
