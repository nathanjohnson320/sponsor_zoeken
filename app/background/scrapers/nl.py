from bs4 import BeautifulSoup
from app.core.db import get_db
from app.contexts import companies
import urllib.request


ind_data = urllib.request.urlopen(
    "https://ind.nl/en/public-register-recognised-sponsors/public-register-regular-labour-and-highly-skilled-migrants"
)
ind_bytes = ind_data.read()

html = ind_bytes.decode("utf8")
ind_data.close()

parsed = BeautifulSoup(html, "html.parser")

table = parsed.find("table")

db = next(get_db())

for row in table.find_all("tr"):
    organization = row.find("th")
    meta = row.find("td")
    if organization and meta:
        organization = organization.string
        kvk_number = meta.string

        company = companies.get_by_name(db, organization)
        if not company:
            companies.create(db, name=organization, meta={"kvk_number": kvk_number})

print("Done")
