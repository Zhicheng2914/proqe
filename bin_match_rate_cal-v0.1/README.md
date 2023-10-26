# Bin Match Rate Calculate 模塊

## 功能邏輯

已知DATA工作簿I列中存放的是料件L值，为对应每片料的实测值，且数据正态分布
已知DATA工作簿J列中存放的是料件a值，为对应每片料的实测值，且数据正态分布
已知DATA工作簿A列中存放的是对应料件名称，有以下两种内容
[Bucket,Kickstand]
已知DATA工作簿E列中存放的是对应料件Bin信息，有以下内容
L1-a1,L1-a2,L1-a3,L1-a4,L2-a1,L2-a2,L2-a3,L2-a4,L3-a1,L3-a2,L3-a3,L3-a4,L4-a1,L4-a2,L4-a3,L4-a4,L5-a1,L5-a2,L5-a3,L5-a4

Bucket与Kickstand符合以下条件时可以视为可以匹配。
1. Bucket的a值与Kickstand的a值差值不超过+/-0.15
2. Bucket的L值比Kickstand的L值差值必须在-2~0之间
3. Bucket与Kickstand的L Bin 或者a Bin必须相邻，比如L2-a2可以匹配L2-a1或者L2-a3或者L1-a1或者L3-a1
4. 为每个Bucket只匹配一个Kickstand
5. Kickstand随机选择，但一旦Kickstand被选择了下次它就不能再参与匹配了
6. 匹配数量指的是能够匹配在一起的料件数量，比如说一个Bucket和一个Kickstand共同组成了一个成品，那么匹配数量就是1

data.csv的B列名称为"SN"，里面记录了Bucket和Kickstand的序列号，在匹配的同时，将能匹配的Bucket和Kickstand的SN成对记录下来并输出到matched_sn.csv文件中。

## ChatGPT溝通記錄

[對話記錄](https://chat.openai.com/share/41570701-2767-424f-9c44-1e7802dbbb5e)