import pandas as pd

df = pd.read_csv("../data/survey_data.csv")

df = df.drop_duplicates()

df["feedback_text"] = df["feedback_text"].str.strip()

df.to_csv("../data/cleaned_survey_data.csv", index=False)

print("Data cleaned and saved.")
