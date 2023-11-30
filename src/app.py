from st_pages import Page, show_pages

show_pages(
    [
        Page("src/index.py", "Overall", ":house:"),
        Page("src/unemployment.py", "Unemployment", ":briefcase:"),
        Page("src/education_fields.py", "Education", ":books:"),
        Page("src/youth_neets.py", "Youth Neets", "🚫"),
        Page("src/map_for_unemployment.py",
             "Map", ":globe_with_meridians:"),
    ]
)
