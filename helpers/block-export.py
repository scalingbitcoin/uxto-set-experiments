# Copyright (c) 2024 Scaling Bitcoin Developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

# Usage:
# - First: run bitcoind with rpcuser and rpcpassword
#   ./bitcoind -rpcpassword=bitcoin -rpcuser=bitcoin
# - Second: run this script
#   python3 src/block-export.py 0 10000

from bitcoincli import Bitcoin
import json
import sys

def export_block_info(bitcoin, tip, initial_from, max):
    for frm in range(initial_from, tip + 1, max):
        filename = f'block-info-{frm}-{frm + max - 1}.csv'
        print(f'Starting file: {filename}')
        with open(filename, 'w') as f:
            for i in range(frm, frm + max):
                # height = tip - n + i
                hash = bitcoin.getblockhash(i)
                # print(f'{height}: {hash}')
                block = bitcoin.getblock(hash, 1)

                # f.write(f'{block}\n')
                # print(f'{block}\n')

                height = block['height']
                print(f'Processing block at height {i} {height}...')

                size = block['size']
                time = block['time']
                mediantime = block['mediantime']
                nTx = block['nTx']
                # print(f'{height};{hash};{size};{time};{mediantime};{nTx}')
                # print(block)
                f.write(f'{height};{hash};{size};{time};{mediantime};{nTx}\n')

def export_raw_blocks(bitcoin, tip, initial_from, max):
    for frm in range(initial_from, tip + 1, max):
        filename = f'block-raw-{frm}-{frm + max - 1}.csv'
        print(f'Starting file: {filename}')
        with open(filename, 'w') as f:
            for i in range(frm, frm + max):
                hash = bitcoin.getblockhash(i)
                block = bitcoin.getblock(hash, 0)
                print(f'Processing block at height {i} ...')
                f.write(f'{block}\n')


host = "127.0.0.1"
port = "8332"
username = "bitcoin"
password = "bitcoin"

bitcoin = Bitcoin(username, password, host, port)

# info = bitcoin.getblockchaininfo()
info_raw = bitcoin.getchaintips()
# print(info_raw[0]['height'])
tip = info_raw[0]['height']

print(f'Blockchain tip: {tip}')

if len(sys.argv) < 3:
    print('Usage: block-export.py <initial_from> <max>')
    print('Example: block-export.py 0 10000')
    sys.exit(1)

initial_from = int(sys.argv[1])
max = int(sys.argv[2])

# export_block_info(bitcoin, tip, initial_from, max)
export_raw_blocks(bitcoin, tip, initial_from, max)

# info = bitcoin.getblockchaininfo()
info_raw = bitcoin.getchaintips()
# print(info_raw[0]['height'])
tip = info_raw[0]['height']

print(f'Blockchain tip: {tip}')

