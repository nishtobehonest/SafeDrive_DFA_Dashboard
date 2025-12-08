# SafeDrive Ithaca – ADAS Decision Dashboard

## Overview

SafeDrive is an interactive decision-support dashboard designed to help the **City of Ithaca** and insurance providers evaluate and prioritize **Advanced Driver Assistance System (ADAS)** features. This tool enables data-driven decision-making by balancing multiple priorities: vehicle safety, implementation cost, and environmental impact.

Using **Multi-Criteria Decision Analysis (MCDA)**, the dashboard allows stakeholders to explore how different priority weights influence which ADAS features should be adopted first.

---

## What is ADAS?

Advanced Driver Assistance Systems are technologies that help drivers avoid accidents and improve vehicle safety. Examples include:
- **Forward Collision Warning / Automatic Emergency Braking (AEB)** – Detects obstacles and applies brakes
- **Blind-Spot Monitoring** – Alerts drivers to vehicles in blind spots
- **Lane-Keeping Assist** – Helps maintain lane position
- **Driver Monitoring System** – Detects driver fatigue or distraction
- **Adaptive Cruise Control** – Maintains safe following distance

---

## Why This Dashboard?

Cities and insurers must decide which ADAS features to prioritize for deployment. This is a **multi-criteria problem**:

- **Safety** → Which features save the most lives?
- **Cost** → What's the implementation & maintenance budget?
- **Environment** → What's the carbon footprint?

SafeDrive solves this by letting decision-makers adjust the importance of each criterion and see how rankings change in real-time.

---

## Features

### 🎛️ **Interactive Weight Settings**
Adjust the relative importance of each criterion using sliders:
- **Safety Weight** → How much to prioritize accident prevention
- **Cost Weight** → How much to prioritize affordability
- **Environment Weight** → How much to prioritize sustainability

Weights automatically normalize to sum to 1.0.

### 📊 **Real-Time Ranking**
Displays features ranked by **MCDA Score** – a composite metric combining all three criteria under your chosen weights.

### 📈 **Visual Analysis**
Bar chart showing the top-ranked features, making it easy to see which options lead the competition.

### 📋 **Detailed Scores**
View normalized scores (0–1) for safety, cost, and environmental impact alongside the final MCDA ranking.

---

## How It Works

### MCDA Formula

The dashboard calculates each feature's score as:

```
MCDA_Score = (w_safety × safety_score) 
           + (w_cost × (1 - cost_score))
           + (w_environment × (1 - environmental_score))
```

Where:
- **Safety Score** → Higher is better (direct)
- **Cost Score** → Lower is better (inverted: 1 - cost)
- **Environmental Score** → Lower impact is better (inverted: 1 - environmental)
- **w_*** → Normalized weights (sum to 1.0)

### Example Scenario

**Scenario:** City prioritizes safety above all else
- Safety Weight: 0.7
- Cost Weight: 0.2
- Environment Weight: 0.1

→ Features with high safety scores rank first, even if costly.

**Different Scenario:** Budget-constrained city
- Safety Weight: 0.4
- Cost Weight: 0.5
- Environment Weight: 0.1

→ Affordable features rise in the ranking despite lower safety gains.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/SafeDrive_DFA_Dashboard.git
   cd SafeDrive_DFA_Dashboard
   ```

2. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```
   
   Or manually:
   ```bash
   pip3 install streamlit pandas matplotlib
   ```

3. **Run the dashboard:**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open in browser:**
   The app will open at `http://localhost:8501`

---

## Data Source

The dashboard uses `ADAS_Ithaca_Stage1_output.csv`, which contains:
- **Feature Name** → Name of the ADAS technology
- **Safety Score** → Normalized score (0–1) based on accident prevention effectiveness
- **Cost Score** → Normalized score (0–1) based on implementation & maintenance cost
- **Environmental Score** → Normalized score (0–1) based on carbon footprint & emissions

All scores are pre-normalized (0–1 scale) for consistency and comparison.

---

## Usage Guide

### Step 1: Adjust Weights
Use the sidebar sliders to set priorities:
- Move sliders left (lower) or right (higher)
- Watch the **Normalized Weights** update in real-time

### Step 2: View Rankings
- Left panel: See all features ranked by MCDA score (highest = best)
- View their individual safety, cost, and environmental scores

### Step 3: Explore Top Features
- Right panel: Adjust the slider to show top 3–10 features
- Bar chart visualizes the top contenders

### Step 4: Make Decisions
Use the rankings to inform procurement, policy, or deployment decisions.

---

## Project Context

This project is part of a **Decision and Financial Analysis (DFA)** course assignment. It demonstrates:
- Multi-criteria decision analysis (MCDA) techniques
- Interactive data visualization with Streamlit
- Stakeholder decision support systems
- Goal programming and optimization concepts

---

## Team

Developed for the **City of Ithaca** and classroom stakeholders as a proof-of-concept decision tool.

---

## Technologies Used

- **Streamlit** – Interactive web dashboard framework
- **Pandas** – Data manipulation and analysis
- **Matplotlib** – Data visualization
- **Python 3** – Core programming language

---

## Future Enhancements

Potential improvements:
- Add sensitivity analysis (how robust is the ranking to weight changes?)
- Include additional criteria (e.g., public acceptance, political feasibility)
- Support for custom datasets
- Export reports as PDF
- Scenario comparison (save/load weight presets)
- Integration with real-world ADAS deployment data

---

## License

This project is for educational purposes. See LICENSE file for details.

---

## Questions or Feedback?

For questions about the dashboard, data sources, or MCDA methodology, contact the development team or submit an issue on GitHub.

---

**Last Updated:** December 2025
