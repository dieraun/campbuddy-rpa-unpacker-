import sys, os
import zlib, pickle

KEY = 1863002351  # CampBuddy 所有 RPA 通用密钥（Python 2.7 random 验证）

def to_bytes(data):
    if not data: return b''
    if not isinstance(data, bytes): data = data.encode('latin-1')
    return data

def extract_rpa(rpa_path, out_dir):
    with open(rpa_path, 'rb') as f:
        header = f.read(40)
        offset = int(header[8:24], 16)
        f.seek(offset)
        index = pickle.loads(zlib.decompress(f.read()))

    for name, entries in index.items():
        new_entries = []
        for entry in entries:
            if len(entry) == 2:
                o, l = entry
                new_entries.append((o ^ KEY, l ^ KEY, b''))
            else:
                o, l, data = entry
                new_entries.append((o ^ KEY, l ^ KEY, to_bytes(data)))
        index[name] = new_entries

    file_size = os.path.getsize(rpa_path)
    bad = sum(1 for e in index.values()
              for o, l, _ in e if o + l > file_size or l > file_size // 2)
    print(f"条目总数: {len(index)}, 异常条目: {bad}")
    if bad > 0:
        print("⚠ 有条目越界，但通常只有极少数，不影响主体解包。")

    os.makedirs(out_dir, exist_ok=True)
    total = len(index)
    for i, (name, entries) in enumerate(index.items(), 1):
        out_path = os.path.join(out_dir, name)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(rpa_path, 'rb') as f, open(out_path, 'wb') as out:
            for o, l, data in entries:
                f.seek(o)
                out.write(data)
                remaining = l
                while remaining > 0:
                    chunk = f.read(min(remaining, 1 << 20))
                    if not chunk: break
                    out.write(chunk)
                    remaining -= len(chunk)
        if i <= 3 or i % 1000 == 0 or i == total:
            print(f"  [{i}/{total}] {name}")

    print(f"完成！输出: {out_dir}")

if __name__ == '__main__':
    extract_rpa(sys.argv[1], sys.argv[2])