# Labor Force Dashboard

This project creates an interactive dashboard to explore labor force survey data especially for addressing unemployed Rwandan youth.

## How it works

The dashboard is built using the [Streamlit](https://streamlit.io/) library in Python. Streamlit allows creating web apps directly in Python scripts.

Some key Python packages used:

- [**Streamlit**](https://streamlit.io/) - to build the web interface
- [**Pandas**](https://pandas.pydata.org/) - to load and work with the data from Excel files
- [**Plotly**](https://plotly.com/python/) - to create interactive charts and graphs
- [**Streamlit-folium**](https://streamlit-folium.readthedocs.io/en/latest/) - to display interactive maps

The user interface is created with Streamlit components like buttons, dropdowns, text inputs etc. These are used to select data and display different views.

Plots and maps are generated dynamically based on user input using Plotly and Streamlit-folium.

## Running the dashboard

To run the dashboard locally:

- Install required packages
- Run `streamlit run app.py`
- View dashboard at http://localhost:8501

The app is still in development. More features will be added over time.

## Data sources

The data is sourced from the (Rwanda Labour Force Survey reports)[]. It includes indicators on the labor force, employment, unemployment, education etc.

The dashboard provides an easy way to explore trends and patterns in the labor market data. It aims to make the key insights more accessible to the general public.

## Contributors

Contributions are welcome! Please create an issue or pull request on GitHub.

Some ways to contribute:

- Fix bugs
- Add new data visualizations
- Improve interactive features
- Write documentation

## Contact

If you have any questions or comments, feel free to reach out!
