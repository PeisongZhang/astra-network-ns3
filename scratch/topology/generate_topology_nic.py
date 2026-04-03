with open('128_nodes_211.txt', 'w') as f:
    # Nodes: 128 NPU + 128 NIC Switch + 16 HB Switch + 4 Leaf Eth Switch + 1 Spine Eth Switch = 277
    # Switches: 128 NIC + 16 HB + 4 Leaf Eth + 1 Spine Eth = 149
    # Links: 128 (NPU-HB) + 128 (NPU-NIC) + 128 (NIC-LeafEth) + 4 (LeafEth-Spine) = 388
    f.write('277 149 388\n')
    
    switches = list(range(128, 277))
    f.write(' '.join(map(str, switches)) + '\n')
    
    # NIC switches (128-255)
    for npu_id in range(128):
        nic_switch_id = 128 + npu_id
        # NPU connects to NIC Switch
        f.write(f'{npu_id} {nic_switch_id} 200Gbps 1ns 0\n')

    # HB switches (256-271)
    for i in range(16):
        hb_switch_id = 256 + i
        for j in range(8):
            npu_id = i * 8 + j
            f.write(f'{npu_id} {hb_switch_id} 1600Gbps 50ns 0\n')
            
    # Leaf Eth switches (272-275)
    for i in range(4):
        eth_switch_id = 272 + i
        for j in range(32):
            npu_id = i * 32 + j
            nic_switch_id = 128 + npu_id
            # NIC Switch connects to Leaf Eth Switch
            f.write(f'{nic_switch_id} {eth_switch_id} 200Gbps 10us 0\n')

    # Spine Eth switch (276)
    spine_switch_id = 276
    for i in range(4):
        eth_switch_id = 272 + i
        # Leaf Eth Switch connects to Spine Eth Switch
        # Non-blocking bandwidth: 32 * 200Gbps = 6400Gbps
        f.write(f'{eth_switch_id} {spine_switch_id} 6400Gbps 10us 0\n')
