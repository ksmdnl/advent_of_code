colours = {
  "red": 12,
  "green": 13,
  "blue": 14,
}

def decide(game):
  possible = True
  for seq in game:
    seq = seq.split(" ")
    possible = possible & (int(seq[0]) <= colours[seq[1]])
    if not possible:
      #print(int(seq[0]) <= colours[seq[1]], possible, seq[0], colours[seq[1]])
      return False

  return possible

def main():
  with open('2.txt', 'r') as file:
    lines = [line.strip() for line in file]
  possible = True
  sum_ids = 0
  for line in lines:
    games = line.split(": ")[-1].split("; ")
    for idx, game in enumerate(games):
       game = game.split(", ")
       possible = decide(game)
       if not possible:
         break
    if possible:
      game_id = line.split(": ")[0]
      sum_ids += int(game_id.split(" ")[1])
  print(sum_ids)

if __name__ == "__main__":
  main()
