import streamlit as st
import pandas as pd

st.set_page_config(page_title="Immunization Code Crosswalk", page_icon="💉", layout="wide")

st.title("💉 Immunization Code Crosswalk")
st.caption("Crosswalk lookup tool for NDC, CVX, CPT, and EHR EAP procedure codes.")

# Replace or extend with a full CDC CSV dataset
data = [
    {
        "NDC": "00006-4047-41",
        "Trade Name": "RotaTeq",
        "CVX Code": "116",
        "CVX Description": "rotavirus, pentavalent",
        "CPT Code": "90680",
        "EAP Record": "IMM57",
        "EAP Description": "ROTAVIRUS VACCINE PENTAVALENT 3 DOSE ORAL",
        "Status": "Active"
    }
]

df = pd.DataFrame(data)

query = st.text_input("🔍 Search by NDC, CPT, CVX, EAP, or Vaccine Name:", "")

if query:
    results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    st.dataframe(results, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)
