import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="SafeDrive Ithaca – ADAS Decision Dashboard",
    layout="wide"
)

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Rename columns to lowercase with underscores for easier access
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    # Normalize scores between 0 and 1
    cols = ['safety_score', 'cost_score', 'environmental_score']
    df_norm = df.copy()
    df_norm[cols] = (df_norm[cols] - df_norm[cols].min()) / (df_norm[cols].max() - df_norm[cols].min())
    return df_norm

def compute_mcda(df: pd.DataFrame, w_s: float, w_c: float, w_e: float) -> pd.DataFrame:
    df = df.copy()
    df["mcda_score"] = (
        w_s * df["safety_score"]
        + w_c * (1 - df["cost_score"])
        + w_e * (1 - df["environmental_score"])
    )
    return df.sort_values("mcda_score", ascending=False)

# Load data
import os
csv_path = os.path.join(os.path.dirname(__file__), "ADAS_Ithaca_Stage1_output.csv")
df_norm = load_data(csv_path)

# Sidebar – weights
st.sidebar.header("Weight settings")
st.sidebar.write("Set relative importance for each criterion")

w_s = st.sidebar.slider("Safety weight", 0.0, 1.0, 0.5, 0.05)
w_c = st.sidebar.slider("Cost weight (lower cost is better)", 0.0, 1.0, 0.3, 0.05)
w_e = st.sidebar.slider("Environment weight (lower impact is better)", 0.0, 1.0, 0.2, 0.05)

# Normalize weights so they sum to 1
weight_sum = w_s + w_c + w_e
if weight_sum == 0:
    w_s, w_c, w_e = 1.0, 0.0, 0.0
    weight_sum = 1.0

w_s /= weight_sum
w_c /= weight_sum
w_e /= weight_sum

st.sidebar.markdown("**Normalized weights**")
st.sidebar.write(f"Safety: {w_s:.2f}, Cost: {w_c:.2f}, Environment: {w_e:.2f}")

# Compute MCDA
df_ranked = compute_mcda(df_norm, w_s, w_c, w_e)

# Layout columns
col1, col2 = st.columns([2, 2])

with col1:
    st.subheader("Ranked ADAS features for Ithaca")
    st.dataframe(
        df_ranked[["feature_name", "safety_score", "cost_score", "environmental_score", "mcda_score"]]
        .reset_index(drop=True)
        .style.format({"safety_score": "{:.2f}", "cost_score": "{:.2f}", "environmental_score": "{:.2f}", "mcda_score": "{:.3f}"})
    )

with col2:
    st.subheader("MCDA scores – top features")
    top_k = st.slider("Number of top features to plot", 3, len(df_ranked), 7, 1)
    plot_df = df_ranked.head(top_k)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(plot_df["feature_name"], plot_df["mcda_score"])
    ax.invert_yaxis()
    ax.set_xlabel("MCDA score")
    ax.set_title("Top ADAS features under current weights")
    st.pyplot(fig)

st.markdown("---")
st.subheader("Summary")
best_feature = df_ranked.iloc[0]["feature_name"]
st.write(
    f"Under the current weights, the highest ranked feature is **{best_feature}**. "
    f"This dashboard lets City of Ithaca staff and insurers explore how priorities over safety, cost and environmental impact "
    f"change which ADAS features rise to the top."
)