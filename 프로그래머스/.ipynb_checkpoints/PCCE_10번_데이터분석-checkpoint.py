def solution(data, ext, val_ext, sort_by):
    by = ['code','date','maximum','remain']
    
    answer = []
    for item in data:
        if item[by.index(ext)] < val_ext:
            answer.append(item)
    
    return sorted(answer, key=lambda x: x[by.index(sort_by)])