import pandas as pd
import matplotlib.pyplot as plt

TYRE_MODELS = {
    "Soft": 0.090,
    "Medium": 0.055,
    "Hard": 0.035,
}


def simulate_strategy(
    total_laps,
    base_lap_time,
    pit_lap,
    pit_loss,
    stint_1_tyre,
    stint_2_tyre,
):
    lap_times = []

    for lap in range(1, total_laps + 1):

        if lap < pit_lap:
            tyre = stint_1_tyre
            tyre_age = lap
        else:
            tyre = stint_2_tyre
            tyre_age = lap - pit_lap + 1

        degradation = TYRE_MODELS[tyre]

        lap_time = (
            base_lap_time
            + tyre_age * degradation
        )

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


# =====================
# STRATEGY A
# Medium -> Hard
# =====================

strategy_a = simulate_strategy(
    total_laps=53,
    base_lap_time=86.5,
    pit_lap=24,
    pit_loss=22.0,
    stint_1_tyre="Medium",
    stint_2_tyre="Hard",
)

# =====================
# STRATEGY B
# Medium -> Hard
# Earlier Stop
# =====================

strategy_b = simulate_strategy(
    total_laps=53,
    base_lap_time=86.5,
    pit_lap=18,
    pit_loss=22.0,
    stint_1_tyre="Medium",
    stint_2_tyre="Hard",
)

# =====================
# STRATEGY C
# Soft -> Hard
# =====================

strategy_c = simulate_strategy(
    total_laps=53,
    base_lap_time=86.5,
    pit_lap=14,
    pit_loss=22.0,
    stint_1_tyre="Soft",
    stint_2_tyre="Hard",
)

time_a = total_race_time(strategy_a)
time_b = total_race_time(strategy_b)
time_c = total_race_time(strategy_c)

print("\nRace Strategy Simulator")
print("----------------------------")

print(f"Strategy A (Medium -> Hard): {time_a:.2f} s")
print(f"Strategy B (Medium -> Hard Early Stop): {time_b:.2f} s")
print(f"Strategy C (Soft -> Hard): {time_c:.2f} s")

strategies = {
    "Strategy A": time_a,
    "Strategy B": time_b,
    "Strategy C": time_c,
}

best_strategy = min(strategies, key=strategies.get)

print("\nRecommended Strategy")
print("----------------------------")
print(best_strategy)
print(f"Estimated race time: {strategies[best_strategy]:.2f} s")

# =====================
# VISUALIZATION
# =====================

plt.figure(figsize=(12, 6))

plt.plot(
    strategy_a["Lap"],
    strategy_a["Lap Time"],
    label="Strategy A (M-H)",
)

plt.plot(
    strategy_b["Lap"],
    strategy_b["Lap Time"],
    label="Strategy B (M-H Early)",
)

plt.plot(
    strategy_c["Lap"],
    strategy_c["Lap Time"],
    label="Strategy C (S-H)",
)

plt.title("F1 Race Strategy Comparison")
plt.xlabel("Lap")
plt.ylabel("Lap Time (s)")
plt.legend()
plt.grid(True)

plt.show()