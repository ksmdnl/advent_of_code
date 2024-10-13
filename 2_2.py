from functools import reduce

def update(game, min_set):
  possible = True
  for seq in game:
    seq = seq.split(" ")
    if min_set[seq[1]] <= int(seq[0]):
      min_set[seq[1]] = int(seq[0])
  return min_set

def main():
  with open('2.txt', 'r') as file:
    lines = [line.strip() for line in file]
  red_min, green_min, blue_min = 0, 0, 0
  sum = 0

  for line in lines:
    min_set = {
      "red": 0,
      "green": 0,
      "blue": 0,
    }
    games = line.split(": ")[-1].split("; ")
    for game in games:
      game = game.split(", ")
      min_set = update(game, min_set)
    sum += reduce((lambda x, y: x* y), min_set.values())
  print(sum)
    

if __name__ == "__main__":
  main()
