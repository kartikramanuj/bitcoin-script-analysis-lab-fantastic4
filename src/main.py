if __name__ == "__main__":
    print("Starting setup process")

    check_connection()
    create_wallet()
    mine_blocks()

    print("Generating legacy addresses")
    addr_A, addr_B, addr_C = generate_addresses("legacy")

    print("Funding address A")
    fund_address(addr_A)

    print("Setup completed")
