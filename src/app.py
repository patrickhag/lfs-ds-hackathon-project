from st_pages import Page, show_pages, add_page_title

add_page_title()

show_pages(
    [
        Page("src/index.py", "Home page", ":books:"),
        Page("src/unemployment.py", "youth unemployment", "🏠"),
        Page("src/education_fields.py", "education fields", ":books:"),
        Page("src/youth_neets.py", "Youth Neets", ":books:"),
        Page("src/map_for_unemployment.py", "View unemployment map", ":books:"),
    ]
)
