with open('128_nodes_211.txt', 'w') as f:
    f.write('148 20 256\n')
    
    switches = list(range(128, 148))
    f.write(' '.join(map(str, switches)) + '\n')
    
    # HB switches (128-143)
    for i in range(16):
        hb_switch_id = 128 + i
        for j in range(8):
            npu_id = i * 8 + j
            f.write(f'{npu_id} {hb_switch_id} 1600Gbps 50ns 0\n')
            
    # Eth switches (144-147)
    for i in range(4):
        eth_switch_id = 144 + i
        for j in range(32):
            npu_id = i * 32 + j
            f.write(f'{npu_id} {eth_switch_id} 200Gbps 10us 0\n')
