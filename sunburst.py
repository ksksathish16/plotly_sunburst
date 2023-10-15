import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv("EmployeeSampleData.csv", encoding='unicode_escape')
df["Age"] = pd.to_numeric(df["Age"], errors='coerce').fillna(0).astype(np.int64)

df = df[df["Ethnicity"].isin(['Asian', 'Caucasian', 'Latino'])]
df = df[df["Country"].isin(["United States", "China", "Brazil", "Asian"])]


fig = px.sunburst(
    data_frame=df,
    path=["Department", 'Business Unit', "Country"],  # Root, branches, leaves
    color="Department",
    color_discrete_sequence=px.colors.qualitative.Pastel,
)

fig.update_traces(textinfo='label+percent entry')
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()