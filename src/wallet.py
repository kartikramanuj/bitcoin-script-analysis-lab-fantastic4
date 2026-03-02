from config import rpc_connection
from bitcoinrpc.authproxy import JSONRPCException

def mine_blocks(num_blocks=101):
    # Mine blocks in regtest to get balance
    mining_address = rpc_connection.getnewaddress()
    rpc_connection.generatetoaddress(num_blocks, mining_address)

    balance = rpc_connection.getbalance()
    print("Blocks mined:", num_blocks)
    print("Current balance:", balance, "BTC")


def generate_addresses(address_type="legacy"):
    # Generate three addresses A, B, C with the default type of legacy if nothing mentioned
    address_A = rpc_connection.getnewaddress("", address_type)
    address_B = rpc_connection.getnewaddress("", address_type)
    address_C = rpc_connection.getnewaddress("", address_type)

    print("Address A:", address_A)
    print("Address B:", address_B)
    print("Address C:", address_C)

    return address_A, address_B, address_C


def fund_address(address, amount=10):
    # Send some coins to given address
    txid = rpc_connection.sendtoaddress(address, amount)
    print("Sent", amount, "BTC to", address)
    print("Transaction ID:", txid)

    # Mine one block to confirm transaction
    rpc_connection.generatetoaddress(1, rpc_connection.getnewaddress())

    return txid
