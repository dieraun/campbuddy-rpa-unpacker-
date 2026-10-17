```
# CampBuddy RPA Extractor
A Python tool for decrypting and extracting Ren'Py RPA archive files used by CampBuddy.

> ⚠️ This tool is only for **personal research, learning and archival purposes**.

## Background
CampBuddy uses a modified‑encrypted Ren'Py RPA‑3.0 archive format.
The official Ren'Py rpa extractor cannot directly unpack these archives, because the file offset/length values in index entries are XOR‑obfuscated with a fixed custom key.

This project implements the known fixed decryption key to decode offset and length metadata, then extract original assets from `.rpa` files.

## Features
- Decrypt CampBuddy‑style obfuscated RPA‑3.0 index metadata
- Batch‑extract files from RPA archives
- Simple diagnostic script to inspect raw RPA index structure
- Detect out‑of‑bounds index entries and give warning hints

## Requirements
- Python 3.7+
- No extra third‑party packages required for main extractor (`decrypt_rpa.py`)

> Note: `verify.py` uses `random2` for legacy Python 2.7 random seed reproduction, it is only for key verification research and **not required for normal extraction workflow**.

## File List
| File | Purpose |
|---|---|
| `decrypt_rpa.py` | Main extraction script, use this for unpacking RPA files |
| `diag.py` | Diagnostic debug tool: print raw index entries, inspect obfuscated values |
| `verify.py` | Research‑only: reproduce how the fixed XOR key was derived from Python2.7 random |
| `DISCLAIMER.md` | Full legal disclaimer document |
| `LICENSE` | MIT open‑source license |

## Usage

### 1. Main extract (decrypt & unpack)
```bash
python decrypt_rpa.py your_archive.rpa output_folder
```

- `your_archive.rpa`: Path to CampBuddy `.rpa` file
- `output_folder`: Directory for extracted original files (will auto‑create if missing)

### 2. Diagnostic inspection

If you want to view raw index data for debugging:

```
python diag.py your_archive.rpa
```

### 3. Key reproduction (research only)

> 
> Not needed for normal use. Requires install `random2` package.

```
pip install random2
python verify.py
```

## Important Disclaimer

**DISCLAIMER**
This software is provided "as‑is", without warranty of any kind, express or implied.

1. This tool is for **educational, personal reverse‑engineering research and private archival purposes only**.
2. You may only process game assets that you **legally own and possess**.
3. You are NOT permitted to use output assets for commercial use, public redistribution, republishing, or any violation of the original copyright of CampBuddy and its copyright holders.
4. Any usage of this tool that violates local copyright law or the game’s End‑User License Agreement (EULA) is entirely your own responsibility. The author takes zero liability for any misuse, damage or legal consequences arising from your operation of this program.
5. Do not share, distribute or leak extracted copyrighted game resources to public internet platforms.

Full legal terms are available in [DISCLAIMER.md](./DISCLAIMER.md).

## Known limitations

- A small number of index entries may show offset/length out‑of‑bounds warnings; this is an artifact of original archive, most game assets can still extract correctly.
- Only targets CampBuddy modified RPA‑3.0 archives, does not guarantee compatibility with other custom‑patched Ren'Py RPA files.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

```

---

### LICENSE
```

MIT License

Copyright (c) 2026 dieraun

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

### DISCLAIMER.md
```markdown
# Disclaimer

> Read this document carefully before using this software.

This Python tool is built solely for **educational study, personal reverse‑engineering research, and private archival purposes**.

1. You are only authorized to operate on game files and assets which you **legally own and have legitimately acquired**.
2. This tool decrypts archive metadata of CampBuddy’s modified Ren'Py RPA‑3.0 format. The copyright of all extracted game content belongs exclusively to the respective copyright holders of CampBuddy.
3. You **must not** use any extracted assets for commercial activities, public display, reposting, redistribution, leak, or any behavior that infringes copyright, violates the game’s End‑User License Agreement (EULA), or breaks local laws.
4. This software is distributed **"AS‑IS"**, without any form of guarantee. The author (dieraun) provides no warranty regarding functionality, stability or safety.
5. All operations performed with this tool are at your own risk. The author shall not be held liable for any direct or indirect consequences including, but not limited to: file damage, data loss, copyright disputes, legal penalties, or other losses arising from improper or illegal use of this program.
6. If you do not agree to the terms of this disclaimer, please do not use this software.
```

### .gitignore

```
__pycache__/
*.pyc
*.pyo
*.pyd
*.rpa
output/
extracted/
*.log
```

**Repository file tree summary**

```
├── README.md
├── LICENSE
├── DISCLAIMER.md
├── .gitignore
├── decrypt_rpa.py
├── diag.py
└── verify.py
```

> 
> Important: Do **not** commit any game rpa files or extracted game content.