"""不依赖 Pillow，直接解码 PNG，测量文本行的像素尺寸。
用法：python measure_text.py <图片路径>
"""
import struct
import sys
import zlib


def load_png(path):
    with open(path, 'rb') as f:
        data = f.read()
    assert data[:8] == b'\x89PNG\r\n\x1a\n', 'not a png'
    pos = 8
    idat = b''
    w = h = bitdepth = colortype = None
    while pos < len(data):
        length = struct.unpack('>I', data[pos:pos + 4])[0]
        ctype = data[pos + 4:pos + 8]
        chunk = data[pos + 8:pos + 8 + length]
        if ctype == b'IHDR':
            w, h, bitdepth, colortype = struct.unpack('>IIBB', chunk[:10])
        elif ctype == b'IDAT':
            idat += chunk
        elif ctype == b'IEND':
            break
        pos += 12 + length
    raw = zlib.decompress(idat)
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[colortype]
    assert bitdepth == 8, f'bitdepth {bitdepth} unsupported'
    stride = w * channels
    out = bytearray(w * h * channels)
    prev = bytearray(stride)
    p = 0
    for y in range(h):
        ft = raw[p]
        p += 1
        line = bytearray(raw[p:p + stride])
        p += stride
        if ft == 1:
            for i in range(channels, stride):
                line[i] = (line[i] + line[i - channels]) & 0xff
        elif ft == 2:
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 0xff
        elif ft == 3:
            for i in range(stride):
                a = line[i - channels] if i >= channels else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 0xff
        elif ft == 4:
            for i in range(stride):
                a = line[i - channels] if i >= channels else 0
                b = prev[i]
                c = prev[i - channels] if i >= channels else 0
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pr) & 0xff
        out[y * stride:(y + 1) * stride] = line
        prev = line
    return w, h, channels, out


def measure(path):
    w, h, ch, px = load_png(path)
    stride = w * ch

    def gray(x, y):
        i = y * stride + x * ch
        if ch >= 3:
            return (px[i] * 299 + px[i + 1] * 587 + px[i + 2] * 114) // 1000
        return px[i]

    # 判断底色明暗，选用"深色墨水"还是"浅色墨水"
    corners = [gray(2, 2), gray(w - 3, 2), gray(2, h - 3), gray(w - 3, h - 3)]
    bg = sum(corners) // 4
    dark_bg = bg < 128
    thresh = bg + 60 if dark_bg else bg - 60

    def is_ink(x, y):
        g = gray(x, y)
        return (g > thresh) if dark_bg else (g < thresh)

    # 行投影：每行墨点数
    rows = []
    for y in range(h):
        c = 0
        for x in range(0, w):
            if is_ink(x, y):
                c += 1
        rows.append(c)

    # 把连续有墨的行切成文本带
    bands = []
    start = None
    for y, c in enumerate(rows):
        if c > 0 and start is None:
            start = y
        elif c == 0 and start is not None:
            if y - start >= 2:
                bands.append((start, y - 1))
            start = None
    if start is not None:
        bands.append((start, h - 1))

    print(f'尺寸 {w}x{h}  底色灰={bg}  {"深底浅字" if dark_bg else "浅底深字"}')
    print(f'切出 {len(bands)} 个文本带\n')
    print(f'{"行号":>4} {"y起":>5} {"y止":>5} {"高px":>5} {"x起":>5} {"x止":>5} {"宽px":>5} {"宽/高":>6}')
    for i, (y0, y1) in enumerate(bands):
        # 该带内所有墨点的横向范围
        xmin, xmax = w, -1
        for y in range(y0, y1 + 1):
            for x in range(w):
                if is_ink(x, y):
                    if x < xmin:
                        xmin = x
                    if x > xmax:
                        xmax = x
        bh = y1 - y0 + 1
        bw = xmax - xmin + 1 if xmax >= 0 else 0
        print(f'{i:>4} {y0:>5} {y1:>5} {bh:>5} {xmin:>5} {xmax:>5} {bw:>5} {bw / bh:>6.2f}')


if __name__ == '__main__':
    measure(sys.argv[1])
