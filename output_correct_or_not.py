import json
import numpy as np

def main():
    corret_lst = []
    data_file = '../solo_work/solo/output/chicago_open/test_76dd1458-334f-4cff-a826-dd36e64fa0e4/pred_epoch_0_None.jsonl'
    out_file = './correct.json'
    f_o = open(out_file, 'w')
    with open(data_file) as f:
        for line in f:
            item = json.loads(line)
            q_id = item['qid']
            table_id_lst = item['table_id_lst']
            tag_lst = item['tags']
            top_1_table = tag_lst[0]['table_id']
            correct = int(top_1_table in table_id_lst)
            corret_lst.append(correct)
            
            out_item = {
                'qid':q_id,
                'question':item['question'],
                'correct':correct
            }
            f_o.write(json.dumps(out_item) + '\n') 

    f_o.close()
    co_ratio = np.mean(corret_lst)
    print('%.2f' % (co_ratio * 100))

if __name__ == '__main__':
    main()
