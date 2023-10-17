def player(prev_play, opponent_history=[]):
  # This dictionary tracks the opponent's move patterns
  move_patterns = {
      "RR": {"R": 0, "P": 0, "S": 0},
      "RP": {"R": 0, "P": 0, "S": 0},
      "RS": {"R": 0, "P": 0, "S": 0},
      "PR": {"R": 0, "P": 0, "S": 0},
      "PP": {"R": 0, "P": 0, "S": 0},
      "PS": {"R": 0, "P": 0, "S": 0},
      "SR": {"R": 0, "P": 0, "S": 0},
      "SP": {"R": 0, "P": 0, "S": 0},
      "SS": {"R": 0, "P": 0, "S": 0}
  }

  opponent_history.append(prev_play)

  if len(opponent_history) > 2:
      # Update the move patterns based on the last two moves
      prev_two_moves = opponent_history[-3] + opponent_history[-2]
      if prev_two_moves in move_patterns:
          move_patterns[prev_two_moves][prev_play] += 1

  # If there's enough history, use it to make an educated guess
  if len(opponent_history) > 1:
      recent_pattern = opponent_history[-2] + opponent_history[-1]
      if recent_pattern in move_patterns:
          likely_move = max(move_patterns[recent_pattern], key=move_patterns[recent_pattern].get)
          # Return the move that would beat the opponent's most likely move
          if likely_move == "R":
              return "P"
          elif likely_move == "P":
              return "S"
          else:
              return "R"

  # Default to Rock if there's not enough data
  return "R"


def quincy(prev_play, _=None):
  if prev_play == "R":
      return "P"
  elif prev_play == "P":
      return "S"
  else:
      return "R"

def play(player1, player2, num_games, verbose=False):
  p1_prev_play = ""
  p2_prev_play = ""
  results = {"p1": 0, "p2": 0, "tie": 0}

  for _ in range(num_games):
      p1_play = player1(p2_prev_play)
      p2_play = player2(p1_prev_play)

      if p1_play == p2_play:
          results["tie"] += 1
          winner = "Tie."
      elif (p1_play == "P" and p2_play == "R") or (
              p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                     and p2_play == "P"):
          results["p1"] += 1
          winner = "Player 1 wins."
      elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
          results["p2"] += 1
          winner = "Player 2 wins."

      if verbose:
          print("Player 1:", p1_play, "| Player 2:", p2_play)
          print(winner)
          print()

      p1_prev_play = p1_play
      p2_prev_play = p2_play

  games_won = results['p2'] + results['p1']

  if games_won == 0:
      win_rate = 0
  else:
      win_rate = results['p1'] / games_won * 100

  print("Final results:", results)
  print(f"Player 1 win rate: {win_rate}%")

  return (win_rate)

# Now, let's play the game
play(player, quincy, 1000, verbose=True)
