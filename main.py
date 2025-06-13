import streamlit as st
import pandas as pd
from data_generator import generate_records
from crud import add_record, update_record, delete_record
from analysis import analyze_sort_algorithms, analyze_search_algorithms
from plot import plot_sorting_results, plot_searching_results


# --- Load Records (you can make this persistent later with file saving)
if "records" not in st.session_state:
    st.session_state.records = generate_records(1000)

records = st.session_state.records
df = pd.DataFrame(records)

# --- Sidebar for CRUD
import streamlit as st
import pandas as pd
from data_generator import generate_records
from crud import add_record, update_record, delete_record
from analysis import analyze_sort_algorithms, analyze_search_algorithms
from plot import plot_sorting_results, plot_searching_results

# --- Load Records
if "records" not in st.session_state:
    st.session_state.records = generate_records(1000)

records = st.session_state.records
df = pd.DataFrame(records)

# --- Sidebar for CRUD
st.sidebar.title("📂 Manage Records")
id_input = st.sidebar.number_input("ID", min_value=1, step=1)
name_input = st.sidebar.text_input("Name")
age_input = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)

if st.sidebar.button("Add"):
    new_record = {"id": id_input, "name": name_input, "age": age_input}
    add_record(records, new_record)
    st.success("✅ Record added!")

if st.sidebar.button("Update"):
    updated_record = {"id": id_input, "name": name_input, "age": age_input}
    if update_record(records, id_input, updated_record):
        st.success("✅ Record updated!")
    else:
        st.error("❌ ID not found.")

if st.sidebar.button("Delete"):
    if delete_record(records, id_input):
        st.success("✅ Record deleted!")
    else:
        st.error("❌ ID not found.")

# --- Main Title
st.title("📊 Data Structures & Algorithms Performance Analyzer")

st.subheader("📋 All Records (Top 100)")
st.dataframe(pd.DataFrame(records).head(100), use_container_width=True)

# --- Sorting Analysis
st.subheader("🌀 Sorting Algorithms Analysis")

sort_mode = st.selectbox("Choose Input Case for Sorting", ["Random", "Sorted (Best Case)", "Reversed (Worst Case)"])
if st.button("Run Sorting Analysis"):
    sizes, sort_data = analyze_sort_algorithms(mode=sort_mode)
    plot_sorting_results(sizes, sort_data)
    st.pyplot()

    df_sort = pd.DataFrame(sort_data, index=sizes)
    st.dataframe(df_sort)
    st.download_button("📥 Download Sort Analysis CSV", df_sort.to_csv(), file_name="sorting_analysis.csv")

# --- Searching Analysis
st.subheader("🔍 Searching Algorithms Analysis")

search_mode = st.selectbox("Choose Input Case for Searching", ["Random", "Sorted (Best Case)", "Reversed (Worst Case)"])
if st.button("Run Searching Analysis"):
    sizes, search_data = analyze_search_algorithms(mode=search_mode)
    plot_searching_results(sizes, search_data)
    st.pyplot()

    df_search = pd.DataFrame(search_data, index=sizes)
    st.dataframe(df_search)
    st.download_button("📥 Download Search Analysis CSV", df_search.to_csv(), file_name="searching_analysis.csv")
