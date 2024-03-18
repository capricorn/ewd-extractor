from ewd_extractor.main import extract_ewd_entries

def test_extract_entries():
    with open('../ewd-index-html/index00xx.html', 'r') as f:
        ewd_index_html = f.read()

    entries = extract_ewd_entries(ewd_index_html)
    assert len(entries) == 24

    assert entries[0]['title'] == 'Substitution processes'
    assert entries[0]['link'] == 'https://www.cs.utexas.edu/users/EWD/ewd00xx/EWD28.PDF'