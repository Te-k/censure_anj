import requests
import os
import sys
from datetime import datetime

URL = "https://ressources.anj.fr/blocage_sites_illegaux/blocage_sites_illegaux.csv"


if __name__ == "__main__":
    path = os.path.dirname(__file__)
    current = os.path.join(path, "current.csv")
    monthly = os.path.join(path, "archives", "{}{:02d}_blocage_sites_illegaux.csv".format(datetime.now().year, datetime.now().month))

    r = requests.get(URL)
    if r.status_code != 200:
        print("Fichier non trouvé")
        sys.exit(1)

    content = r.text

    if os.path.isfile(current):
        os.remove(current)
    with open(current, "w+") as f:
        f.write(content)

    if os.path.isfile(monthly):
        os.remove(monthly)
    with open(monthly, "w+") as f:
        f.write(content)





