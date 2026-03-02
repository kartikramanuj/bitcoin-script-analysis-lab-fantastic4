from config import rpc_connection

def create_transaction(from_addr, to_addr, amount):
    fee=0.0001
    """Creates, signs, and broadcasts a transaction with basic coin selection."""
    # 1. Fetch all available UTXOs
    utxos = rpc_connection.listunspent(1, 9999999, [from_addr])
    
    inputs = []
    total_in = 0.0
    
    # 2. Simple Coin Selection: Keep adding UTXOs until we cover the amount + fee
    for utxo in utxos:
        inputs.append({"txid": utxo["txid"], "vout": utxo["vout"]})
        total_in += float(utxo["amount"])
        if total_in >= (amount + fee):
            break
            
    if total_in < (amount + fee):
        print(f" Insufficient funds. Have: {total_in}, Need: {amount + fee}")
        return None

    # 3. Handle Change
    change = round(total_in - amount - fee, 8)
    outputs = {to_addr: amount}
    if change > 0.00001:  # Only send change if it's above the dust limit
        outputs[from_addr] = change

    # 4. Create, Sign, and Send
    try:
        raw_tx = rpc_connection.createrawtransaction(inputs, outputs)
        signed_tx = rpc_connection.signrawtransactionwithwallet(raw_tx)
        
        if not signed_tx.get("complete"):
            print(" Signing failed")
            return None
            
        txid = rpc_connection.sendrawtransaction(signed_tx["hex"])
        print(f" Transaction {from_addr} → {to_addr} Sent! TXID: {txid}")
        rpc_connection.generatetoaddress(1, rpc_connection.getnewaddress())
        return txid
    except Exception as e:
        print(f" RPC Error: {e}")
        return None