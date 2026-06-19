import os

import fastf1
import fastf1.utils
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(page_title="F1 Telemetry Dashboard", layout="wide")

st.title("F1 Telemetry Analysis Dashboard")
st.write(
    "Compare Formula 1 driver telemetry: speed, throttle, brake, RPM, delta time and speed-colored track map."
)

CACHE_DIR = "telemetry-dashboard/data/cache"
os.makedirs(CACHE_DIR, exist_ok=True)
fastf1.Cache.enable_cache(CACHE_DIR)


year = st.sidebar.selectbox("Season", [2024, 2023, 2022])
grand_prix = st.sidebar.text_input("Grand Prix", "Monza")
session_type = st.sidebar.selectbox("Session", ["Q", "R", "FP1", "FP2", "FP3"])

driver_1 = st.sidebar.text_input("Driver 1 Code", "VER")
driver_2 = st.sidebar.text_input("Driver 2 Code", "LEC")


def plot_telemetry(tel1, tel2, driver_1, driver_2, column, title, y_title):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=tel1["Distance"],
            y=tel1[column],
            mode="lines",
            name=driver_1,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=tel2["Distance"],
            y=tel2[column],
            mode="lines",
            name=driver_2,
        )
    )

    fig.update_layout(
        title=title,
        xaxis_title="Distance (m)",
        yaxis_title=y_title,
        height=450,
    )

    st.plotly_chart(fig, use_container_width=True)


if st.sidebar.button("Analyze"):
    with st.spinner("Loading F1 session data..."):
        session = fastf1.get_session(year, grand_prix, session_type)
        session.load()

        lap1 = session.laps.pick_driver(driver_1).pick_fastest()
        lap2 = session.laps.pick_driver(driver_2).pick_fastest()

        tel1 = lap1.get_car_data().add_distance()
        tel2 = lap2.get_car_data().add_distance()

        delta_time, ref_tel, compare_tel = fastf1.utils.delta_time(lap1, lap2)

    st.subheader(f"{driver_1} vs {driver_2}")

    lap_time_1 = lap1["LapTime"]
    lap_time_2 = lap2["LapTime"]
    lap_delta = lap_time_1 - lap_time_2

    col1, col2, col3 = st.columns(3)

    col1.metric(f"{driver_1} Fastest Lap", str(lap_time_1))
    col2.metric(f"{driver_2} Fastest Lap", str(lap_time_2))
    col3.metric("Lap Delta", str(lap_delta))

    plot_telemetry(
        tel1, tel2, driver_1, driver_2,
        "Speed", "Speed vs Distance", "Speed (km/h)"
    )

    plot_telemetry(
        tel1, tel2, driver_1, driver_2,
        "Throttle", "Throttle vs Distance", "Throttle (%)"
    )

    plot_telemetry(
        tel1, tel2, driver_1, driver_2,
        "Brake", "Brake vs Distance", "Brake"
    )

    plot_telemetry(
        tel1, tel2, driver_1, driver_2,
        "RPM", "RPM vs Distance", "RPM"
    )

    st.subheader("Delta Time Analysis")

    fig_delta = go.Figure()

    fig_delta.add_trace(
        go.Scatter(
            x=ref_tel["Distance"],
            y=delta_time,
            mode="lines",
            name=f"{driver_1} vs {driver_2}",
        )
    )

    fig_delta.update_layout(
        title=f"Delta Time: {driver_1} vs {driver_2}",
        xaxis_title="Distance (m)",
        yaxis_title="Delta Time (s)",
        height=450,
    )

    st.plotly_chart(fig_delta, use_container_width=True)

    final_delta = delta_time.iloc[-1]

    if final_delta < 0:
        st.success(f"{driver_1} gained time over {driver_2} across the lap.")
    else:
        st.success(f"{driver_2} gained time over {driver_1} across the lap.")

    st.subheader("Speed Colored Track Map")

    pos = lap1.get_pos_data()
    car_data = lap1.get_car_data()

    min_len = min(len(pos), len(car_data))

    x = pos["X"].iloc[:min_len]
    y = pos["Y"].iloc[:min_len]
    speed = car_data["Speed"].iloc[:min_len]

    fig_track = go.Figure()

    fig_track.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="markers",
            marker=dict(
                size=6,
                color=speed,
                colorscale="Turbo",
                colorbar=dict(title="Speed km/h"),
            ),
            showlegend=False,
        )
    )

    fig_track.update_layout(
        title=f"{grand_prix} Speed Map - {driver_1}",
        xaxis_title="X Position",
        yaxis_title="Y Position",
        height=700,
        yaxis=dict(scaleanchor="x", scaleratio=1),
    )

    st.plotly_chart(fig_track, use_container_width=True)

    st.subheader("Race Engineer Notes")

    avg_speed_1 = tel1["Speed"].mean()
    avg_speed_2 = tel2["Speed"].mean()

    max_speed_1 = tel1["Speed"].max()
    max_speed_2 = tel2["Speed"].max()

    st.write(f"{driver_1} average speed: {avg_speed_1:.2f} km/h")
    st.write(f"{driver_2} average speed: {avg_speed_2:.2f} km/h")

    st.write(f"{driver_1} top speed: {max_speed_1:.2f} km/h")
    st.write(f"{driver_2} top speed: {max_speed_2:.2f} km/h")

    if avg_speed_1 > avg_speed_2:
        st.info(f"{driver_1} carried higher average speed over the lap.")
    else:
        st.info(f"{driver_2} carried higher average speed over the lap.")

    if max_speed_1 > max_speed_2:
        st.info(f"{driver_1} reached a higher top speed.")
    else:
        st.info(f"{driver_2} reached a higher top speed.")