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
| Ramanuj Kartik | 240041030 | SegWit Transaction Implementation |
| Sana Tejasri | 240041033 | Legacy Transaction Implementation |
| Vaghasiya Parl | 240041037 | Bitcoin RPC Setup and Environment |
# Objectives

1.  Understand how Bitcoin transactions work.
2.  Implement **Legacy P2PKH transactions**.
3.  Implement **SegWit P2SH-P2WPKH transactions**.
4.  Decode and analyze transaction scripts.
5.  Validate scripts using the **btcdeb debugger**.
6.  Compare transaction sizes between **Legacy and SegWit formats**.

------------------------------------------------------------------------

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

Start Bitcoin node:

    bitcoind -regtest -daemon

Create wallet:

    bitcoin-cli -regtest createwallet "labwallet"

Generate spendable coins:

    bitcoin-cli -regtest generatetoaddress 101 $(bitcoin-cli -regtest getnewaddress)

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
