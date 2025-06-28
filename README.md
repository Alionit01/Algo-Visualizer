
# Algorithm Visualizer

This is a small project I built to better understand how sorting and searching algorithms work — and how they perform with different kinds of data. The idea was to create an interactive tool that lets users add data, run algorithms on it, and see how they behave through visual graphs.


## What It Does

- Lets you **add**, **update**, **delete**, and **view** records (like people with name, age, etc.).
- You can sort records by age using:
  - Bubble Sort
  - Quick Sort
  - Merge Sort
- You can also search records using:
  - Linear Search
  - Binary Search
- It shows how long each algorithm takes as the number of records increases.
- All of this is displayed in a clean UI using **Streamlit**.


## Why I Made This

I wanted to go beyond just writing code that "works." I wanted to **visualize performance**, see how algorithms behave in best/worst cases, and get more comfortable with data structures like lists and dictionaries. This was also a chance to practice using Streamlit to build a simple, interactive app.



## How to Run

1. Make sure you have Python 3 installed.
2. Install required libraries:
   ```bash
   pip install streamlit matplotlib
````

3. Run the app:

   ```bash
   streamlit run main.py
   ```


## A Few Screens You’ll See

* Sorting graphs (comparing time taken)
* Searching time graph (Linear vs Binary)
* Table showing top 100 records
* CRUD sidebar where you can manage records


## Limitations I Noticed

* Quick Sort can sometimes cause recursion errors with reversed or sorted inputs if not handled properly.
* Bubble Sort is very slow once the data gets large (as expected).
* Data isn’t saved permanently — it’s all in-memory for now.
* Streamlit has some limitations with large recursion on hosted apps.


## What I Learned

* How different algorithms behave with different input types.
* Importance of picking the right algorithm based on data.
* How to visualize algorithm performance clearly.
* Basics of building interactive Python apps with Streamlit.


## License

This is a personal learning project, but feel free to fork it, use it, or improve it.

```


