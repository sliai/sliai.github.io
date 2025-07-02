import ark
import bibtexparser
import shortcodes

def find_entry(library: dict[str, str], citekey: str):
    for entry in library.entries:
        if entry.key == citekey:
            for k, v in entry.items():
                # Normalize all keys to lowercase
                entry.set_field(bibtexparser.model.Field(k.lower(), v))
            return entry
    return f"{citekey} not found"

@shortcodes.register('bibitem')
def handler(pargs, kwargs, node):
    path = ark.site.inc(kwargs["bibfile"])
    with open(path) as fin:
        bibtex_str = fin.read()
    library = bibtexparser.parse_string(bibtex_str)
    entry = find_entry(library, kwargs["citekey"])
    author = entry["author"]
    title = entry["title"]
    venue = entry["journal"] if "journal" in entry else \
        entry["booktitle"] if "booktitle" in entry else ""
    address = entry["address"] if "address" in entry else ""
    month = entry["month"] if "month" in entry else ""
    year = entry["year"] if "year" in entry else ""
    pdf = entry["pdf"] if "pdf" in entry else ""

    return f'{author}. {title}. <i>{venue}</i>. {address}. {month}. {year}. <a href="{pdf}" _target="blank">PDF</a>'