<img src="https://www.statistics.gov.rw/sites/default/files/images/logo.png" alt="NISR logo">

# Addressing youth unemployment dashboard

This project creates an interactive dashboard to explore labor force survey data especially for addressing unemployed Rwandan youth. After founding that 25.6% of youth who's in 16-30 years old are unemployed which means 1 guy in 4 of youth are unemployed, Thereafter I came with the story of creating a dashboard that will highlight this severe condition and see if these insights can help to track where the problem at.

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

## Important links
- [Hackathon & Infographics Competition - 2023 Edition](https://statistics.gov.rw/about-us/hackathon-competition-2023-edition)
- [Labour Force Survey Annual Report 2022](https://www.statistics.gov.rw/publication/1919)

## Contact

If you have any questions or comments, feel free to reach out!
