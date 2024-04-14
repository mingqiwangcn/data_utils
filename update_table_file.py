import json
from tqdm import tqdm

def main():
    input_file = './tables.jsonl'
    with open(input_file) as f:
        for line in tqdm(f):
            table_data = json.loads(line)
            table_id = table_data['tableId'] 
            out_file = './' + table_id + '.jsonl'   
            with open(out_file, 'w') as f_o:
                f_o.write(json.dumps(table_data))

if __name__ == '__main__':
    main()

