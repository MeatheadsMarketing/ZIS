import altair as alt
import pandas as pd

def analyze_tradeoffs(selected_file, cheat_code):
    df = pd.DataFrame({"Criteria": ["Speed", "Readability", "Maintainability"],
                       "Score": [80, 65, 70]})
    return alt.Chart(df).mark_bar().encode(x='Criteria', y='Score', tooltip=['Criteria', 'Score'])