from st_pages import Page, show_pages, add_page_title

add_page_title()

show_pages(
    [
        Page("unemployment.py", "youth unemployment", "🏠"),
        Page("education_fields.py", "education fields", ":books:"),
    ]
)
