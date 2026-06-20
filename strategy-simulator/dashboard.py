import pandas as pd
import plotly.graph_objects as go
import streamlit as st


TYRE_MODELS = {
    "Soft": 0.090,
    "Medium": 0.055,
    "Hard": 0.035,
}


st.set_page_config(page_title="F1 Strategy Simulator", layout="wide")

st.title("F1 Race Strategy Simulator")
st.write(
    "Compare Formula 1 race strategies using tyre degradation, pit stop timing and total race time simulation."
)


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

        lap_time = base_lap_time + tyre_age * degradation

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


st.sidebar.header("Race Settings")

total_laps = st.sidebar.slider("Total Laps", 10, 80, 53)
base_lap_time = st.sidebar.number_input("Base Lap Time (seconds)", 60.0, 120.0, 86.5)
pit_loss = st.sidebar.number_input("Pit Stop Loss (seconds)", 10.0, 40.0, 22.0)

st.sidebar.header("Strategy A")
a_stint_1 = st.sidebar.selectbox("Strategy A Stint 1 Tyre", ["Soft", "Medium", "Hard"], index=1)
a_stint_2 = st.sidebar.selectbox("Strategy A Stint 2 Tyre", ["Soft", "Medium", "Hard"], index=2)
a_pit_lap = st.sidebar.slider("Strategy A Pit Lap", 2, total_laps - 1, 24)

st.sidebar.header("Strategy B")
b_stint_1 = st.sidebar.selectbox("Strategy B Stint 1 Tyre", ["Soft", "Medium", "Hard"], index=1)
b_stint_2 = st.sidebar.selectbox("Strategy B Stint 2 Tyre", ["Soft", "Medium", "Hard"], index=2)
b_pit_lap = st.sidebar.slider("Strategy B Pit Lap", 2, total_laps - 1, 18)

st.sidebar.header("Strategy C")
c_stint_1 = st.sidebar.selectbox("Strategy C Stint 1 Tyre", ["Soft", "Medium", "Hard"], index=0)
c_stint_2 = st.sidebar.selectbox("Strategy C Stint 2 Tyre", ["Soft", "Medium", "Hard"], index=2)
c_pit_lap = st.sidebar.slider("Strategy C Pit Lap", 2, total_laps - 1, 14)

strategy_a = simulate_strategy(total_laps, base_lap_time, a_pit_lap, pit_loss, a_stint_1, a_stint_2)
strategy_b = simulate_strategy(total_laps, base_lap_time, b_pit_lap, pit_loss, b_stint_1, b_stint_2)
strategy_c = simulate_strategy(total_laps, base_lap_time, c_pit_lap, pit_loss, c_stint_1, c_stint_2)

time_a = total_race_time(strategy_a)
time_b = total_race_time(strategy_b)
time_c = total_race_time(strategy_c)

strategies = {
    "Strategy A": time_a,
    "Strategy B": time_b,
    "Strategy C": time_c,
}

best_strategy = min(strategies, key=strategies.get)

st.subheader("Strategy Result Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Strategy A", f"{time_a:.2f}s")
col2.metric("Strategy B", f"{time_b:.2f}s")
col3.metric("Strategy C", f"{time_c:.2f}s")
col4.metric("Recommended", best_strategy)

st.subheader("Lap Time Comparison")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=strategy_a["Lap"],
        y=strategy_a["Lap Time"],
        mode="lines",
        name=f"Strategy A ({a_stint_1}-{a_stint_2})",
    )
)

fig.add_trace(
    go.Scatter(
        x=strategy_b["Lap"],
        y=strategy_b["Lap Time"],
        mode="lines",
        name=f"Strategy B ({b_stint_1}-{b_stint_2})",
    )
)

fig.add_trace(
    go.Scatter(
        x=strategy_c["Lap"],
        y=strategy_c["Lap Time"],
        mode="lines",
        name=f"Strategy C ({c_stint_1}-{c_stint_2})",
    )
)

fig.update_layout(
    title="Tyre Degradation and Pit Stop Strategy Comparison",
    xaxis_title="Lap",
    yaxis_title="Lap Time (seconds)",
    height=600,
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Strategy Details")

summary_df = pd.DataFrame(
    {
        "Strategy": ["Strategy A", "Strategy B", "Strategy C"],
        "Stint 1 Tyre": [a_stint_1, b_stint_1, c_stint_1],
        "Stint 2 Tyre": [a_stint_2, b_stint_2, c_stint_2],
        "Pit Lap": [a_pit_lap, b_pit_lap, c_pit_lap],
        "Total Race Time": [f"{time_a:.2f}s", f"{time_b:.2f}s", f"{time_c:.2f}s"],
    }
)

st.dataframe(summary_df, use_container_width=True)

st.info(
    f"{best_strategy} is the recommended strategy based on the lowest simulated total race time."
)