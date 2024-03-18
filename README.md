Simple scripts for extracting EWDs from the [Edsger W. Dijkstra Archive](https://www.cs.utexas.edu/users/EWD/welcome.html)

## Files

- `ewds.txt`: a list of each page containing links to the various EWD's.
- `entries.json`: A json list of EWDs. Each entry contains the EWD title and document link.
- `download_ewd_indexes.sh`: Downloads every index linked in `ewds.txt`.
- `ewd_html_to_json.sh`: Extracts and folds every EWD entry into a single json file; see `entries.json`. 