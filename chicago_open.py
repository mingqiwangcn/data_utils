import json
import os
from tqdm import tqdm
import glob

def get_data_file_lst():
    file_pattern = '../table_discovery_project/data/chicago_open/tables_csv/*.csv'
    file_lst = glob.glob(file_pattern) 
    return file_lst

def get_meta_data():
    meta_file = '../table_discovery_project/data/chicago_open/meta.json'
    with open(meta_file) as f:
        meta_data = json.load(f)
   
    meta_dict = {}
    for item in meta_data:
        res_type = item['resource']['type']
        assert(res_type) == 'dataset'
        table_id = item['resource']['id']

        meta_dict[table_id] = item
    
    return meta_dict

def main():
    meta_dict = get_meta_data()
    data_file_lst = get_data_file_lst()
    for data_file in tqdm(data_file_lst):
        base_name = os.path.basename(data_file)
        table_id = os.path.splitext(base_name)[0]
        meta_item = meta_dict[table_id]
        title = meta_item['resource']['name']
        col_names = meta_item['resource']['columns_name']
        data_dir = os.path.dirname(data_file)
        csv_meta_file = os.path.join(data_dir, '%s.meta.json' % table_id)
        with open(csv_meta_file, 'w') as f_o:
            csv_meta = {
                'table_id':table_id,
                'title':title,
                'col_names':col_names
            }
            f_o.write(json.dumps(csv_meta, indent=3))
             
if __name__ == '__main__':
    main() 

