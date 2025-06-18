
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('productivity_predictor.pkl')

st.title("Remote Worker Productivity Predictor")

st.markdown("Upload a CSV file with the following columns:")
st.code("task_completion_rate, calendar_scheduled_usage, focus_time_minutes, late_task_ratio")

uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Ensure required columns
    required_cols = ['task_completion_rate', 'calendar_scheduled_usage', 'focus_time_minutes', 'late_task_ratio']
    if not all(col in data.columns for col in required_cols):
        st.error(f"Missing columns. Please make sure your CSV has: {', '.join(required_cols)}")
    else:
        predictions = model.predict(data[required_cols])
        data['predicted_productivity_score'] = predictions
        st.success("Predictions complete!")
        st.dataframe(data)
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button("Download Predictions CSV", csv, "predictions.csv", "text/csv")
