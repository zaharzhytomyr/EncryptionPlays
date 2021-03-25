#replace spaces by "_"

def array_to_str(arr) -> str:
  res = ""
  for i in arr:
    res += str(i)
  return res

def get_col(table, idx : int):
  return [row[idx] for row in table]

def set_col(table, idx : int, col):
  k = 0
  for row in table:
    try:
      row[idx] = col[k]
      k += 1
    except IndexError:
      raise SystemExit

def split_by_len(seq : str, length : int):
  return [seq[i:i + length] for i in range(0, len(seq), length)]

def create_empty_table(rows : int = 7, cols : int = 7):
  return [["_"] * cols for i in range(rows)]

def fill_table_by_cols(table, text : str, rows : int = 7, cols : int = 7): 
  k : int = 0
  for j in range(cols):
    for i in range(rows):
      try:
        table[i][j] = text[k]
        k += 1
      except IndexError:
        break
  return table

def read_table_by_rows(table, rows : int = 7) -> str:
  res = ""
  for i in range(rows):
    res += array_to_str(table[i])
  return res

def fill_table_by_rows(table, text : str, rows : int = 7, cols : int = 7): 
  k : int = 0
  for i in range(rows):
    for j in range(cols):
      try:
        table[i][j] = text[k]
        k+=1
      except IndexError:
        break
  return table

def read_table_by_cols(table, cols : int = 7) -> str:
  res = ""
  for j in range(cols):
    res += array_to_str(get_col(table, j))
  return res

def encode_no_key_permutation(text : str, rows : int = 7, cols : int = 7):
  res = ""
  fragments = split_by_len(text, rows * cols)
  for fragment in fragments:
    table = create_empty_table(rows, cols)
    fill_table_by_rows(table, fragment, rows, cols)
    res += read_table_by_cols(table, cols)
  return res

def decode_no_key_permutation(text : str, rows : int = 7, cols : int = 7):
  res = ""
  fragments = split_by_len(text, rows * cols)
  for fragment in fragments:
    table = create_empty_table(rows, cols)
    fill_table_by_cols(table, fragment, rows, cols)
    res += read_table_by_rows(table, cols)
  return res

def encode_col_key_permutation(text : str, rows : int = 7, cols : int = 7,
                           key : str = '0145236') -> str:
  assert(len(key) == cols)
  key_map = {int(val): num for num, val in enumerate(key)}
  
  res = ""
  fragments = split_by_len(text, rows * cols)
  for fragment in fragments:
    first_table = create_empty_table(rows, cols)
    fill_table_by_cols(first_table, fragment, rows, cols)

    encoded_table = create_empty_table(rows, cols)
    for i in key_map.keys():
      col = get_col(first_table, key_map[i])
      set_col(encoded_table, i, col)
    res += read_table_by_rows(encoded_table, cols)
  return res

def decode_col_key_permutation(text : str, rows : int = 7, cols : int = 7,
                           key : str = '0145236'):
  assert(len(key) == cols)
  key_map = {int(val): num for num, val in enumerate(key)}
  
  res = ""
  fragments = split_by_len(text, rows * cols)
  for fragment in fragments:
    first_table = create_empty_table(rows, cols)
    fill_table_by_rows(first_table, fragment, rows, cols)
    print(first_table)

    decoded_table = create_empty_table(rows, cols)
    for i in key_map.keys():
      col = get_col(first_table, key_map[i])
      set_col(decoded_table, i, col)
    res += read_table_by_cols(decoded_table, cols)
    print(decoded_table)
  return res

def encode_row_key_permutation(text : str, rows : int = 7, cols : int = 7,
                                  key_cols : str = '0145236',
                                  key_rows : str = '0362154'):
  return NotImplemented

def decode_row_key_permutation():
  return NotImplemented





