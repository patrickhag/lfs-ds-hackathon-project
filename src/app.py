from st_pages import Page, show_pages, add_page_title

add_page_title()

show_pages(
    [
        Page("src/unemployment.py", "youth unemployment", "🏠"),
        Page("src/education_fields.py", "education fields", ":books:"),
    ]
)
