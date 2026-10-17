import hashlib, zlib, pickle, random, sys

def diag(rpa_path):
    with open(rpa_path, 'rb') as f:
        header = f.read(40)
        offset = int(header[8:24], 16)
        print(f"索引偏移: {offset}")
        f.seek(offset)
        raw = zlib.decompress(f.read())
        index = pickle.loads(raw)

    print(f"索引条目数: {len(index)}")

    md5_made = hashlib.md5("Made with Ren'Py.".encode()).hexdigest()
    seed = int(hashlib.md5((md5_made[:8] + 'RPA-3.0').encode()).hexdigest()[:8], 16)
    random.seed(seed)
    r1 = random.randint(0, 65535) ^ 43690
    r2 = random.randint(0, 65535) ^ 21845
    key = (r1 << 16 | r2) ^ 3067549256
    print(f"key: {key}\n")

    for i, (name, entries) in enumerate(index.items()):
        if i >= 8:
            break
        print(f"[{i}] {name}")
        print(f"    entries 类型: {type(entries).__name__}, 长度: {len(entries)}")
        for j, e in enumerate(entries[:2]):
            print(f"    entry[{j}] 类型: {type(e).__name__}, 长度: {len(e)}, 原始值: {e}")
            if isinstance(e, (tuple, list)):
                dec = tuple(x ^ key if isinstance(x, int) else f"<{type(x).__name__}:{len(x)}>" for x in e)
                print(f"    解密后: {dec}")
        print()

if __name__ == '__main__':
    diag(sys.argv[1])