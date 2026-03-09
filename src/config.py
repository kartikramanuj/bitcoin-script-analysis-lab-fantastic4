# RPC configuration (make sure these match bitcoin.conf)
rpc_user = "your_username"
rpc_password = "your_password"
rpc_url = "http://%s:%s@127.0.0.1:18443" % (rpc_user, rpc_password)

rpc_connection = AuthServiceProxy(rpc_url)


def check_connection():
    # Check if bitcoind is running and RPC is working
    try:
        info = rpc_connection.getblockchaininfo()
        print("Connected successfully")
        print("Current chain:", info["chain"])
    except Exception as e:
        print("Connection failed")
        print(e)
