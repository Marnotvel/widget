def filter_by_state(glossary, state: str = "EXECUTED"):
    for i in glossary:
        if i['state'] != state:
            glossary = [x for x in glossary if x != i]
    return glossary


def sort_by_date(glossary):
    sorted(glossary, key=lambda x: x['date'], reverse=True)
    return glossary
