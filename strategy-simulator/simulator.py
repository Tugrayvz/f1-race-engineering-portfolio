import pandas as pd


def simulate_strategy(
    total_laps,
    base_lap_time,
    tyre_degradation,
    pit_lap,
    pit_loss,
    stint_1_tyre,
    stint_2_tyre,
):
    lap_times = []

    for lap in range(1, total_laps + 1):
        if lap < pit_lap:
            tyre_age = lap
            tyre = stint_1_tyre
        else:
            tyre_age = lap - pit_lap + 1
            tyre = stint_2_tyre

        lap_time = base_lap_time + (tyre_age * tyre_degradation)

        if lap == pit_lap:
            lap_time += pit_loss

        lap_times.append(
            {
                "Lap": lap,
                "Tyre": tyre,
                "Tyre Age": tyre_age,
                "Lap Time": lap_time,
            }
        )

    return pd.DataFrame(lap_times)


def total_race_time(strategy_df):
    return strategy_df["Lap Time"].sum()


total_laps = 53
base_lap_time = 86.5
pit_loss = 22.0

strategy_a = simulate_strategy(
    total_laps=total_laps,
    base_lap_time=base_lap_time,
    tyre_degradation=0.055,
    pit_lap=24,
    pit_loss=pit_loss,
    stint_1_tyre="Medium",
    stint_2_tyre="Hard",
)

strategy_b = simulate_strategy(
    total_laps=total_laps,
    base_lap_time=base_lap_time,
    tyre_degradation=0.065,
    pit_lap=18,
    pit_loss=pit_loss,
    stint_1_tyre="Medium",
    stint_2_tyre="Hard",
)

time_a = total_race_time(strategy_a)
time_b = total_race_time(strategy_b)

print("Race Strategy Simulator")
print("-----------------------")
print(f"Strategy A total time: {time_a:.2f} seconds")
print(f"Strategy B total time: {time_b:.2f} seconds")

if time_a < time_b:
    print(f"Recommended strategy: Strategy A")
    print(f"Estimated gain: {time_b - time_a:.2f} seconds")
else:
    print(f"Recommended strategy: Strategy B")
    print(f"Estimated gain: {time_a - time_b:.2f} seconds")