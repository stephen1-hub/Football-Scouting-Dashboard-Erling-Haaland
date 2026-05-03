import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(layout="wide")

# -----------------------------
# IMAGE
# -----------------------------
image_path = "haaland.jpg"

def load_image(path):
    try:
        if os.path.exists(path):
            return Image.open(path)
        return None
    except:
        return None

image = load_image(image_path)

# -----------------------------
# HEADER
# -----------------------------
col1, col2 = st.columns([1, 3])

with col1:
    if image:
        st.image(image, width=180)
    else:
        st.warning("Image not found")

with col2:
    st.title("Erling Haaland")
    st.markdown("### Forward | Elite Box Striker")
    st.markdown("---")

# -----------------------------
# KPIs
# -----------------------------
total_goals = 24
total_xg = 25.88
total_xa = 4.86

col1, col2, col3, col4 = st.columns(4)

col1.metric("Goals", total_goals, round(total_goals - total_xg, 2))
col2.metric("xG", total_xg)
col3.metric("xA", total_xa)
col4.metric("xG/90", "0.86", "Elite")

st.markdown("---")

# -----------------------------
# ATTRIBUTES (SCOUT GRADE)
# -----------------------------
st.markdown("### Player Attributes")

attributes = {
    "Finishing": 92,
    "Positioning": 94,
    "Physical": 95,
    "Aerial Ability": 78,
    "Creativity": 72,
    "Link-up Play": 80
}

for attr, value in attributes.items():
    st.markdown(f"**{attr}**")
    st.progress(value / 100)

st.markdown("---")

# -----------------------------
# DATA
# -----------------------------
zone_df = pd.DataFrame({
    "zone": ["Out of box", "Penalty area", "Six-yard box"],
    "shots": [13, 91, 12],
    "goals": [1, 21, 2],
    "xG": [0.86, 20.82, 4.20]
})

type_df = pd.DataFrame({
    "type": ["Left foot", "Head", "Right foot"],
    "shots": [72, 29, 15],
    "goals": [19, 3, 2],
    "xG": [17.73, 4.11, 4.04]
})

situation_df = pd.DataFrame({
    "situation": ["Open play", "Corner", "Penalty", "Set piece"],
    "shots": [97, 12, 4, 3],
    "goals": [21, 0, 3, 0],
    "xG": [20.33, 2.01, 3.04, 0.50]
})

# -----------------------------
# SIDEBAR
# -----------------------------
section = st.sidebar.radio("Navigate", [
    "Overview",
    "Shot Zones",
    "Shot Types",
    "Situations",
    "Scouting Summary"
])

# -----------------------------
# OVERVIEW
# -----------------------------
if section == "Overview":

    st.header("Performance Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Goals", total_goals)
    col2.metric("xG", total_xg)
    col3.metric("Shots", 116)

    fig, ax = plt.subplots()
    ax.bar(["Goals", "xG"], [total_goals, total_xg])
    ax.set_title("Goals vs xG")
    st.pyplot(fig)

# -----------------------------
# SHOT ZONES
# -----------------------------
elif section == "Shot Zones":

    st.header("Shot Zone Analysis")

    zone_df["Diff"] = zone_df["goals"] - zone_df["xG"]

    fig, ax = plt.subplots()
    ax.bar(zone_df["zone"], zone_df["goals"])
    ax.set_title("Goals by Zone")
    plt.xticks(rotation=20)
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.bar(zone_df["zone"], zone_df["xG"])
    ax2.set_title("xG by Zone")
    plt.xticks(rotation=20)
    st.pyplot(fig2)

    st.dataframe(zone_df)

# -----------------------------
# SHOT TYPES
# -----------------------------
elif section == "Shot Types":

    st.header("Shot Type Breakdown")

    type_df["Diff"] = type_df["goals"] - type_df["xG"]

    fig, ax = plt.subplots()
    ax.bar(type_df["type"], type_df["goals"])
    ax.set_title("Goals by Shot Type")
    plt.xticks(rotation=20)
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.bar(type_df["type"], type_df["xG"])
    ax2.set_title("xG by Shot Type")
    plt.xticks(rotation=20)
    st.pyplot(fig2)

    st.dataframe(type_df)

# -----------------------------
# SITUATIONS
# -----------------------------
elif section == "Situations":

    st.header("Situation Analysis")

    situation_df["Diff"] = situation_df["goals"] - situation_df["xG"]

    fig, ax = plt.subplots()
    ax.pie(situation_df["shots"], labels=situation_df["situation"], autopct="%1.1f%%")
    st.pyplot(fig)

    st.dataframe(situation_df)

# -----------------------------
# SCOUTING SUMMARY
# -----------------------------
elif section == "Scouting Summary":

    st.header("Scouting Report")

    st.markdown("""
    ### Player Profile
    - Elite penalty-box striker  
    - High xG shot selection profile  
    - System-driven goal scorer  

    ### Strengths
    - Exceptional positioning in central zones  
    - Elite left-foot finishing  
    - Consistent open-play goal threat  

    ### Weaknesses
    - Underperformance in six-yard box  
    - Weak aerial conversion vs expectation  
    - Limited right-foot finishing efficiency  

    ### Tactical Insight
    - Majority of goals from open play  
    - Minimal contribution from set pieces  
    - Strong dependence on chance creation system  

    ### Analyst Verdict
    > World-class striker with elite movement and shot selection,  
    > but with untapped potential in high-value scoring situations.
    """)