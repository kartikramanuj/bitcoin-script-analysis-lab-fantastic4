if __name__ == "__main__":
    from wallet import *
    from transactions import *
      
    print("🔹 Setting up Bitcoin Environment...")
    create_wallet()
    mine_blocks()

    print("\n🔹 Generating Legacy (P2PKH) Addresses...")
    addr_A, addr_B, addr_C = generate_addresses("legacy")

    print("\n🔹 Funding Address A...")
    fund_txid = fund_address(addr_A)

    print("\n🔹 Creating Transaction (A → B)...")
    txid_AB = create_transaction(addr_A, addr_B, 2)

    print("\n🔹 Decoding Legacy Transaction (A → B)...")
    decode_transaction(txid_AB)

    print("\n🔹 Extracting Challenge Script (A → B)...")
    extract_challenge_script(txid_AB)

    print("\n🔹 Creating Transaction (B → C)...")
    txid_BC = create_transaction(addr_B, addr_C, 1)

    print("\n🔹 Decoding Legacy Transaction (B → C)...")
    decode_transaction(txid_BC)

    print("\n🔹 Extracting Response Script (B → C)...")
    extract_response_script(txid_BC)

    print("\n🔹 Generating SegWit (P2SH-P2WPKH) Addresses...")
    addr_A_segwit, addr_B_segwit, addr_C_segwit = generate_addresses("p2sh-segwit")

    print("\n🔹 Funding SegWit Address A'...")
    fund_txid_segwit = fund_address(addr_A_segwit)

    print("\n🔹 Creating Transaction (A' → B')...")
    txid_AB_segwit = create_transaction(addr_A_segwit, addr_B_segwit, 2)

    print("\n🔹 Decoding SegWit Transaction (A' → B')...")
    decode_transaction(txid_AB_segwit)

    print("\n🔹 Extracting Challenge Script (A' → B')...")
    extract_challenge_script(txid_AB_segwit)

    print("\n🔹 Creating Transaction (B' → C')...")
    txid_BC_segwit = create_transaction(addr_B_segwit, addr_C_segwit, 1)

    print("\n🔹 Decoding SegWit Transaction (B' → C')...")
    decode_transaction(txid_BC_segwit)

    print("\n🔹 Extracting Response Script (B' → C')...")
    extract_response_script(txid_BC_segwit)

    print("\n🔹 Comparing Transaction Sizes...")
    
    print("\n (A → B) and (A' → B')-")
    compare_transaction_sizes(txid_AB, txid_AB_segwit)

    print("\n (B → C) and (B' → C')-")
    compare_transaction_sizes(txid_BC, txid_BC_segwit)

    print("\n Bitcoin Scripting Assignment Completed!")
