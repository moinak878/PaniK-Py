from block import Block
import datetime
blockchain = [Block.create_genesis_block()]
print("The genesis block has been created !")
print("Hash : %s" % blockchain[-1].hash)

num_blocks_to_add = 5

for i in range(1,num_blocks_to_add+1):
    blockchain.append(Block(blockchain[-1].hash,i,datetime.datetime.now()))
    print("block #%d has been created with Hash : %s " %(i,blockchain[-1].hash))