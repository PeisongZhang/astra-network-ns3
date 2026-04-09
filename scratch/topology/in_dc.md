# 16个NPU位于同一DC内的网络拓扑配置

## Node配置
- 每个Node包含4个NPU，每个NPU的LBW带宽为200Gbps, 时延为500ns
- 每个Node内部的NPU通过LBW Switch互联，组成全互联拓扑
- 每个Node内部的4个NPU之间通过4800Gbps的HBW Switch互联，模拟DGX A100 4GPU的Server Node, 时延为150ns
- 为了让Node内部的NPU之间通过的数据走HBW Switch而不是LBW Switch，每个NPU直连一个NIC Switch，时延1ns，NIC Switch再连接到LBW Switch, 时延500ns，

## DC配置
- DC内部有4个Node，Node之间通过Spine Switch互联，组成全互联拓扑
- LBW Switch到Spine Switch的链路带宽为800Gbps, 时延为600ns
