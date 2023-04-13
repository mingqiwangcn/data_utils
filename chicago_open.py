import json
import os
import csv
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
        field_show_dict = build_col_name_index(item)
        meta_dict[table_id] = {
            'title':item['resource']['name'],
            'field_dict':field_show_dict,
        }
    return meta_dict

def build_col_name_index(item):
    col_field_names = item['resource']['columns_field_name']
    col_show_names = item['resource']['columns_name']
    assert len(col_field_names) == len(col_show_names)
    field_show_dict = {}
    for idx, field in enumerate(col_field_names):
        field_show_dict[field] = col_show_names[idx]
    return field_show_dict

def get_header(data_file):
    with open(data_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row, item in enumerate(reader):
            field_name_lst = item
            return field_name_lst
    return None      

def main():
    meta_dict = get_meta_data()
    data_file_lst = get_data_file_lst()
    for data_file in tqdm(data_file_lst):
        base_name = os.path.basename(data_file)
        table_id = os.path.splitext(base_name)[0]
        meta_item = meta_dict[table_id]
        title = meta_item['title']
        field_name_lst = get_header(data_file)
        field_show_dict = meta_item['field_dict']
        col_name_lst = [field_show_dict[a].lower() for a in field_name_lst]
        data_dir = os.path.dirname(data_file)
        csv_meta_file = os.path.join(data_dir, '%s.meta.json' % table_id)
        with open(csv_meta_file, 'w') as f_o:
            csv_meta = {
                'table_id':table_id,
                'title':title,
                'col_names':col_name_lst
            }
            f_o.write(json.dumps(csv_meta, indent=3))
             
if __name__ == '__main__':
    main() 

