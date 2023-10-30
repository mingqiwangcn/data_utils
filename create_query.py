import csv
import uuid
import json

def main():
    q_data = []
    with open('../solo_work/data/chicago_open/query/test/test_questions.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row, item in enumerate(reader):
            q_data.append(item)

    with open('../solo_work/data/chicago_open/query/test/fusion_query.jsonl', 'w') as f_o:
        for row, q_item in enumerate(q_data):
            out_item = {
                'id':str(row + 1),
                'question':q_item[0],
                'table_id_lst':[q_item[1]],
                'answers':['n/a'],
                'ctxs':[{"title": "", "text": "This is a example passage."}]
            }
            f_o.write(json.dumps(out_item) + '\n')

if __name__ == '__main__':
    main()

