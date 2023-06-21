# 정렬 유무 확인
def is_sorted(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

# 역정렬 유무 확인
def is_reverse_sorted(seq):
    return all(seq[i] >= seq[i+1] for i in range(len(seq)-1))