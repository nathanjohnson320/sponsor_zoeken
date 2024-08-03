from bs4 import BeautifulSoup
from app.core.db import get_db
from app.contexts import companies
from app.schemas import CompanyCreate
import urllib.request, csv


COUNTRY = "uk"

uk_data = urllib.request.urlopen(
    "https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers"
)
uk_bytes = uk_data.read()

html = uk_bytes.decode("utf8")
uk_data.close()

parsed = BeautifulSoup(html, "html.parser")

download = parsed.find(class_="govuk-link gem-c-attachment__link")
download_link = download.attrs["href"]

csv_data = urllib.request.urlopen(download_link)
lines = [l.decode("utf-8") for l in csv_data.readlines()]
db = next(get_db())

for row in csv.reader(lines):
    [organization, town_city, county, type_rating, route] = row

    if organization and organization != "Organisation Name":
        company = companies.get_by_name(db, country=COUNTRY, name=organization)
        if not company:
            companies.create(
                db,
                CompanyCreate(
                    name=organization,
                    country=COUNTRY,
                    meta={
                        "town_city": town_city,
                        "county": county,
                        "type_rating": type_rating,
                        "route": route,
                    },
                ),
            )

csv_data.close()
