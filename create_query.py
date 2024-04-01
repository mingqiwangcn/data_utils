import os
import csv
import uuid
import json

def main():
    out_file = '../data/nyc_open_100K/query/test/fusion_query.jsonl'
    if os.path.isfile(out_file):
        print(f'{out_file} already exists.')
        return
    f_o = open(out_file, 'w')
    with open('../data/nyc_open_100K/query/test/example_questions.csv') as f:
        reader = csv.reader(f, delimiter=',')
        q_count = 0
        for row, item in enumerate(reader):
            if row == 0:
                continue
            question = item[2].strip()
            if question == '':
                 continue
            q_count += 1
            table_id = item[1].strip()
            out_item = {
                'id':str(q_count),
                'question':question,
                'table_id_lst':[table_id],
                'answers':['n/a'],
                'ctxs':[{"title": "", "text": "This is a example passage."}]
            }
            f_o.write(json.dumps(out_item) + '\n')
    f_o.close()

if __name__ == '__main__':
    main()

