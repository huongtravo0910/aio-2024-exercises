def calc_f1_score(tp, fp, fn):
    if not isinstance(tp, int):
        print("tp must be int")
        return

    if not isinstance(fp, int):
        print("tp must be int")
        return

    if not isinstance(fn, int):
        print("tp must be int")
        return

    if tp<=0 or fp<=0 or fn<=0:
        print("tp, fp and fn must be greater than 0")
        return 
    
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*(precision*recall)/(precision+recall)

    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1_score is {f1_score}')



calc_f1_score(2,3,4)
calc_f1_score(tp="a", fp=3, fn=4)
calc_f1_score(tp=2, fp="a", fn=4)
calc_f1_score(tp=2, fp=3, fn="a")
calc_f1_score(tp=2, fp=3, fn=0)
calc_f1_score(tp=2.1, fp=3, fn=0)