import streamlit as st
import pandas as pd
from data_generator import generate_records
from crud import add_record, update_record, delete_record
from analysis import analyze_sort_algorithms, analyze_search_algorithms
from plot import plot_sorting_results, plot_searching_results
from sorting import bubble_sort, quick_sort, merge_sort
from searching import linear_search, binary_search

# --- Load Records
if "records" not in st.session_state:
    st.session_state.records = generate_records(1000)

records = st.session_state.records

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
df = pd.DataFrame(records)
st.dataframe(df.head(100), use_container_width=True)

# --- Sorting Analysis
st.subheader("🌀 Sorting Algorithms Analysis")
sort_mode = st.selectbox("Choose Input Case for Sorting", ["Random", "Sorted (Best Case)", "Reversed (Worst Case)"])
if st.button("Run Sorting Analysis"):
    sizes, sort_data = analyze_sort_algorithms(mode=sort_mode)
    fig = plot_sorting_results(sizes, sort_data)
    st.pyplot(fig)

    df_sort = pd.DataFrame(sort_data, index=sizes)
    st.dataframe(df_sort)
    st.download_button("📥 Download Sort Analysis CSV", df_sort.to_csv(), file_name="sorting_analysis.csv")

    st.markdown("### ⏱️ Asymptotic Notation for Sorting")
    st.markdown("""
    - **Bubble Sort**: Best: O(n), Average: O(n²), Worst: O(n²)  
    - **Quick Sort**: Best: O(n log n), Average: O(n log n), Worst: O(n²)  
    - **Merge Sort**: Best: O(n log n), Average: O(n log n), Worst: O(n log n)
    """)

# --- Searching Analysis
st.subheader("🔍 Searching Algorithms Analysis")
search_mode = st.selectbox("Choose Input Case for Searching", ["Random", "Sorted (Best Case)", "Reversed (Worst Case)"])
if st.button("Run Searching Analysis"):
    sizes, search_data = analyze_search_algorithms(mode=search_mode)
    fig = plot_searching_results(sizes, search_data)
    st.pyplot(fig)

    df_search = pd.DataFrame(search_data, index=sizes)
    st.dataframe(df_search)
    st.download_button("📥 Download Search Analysis CSV", df_search.to_csv(), file_name="searching_analysis.csv")

    st.markdown("### ⏱️ Asymptotic Notation for Searching")
    st.markdown("""
    - **Linear Search**: Best: O(1), Average: O(n), Worst: O(n)  
    - **Binary Search**: Best: O(1), Average: O(log n), Worst: O(log n)
    """)

# --- Search Individual Record
st.subheader("🔎 Search a Record by ID")
search_id = st.number_input("Enter ID to Search", min_value=1, step=1, key="search")
search_algo = st.selectbox("Search Algorithm", ["Linear Search", "Binary Search"], key="search_algo")
if st.button("Search Record"):
    sorted_records = sorted(records, key=lambda x: x['id'])
    if search_algo == "Linear Search":
        index = linear_search([r['id'] for r in records], search_id)
        if index != -1:
            st.write(records[index])
        else:
            st.warning("Not found.")
    else:
        index = binary_search([r['id'] for r in sorted_records], search_id)
        if index != -1:
            st.write(sorted_records[index])
        else:
            st.warning("Not found.")

# --- Sort Records
st.subheader("📑 Sort Records by Age")
sort_algo = st.selectbox("Sort Algorithm", ["Bubble Sort", "Quick Sort", "Merge Sort"], key="sort_algo")
if st.button("Sort Records"):
    key_func = lambda x: x["age"]
    if sort_algo == "Bubble Sort":
        sorted_list = bubble_sort(records.copy(), key=key_func)
    elif sort_algo == "Quick Sort":
        sorted_list = quick_sort(records.copy(), key=key_func)
    else:
        sorted_list = merge_sort(records.copy(), key=key_func)

    st.dataframe(pd.DataFrame(sorted_list).head(100), use_container_width=True)

