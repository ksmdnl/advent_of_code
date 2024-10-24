valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

def scan(seq, idx):
  start = False
  end = False
  str_num = ""
  
  while(True):
    try:
      cur_char = seq[idx]
      if cur_char.isdigit():
        start = True
        str_num += cur_char
      elif not cur_char.isdigit() and start is True:
        break
      idx += 1
    except IndexError as e:
      print(e)
      breakpoint()
  return idx, len(str_num), str_num

def scan_neighborhood(seq, cur_idx):
  left = cur_idx - 1
  right = cur_idx + 1
  top = cur_idx - 10
  bottom = cur_idx + 10
  diag_top_left = top - 1
  diag_top_right = top + 1
  diag_bottom_left = bottom - 1
  diag_bottom_right = bottom + 1
  return (left, right, top, bottom, diag_top_left, diag_top_right, diag_bottom_left, diag_bottom_right)

def is_any_neighbor_symbol(seq, indices):
  max_len = len(seq)
  is_symbol = True
  for idx in indices:
    if idx < 0 or idx >= max_len or (seq[idx] in valid):
      continue
    else:
      is_symbol = False
  return is_symbol

def main():
  sum_num = 0
  with open('3.txt', 'r') as file:
    seq_list = file.readlines()
  seq = "".join([str(item) for item in seq_list])
  max_len = len(seq)
  idx_last_cur_idx = 0
  sum_num = 0
  it_is = False
  while(idx_last_cur_idx <= max_len):
    idx_last_cur_idx, str_len, str_num = scan(seq, idx_last_cur_idx)
    print(f"sum: {sum_num}, str_num: {str_num}, near symbol: {it_is}")
    idx_start_cur_idx = idx_last_cur_idx - str_len
    for i in range(str_len - 1):
      indices = scan_neighborhood(seq, idx_start_cur_idx)
      it_is = is_any_neighbor_symbol(seq, indices)
      idx_start_cur_idx += 1
    if not it_is:
      sum_num += int(str_num)


if __name__ == "__main__":
  main()
    
