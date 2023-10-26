import pandas as pd

def can_match(bucket, kickstand):
    # 条件1: a值差值不超过+/-0.15
    a_match = abs(bucket['A1'] - kickstand['A1']) <= 0.15
    
    # 条件2: L值差值必须在-2~-1之间
    l_match = -2 <= (bucket['L1'] - kickstand['L1']) <= -1
    
    # 如果L和a中的任何一个不匹配，则直接返回False
    if not (a_match and l_match):
        return False

    # 条件3: L Bin 或者a Bin必须相邻
    bucket_L_bin, bucket_a_bin = int(bucket['BININFO'].split('-')[0][1:]), int(bucket['BININFO'].split('-')[1][1:])
    kickstand_L_bin, kickstand_a_bin = int(kickstand['BININFO'].split('-')[0][1:]), int(kickstand['BININFO'].split('-')[1][1:])
    
    bin_match = (bucket_L_bin == kickstand_L_bin and abs(bucket_a_bin - kickstand_a_bin) == 1) or (abs(bucket_L_bin - kickstand_L_bin) == 1 and bucket_a_bin == kickstand_a_bin)
    
    return bin_match

def compute_matching_probability_and_count(bin_info):
    data = pd.read_csv('data.csv')
    
    buckets = data[data['PARTNAME'] == 'Bucket']
    kickstands = data[data['PARTNAME'] == 'Kickstand']
    
    target_bucket = buckets[buckets['BININFO'] == bin_info]
    
    match_count = 0
    for _, bucket_row in target_bucket.iterrows():
        for _, kickstand_row in kickstands.iterrows():
            if can_match(bucket_row, kickstand_row):
                match_count += 1
                break  # 找到匹配后，跳出内部循环

    total_buckets = len(buckets)  # 使用所有Bucket的数量作为总数
    
    if total_buckets == 0:
        print("没有Bucket数据。")
        return 0, 0
    
    probability = match_count / total_buckets
    return probability, match_count

# 使用
bin_info = "L3-a2"
probability, count = compute_matching_probability_and_count(bin_info)
print(f"{bin_info} Bucket与Kickstand的匹配概率为: {probability:.2%}")
print(f"匹配的数量为: {count}")