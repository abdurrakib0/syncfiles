# File Copier

![file-copier](file-copier.png?raw=true)

Copies a list of files into a target directory. Give it a text file with one file path per line (see `sample.txt`) and it copies each file, creating folders as needed. Handles thousands of files and works on Windows, macOS and Linux.

## Usage

```bash
git clone https://github.com/abdurrakib0/syncfiles.git
cd syncfiles
pip install -r requirements.txt
python main.py <list.txt> <destination>
```

## Example

```bash
python main.py sample.txt ./backup
```

Each path in `sample.txt` is copied into `./backup`, keeping its folder structure (the first few leading folders are dropped, set by `EXCLUDE_DIRECTORY_COUNT` in `main.py`).

`sync-folders.py` is a separate helper script in the same repo.

## License

[MIT](LICENSE)
