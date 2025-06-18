{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2bfe1c4-3a2e-44f7-b17a-1347f7628049",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "# Load the trained model\n",
    "model = joblib.load('productivity_predictor.pkl')\n",
    "\n",
    "st.title(\"Remote Worker Productivity Predictor\")\n",
    "\n",
    "st.markdown(\"Upload a CSV file with the following columns:\")\n",
    "st.code(\"task_completion_rate, calendar_scheduled_usage, focus_time_minutes, late_task_ratio\")\n",
    "\n",
    "uploaded_file = st.file_uploader(\"Upload your input CSV file\", type=[\"csv\"])\n",
    "\n",
    "if uploaded_file is not None:\n",
    "    data = pd.read_csv(uploaded_file)\n",
    "\n",
    "    # Ensure required columns\n",
    "    required_cols = ['task_completion_rate', 'calendar_scheduled_usage', 'focus_time_minutes', 'late_task_ratio']\n",
    "    if not all(col in data.columns for col in required_cols):\n",
    "        st.error(f\"Missing columns. Please make sure your CSV has: {', '.join(required_cols)}\")\n",
    "    else:\n",
    "        predictions = model.predict(data[required_cols])\n",
    "        data['predicted_productivity_score'] = predictions\n",
    "        st.success(\"Predictions complete!\")\n",
    "        st.dataframe(data)\n",
    "        csv = data.to_csv(index=False).encode('utf-8')\n",
    "        st.download_button(\"Download Predictions CSV\", csv, \"predictions.csv\", \"text/csv\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
