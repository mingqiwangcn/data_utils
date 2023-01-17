import mysql.connector
from tqdm import tqdm
import json

chunk_id = 0

def main():
    cnx = mysql.connector.connect(user='cc', password='cc', database='wiki')
    cursor = cnx.cursor()
    query = 'select old_text from text'
    cursor.execute(query)
    buffer_text = [] 
    chunk_size = 200000
    for record in tqdm(cursor):
        wiki_text = str(record[0], 'utf8')
        buffer_text.append(wiki_text)
        if len(buffer_text) >= chunk_size:
            write_buffer(buffer_text)
            buffer_text = []

    if len(buffer_text) > 0:
        write_buffer(buffer_text)

def write_buffer(buffer_text):
    global chunk_id
    chunk_id += 1
    out_file = 'wiki_text/part_%d.jsonl' % chunk_id
    with open(out_file, 'w') as f_o:
        for text in buffer_text:
            out_item = {
                'text':text
            }
            f_o.write(json.dumps(out_item) + '\n')

if __name__ == '__main__':
    main()

