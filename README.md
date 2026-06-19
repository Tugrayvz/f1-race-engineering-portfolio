# 🏎️ F1 Race Engineering Portfolio

Professional Formula 1 telemetry analysis, race strategy simulation and motorsport data science projects built with Python.

---

## Overview

This repository contains Formula 1 data analytics projects designed to replicate real-world race engineering and strategy workflows.

The objective is to analyze telemetry data, compare driver performance, evaluate race strategy and build engineering-focused decision support tools using real Formula 1 data and simulation models.

---

# F1 Telemetry Analysis Dashboard

Interactive dashboard for comparing Formula 1 drivers using telemetry data.

## Features

- Fastest Lap Comparison
- Speed Analysis
- Throttle Analysis
- Brake Analysis
- RPM Analysis
- Delta Time Analysis
- Sector Performance Analysis
- Track Map Visualization
- Speed Colored Track Map
- Racing Line Comparison
- Engineering Report Generator
- AI Race Engineer Summary
- Average Speed Comparison
- Top Speed Comparison
- Race Engineer Notes
- Race Strategy Simulator
- Tyre Degradation Model
- Strategy Comparison Visualization

---

## Technology Stack

- Python
- FastF1
- Streamlit
- Plotly
- Pandas
- NumPy
- Matplotlib

---

## Dashboard Screenshots

### Main Dashboard

![Dashboard Overview](images/dashboard-overview.png)

---

### Speed Comparison

![Speed Comparison](images/speed-comparison.png)

---

### Throttle Comparison

![Throttle Comparison](images/throttle-comparison.png)

---

### Brake Comparison

![Brake Comparison](images/brake-comparison.png)

---

### Delta Time Analysis

![Delta Time Analysis](images/delta-time-analysis.png)

---

### Sector Performance Analysis

![Sector Analysis](images/sector-analysis.png)

---

### Track Map Visualization

![Track Map](images/track-map.png)

---

### Speed Colored Track Map

![Speed Colored Track Map](images/speed-track-map.png)

---

### Racing Line Comparison

![Racing Line Comparison](images/racing-line-comparison.png)

---

### Engineering Report Generator

![Engineering Report](images/engineering-report.png)

---

### AI Race Engineer Summary

![AI Race Engineer Summary](images/ai-race-engineer-summary.png)

---

### Strategy Comparison

![Strategy Comparison](images/strategy-comparison.png)

---

### Race Engineer Notes

![Race Engineer Notes](images/race-engineer-notes.png)

---

## Example Analysis

### Session Details

| Parameter | Value |
|------------|--------|
| Season | 2024 |
| Grand Prix | Monza |
| Session | Qualifying |
| Driver 1 | Max Verstappen |
| Driver 2 | Charles Leclerc |

### Analysis Output

The telemetry dashboard compares driver performance and highlights differences in:

- Braking zones
- Corner entry speed
- Corner exit performance
- Acceleration phases
- Top speed sections
- Engine behaviour
- Racing line differences
- Sector performance
- Overall lap efficiency
- Time gained and lost throughout the lap

---

# Race Strategy Simulator

A race strategy simulation module for comparing tyre compounds, pit stop timing and total race time.

## Strategy Simulator Features

- Multi-strategy comparison
- Soft, Medium and Hard tyre degradation models
- Pit stop loss modelling
- Total race time estimation
- Automatic recommended strategy selection
- Tyre degradation visualization

---

## Current Development Progress

### Phase 1 — Telemetry Dashboard

- [x] Driver comparison
- [x] Speed analysis
- [x] Brake analysis
- [x] Throttle analysis
- [x] RPM analysis
- [x] Lap delta visualization
- [x] Sector performance analysis
- [x] Track map visualization
- [x] Speed-colored track map
- [x] Racing line comparison
- [x] Engineering report generator
- [x] AI race engineer summary
- [x] Average speed comparison
- [x] Top speed comparison
- [x] Race engineer notes

### Phase 2 — Advanced Telemetry

- [ ] Corner-by-corner analysis
- [ ] Interactive telemetry overlays
- [x] Racing line comparison
- [x] AI race engineer summary
- [x] Driver comparison report generation

### Phase 3 — Race Strategy Simulator

- [x] Tire degradation modelling
- [x] Strategy comparison visualization
- [x] Multi-strategy comparison
- [ ] Pit stop optimization
- [ ] Safety car simulations
- [ ] Undercut / Overcut analysis
- [ ] Strategy recommendation engine

### Phase 4 — Machine Learning

- [ ] Lap time prediction
- [ ] Driver performance index
- [ ] Pace forecasting
- [ ] Race outcome prediction

---

## Repository Structure

```text
f1-race-engineering-portfolio/
│
├── README.md
├── requirements.txt
│
├── images/
│   ├── dashboard-overview.png
│   ├── speed-comparison.png
│   ├── throttle-comparison.png
│   ├── brake-comparison.png
│   ├── delta-time-analysis.png
│   ├── sector-analysis.png
│   ├── track-map.png
│   ├── speed-track-map.png
│   ├── racing-line-comparison.png
│   ├── engineering-report.png
│   ├── ai-race-engineer-summary.png
│   ├── strategy-comparison.png
│   └── race-engineer-notes.png
│
├── telemetry-dashboard/
│   ├── dashboard.py
│   ├── data/
│   │   └── cache/
│   ├── notebooks/
│   └── src/
│
└── strategy-simulator/
    ├── simulator.py
    └── README.md
```

---

## Future Goal

Build a complete Formula 1 Race Engineering Toolkit capable of supporting telemetry analysis, strategy modelling, performance evaluation and race decision workflows similar to those used in professional motorsport environments.

---

## Author

### Yener Tugra YAVUZ

Motorsport Data Analytics • Artificial Intelligence • Software Engineering

Building a Formula 1 Race Engineering Portfolio through data analytics, simulation and machine learning.