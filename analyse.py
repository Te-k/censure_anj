import csv
import os


def csv_count(fpath) -> (int, int):
    """
    Count the number of sites and domains in a file
    """
    fin = open(fpath)
    reader = csv.reader(fin, delimiter=';')
    next(reader)
    sites = []
    domains = []
    for row in reader:
        if row[0].lower() not in sites:
            sites.append(row[0].lower())
        domain = row[1].strip().lower()
        if domain.startswith("www."):
            domain = domain[4:]
        if domain not in domains:
            domains.append(domain)

    return (len(sites), len(domains))


if __name__ == "__main__":
    files = [f for f in os.listdir("archives")]
    for f in sorted(files):
        nb_sites, nb_domains = csv_count(os.path.join("archives", f))
        print("{} : {} sites - {} domains".format(f, nb_sites, nb_domains))

