import os
from tqdm import tqdm
import json
import wikitextparser as wtp
from multiprocessing import Pool as ProcessPool
import csv
import glob

def process_tables(text_file):
    base_name = os.path.basename(text_file)
    part_name = os.path.splitext(base_name)[0]
    table_id = 0
    with open(text_file) as f:
        for line in f:
            wiki_text = json.loads(line)['text']
            wiki_info = wtp.parse(wiki_text)
            for table in wiki_info.tables:
                table_id += 1
                caption = table.caption
                table_data = table.data()
                if caption is not None: 
                    out_cap_file = './wiki_tables/%s_%d.cap' % (part_name, table_id)
                    with open(out_cap_file, 'w') as f_o_cap:
                        f_o_cap.write(caption)

                out_data_file = './wiki_tables/%s_%d.csv' %(part_name, table_id)
                with open(out_data_file, 'w') as f_o:
                    writer = csv.writer(f_o)
                    writer.writerows(table_data) 

def main():
    part_file_lst = glob.glob('./wiki_text/part_*.jsonl')
    num_workers = min(os.cpu_count(), len(part_file_lst))
    work_pool = ProcessPool(num_workers)
    for _ in tqdm(work_pool.imap_unordered(process_tables, part_file_lst), total=len(part_file_lst)):
         a = 1

if __name__ == '__main__':
    main()

