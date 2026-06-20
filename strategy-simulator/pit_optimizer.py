from simulator import simulate_strategy, total_race_time

best_time = float("inf")
best_pit_lap = None

for pit_lap in range(5, 40):

    strategy = simulate_strategy(
        total_laps=53,
        base_lap_time=86.5,
        pit_lap=pit_lap,
        pit_loss=22.0,
        stint_1_tyre="Medium",
        stint_2_tyre="Hard",
    )

    race_time = total_race_time(strategy)

    if race_time < best_time:
        best_time = race_time
        best_pit_lap = pit_lap

print("Pit Stop Optimizer")
print("------------------")
print(f"Best pit lap: {best_pit_lap}")
print(f"Estimated race time: {best_time:.2f} seconds")