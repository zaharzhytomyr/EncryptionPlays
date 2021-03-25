sample_str = "Еврей, еще и обновленец-таких не любил; вопрос: как он ужился там в 23.04.1965?В 78м он уехал."

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

def encode_one_key_permutation(text : str, rows : int = 7, cols : int = 7,
                           key : str = '0145236') -> str:
  assert(len(key) == cols)
  key_map = {int(val) - 1: num for num, val in enumerate(key)}
  
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

def decode_one_key_permutation(text : str, rows : int = 7, cols : int = 7,
                           key : str = '0145236'):
  assert(len(key) == cols)
  key_map = {int(val) - 1: num for num, val in enumerate(key)}
  
  res = ""
  fragments = split_by_len(text, rows * cols)
  for fragment in fragments:
    first_table = create_empty_table(rows, cols)
    fill_table_by_rows(first_table, fragment, rows, cols)

    decoded_table = create_empty_table(rows, cols)
    for i in key_map.keys():
      col = get_col(first_table, key_map[i])
      set_col(decoded_table, i, col)
    res += read_table_by_cols(decoded_table, cols)
  return res

def encode_two_keys_permutation(text : str, rows : int = 7, cols : int = 7,
                                key_cols : str = '0145236',
                                key_rows : str = '0362154'):
  assert(len(key_rows) == rows)
  key_map = {int(val) - 1: num for num, val in enumerate(key_rows)}
  text = encode_one_key_permutation(text, rows, cols, key_cols)

  res = ""
  fragments = split_by_len(text, rows * cols)
  for fragment in fragments:
    first_table = create_empty_table(rows, cols)
    fill_table_by_rows(first_table, fragment, rows, cols)

    encoded_table = create_empty_table(rows, cols)
    for i in key_map.keys():
      row = first_table[key_map[i]]
      encoded_table[i] = row
    res += read_table_by_rows(encoded_table, rows)
  return res

def decode_two_keys_permutation(text : str, rows : int = 7, cols : int = 7,
                                key_cols : str = '0145236',
                                key_rows : str = '0362154'):
  assert(len(key_rows) == rows)
  key_map = {int(val) - 1: num for num, val in enumerate(key_rows)}

  res = ""
  fragments = split_by_len(text, rows * cols)
  for fragment in fragments:
    first_table = create_empty_table(rows, cols)
    fill_table_by_rows(first_table, fragment, rows, cols)

    decoded_table = create_empty_table(rows, cols)
    for i in key_map.keys():
      row = first_table[i]
      decoded_table[key_map[i]] = row
    print(decoded_table)
    temp = read_table_by_rows(decoded_table, cols)
    res += decode_one_key_permutation(temp, rows, cols, key_cols)
  return res
  
#main
opt : int = input("Select your encryption algo :\n1 - no key permutation\n2 - one key - permutation\n3 - double key permutation: ")
opt = int(opt)
if opt not in range(1, 4):
  exit("Choose correct option: 1, or 2, or 3!")
else:
  text : str = input("Please input your text to decrypt: ")
  text = text.replace(" ", "_")
  rows = input("Input amount of rows for encryption table: ")
  rows = int(rows)
  cols = input("Input amount of columns for encryption table: ")
  cols = int(cols)
  encoded = ''
  decoded = ''
  if opt == 2:
    key : str = input("Input key to decrypt: ")
    encoded = encode_one_key_permutation(text, rows, cols, key)
    decoded = decode_one_key_permutation(text, rows, cols, key)
  elif opt == 3:
    key_cols : str = input("Input 1st key to decrypt: ")
    key_rows : str = input("Input 2nd key to decrypt: ")
    encoded = encode_two_keys_permutation(text, rows, cols, key_cols, key_rows)
    decoded = decode_two_keys_permutation(text, rows, cols, key_cols, key_rows)
  elif opt == 1:
    encoded = encode_no_key_permutation(text, rows, cols)
    decoded = decode_no_key_permutation(text, rows, cols)
  print(encoded)












