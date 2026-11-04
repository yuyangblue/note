# -*- coding: utf-8 -*-
"""按段落拼接 run 文本后再替换注释，保留各 run 的样式"""
import zipfile, re, sys, os
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:/Users/29469/Desktop/大一下计算机科学导论/课件-CSAPP3e'
TMP = r'D:/29469/Documents/notes/.workbuddy/tmp'

TRANS = {
    'file descriptor': '文件描述符',
    'number of bytes read': '已读字节数',
    'Address data.': '地址数据',
    'Allocates descriptor': '分配描述符',
    'Blocksize for filesystem I/O': '文件系统 I/O 的块大小',
    'Canonical host name': '规范主机名',
    'Check read access': '检查读权限',
    'Child': '子进程',
    'Clean up': '清理',
    'Connections only': '仅建立连接',
    'Determine file type': '判断文件类型',
    'Device': '设备号',
    'Device type (if inode device)': '设备类型（若为设备文件）',
    'Display address instead of name': '显示地址而非主机名',
    'First arg to socket function': 'socket 的第一个参数',
    'Free linked list': '释放链表',
    'Get a list of addrinfo records': '取得一份 addrinfo 记录',
    'Group ID of owner': '属组 ID',
    'Hints argument flags': 'hints 参数的标志',
    'Hostname or address': '主机名或地址',
    'IP addr in network byte order': 'IP 地址（网络字节序）',
    'IPv4 only': '仅 IPv4',
    'In: socket addr': '输入：套接字地址',
    'Input parameters': '输入参数',
    'Internet address structure': '因特网地址结构',
    'Interrupted by sig handler return': '被信号处理程序返回中断',
    'Metadata returned by the stat and fstat functions': 'stat 与 fstat 返回的元数据',
    'Number of blocks allocated': '已分配的块数',
    'Number of hard links': '硬链接数',
    'Open file fd ...': '打开文件 fd ...',
    'Open the file fd ...': '打开该文件 fd ...',
    'Out: host': '输出：主机名',
    'Out: service': '输出：服务',
    'Output linked list': '输出链表',
    'Pad to sizeof(struct sockaddr)': '填充至 sizeof(struct sockaddr)',
    'Parent': '父进程',
    'Port num in network byte order': '端口号（网络字节序）',
    'Port or service name': '端口号或服务名',
    'Protection and file type': '保护模式与文件类型',
    'Protocol family': '协议族',
    'Protocol family (always AF_INET)': '协议族（固定为 AF_INET）',
    'Ptr to next item in linked list': '指向链表中的下一项',
    'Ptr to socket address structure': '指向套接字地址结构',
    'Return &gt;= 0': '返回值 &gt;= 0',
    'Return error msg': '返回错误信息',
    'Second arg to socket function': 'socket 的第二个参数',
    'Size of ai_addr struct': 'ai_addr 结构的大小',
    'Then read up to 512 bytes from file fd': '再从文件 fd 读至多 512 字节',
    'Then write up to 512 bytes from buf to file fd': '再把 buf 中至多 512 字节写入文件 fd',
    'Third arg to socket function': 'socket 的第三个参数',
    'Time of last access': '最后访问时间',
    'Time of last change': '最后状态变更时间',
    'Time of last modification': '最后修改时间',
    'Total size, in bytes': '总大小（字节）',
    'User ID of owner': '属主用户 ID',
    'Walk the list and display each IP address': '遍历链表并显示每个 IP 地址',
    'and call read() again': '并再次调用 read()',
    'descriptor for this internal buf': '该内部缓冲区的描述符',
    'errno set by read()': 'read() 设置的 errno',
    'internal buffer': '内部缓冲区',
    'network byte order (big-endian)': '网络字节序（大端）',
    'next unread byte in internal buf': '内部缓冲区中下一个未读字节',
    'optional flags': '可选标志',
    'return value': '返回值',
    'standard error  (descriptor 2)': '标准错误（描述符 2）',
    'standard input  (descriptor 0)': '标准输入（描述符 0）',
    'standard output (descriptor 1)': '标准输出（描述符 1）',
    'unread bytes in internal buf': '内部缓冲区中未读字节数',
}

RUN_RE = re.compile(r'<a:t((?:\s[^>]*[^/>])?)>(.*?)</a:t>', re.S)


def process_para(p_xml):
    runs = list(RUN_RE.finditer(p_xml))
    if not runs:
        return p_xml, 0
    texts = [m.group(2) for m in runs]
    starts, pos = [], 0
    for t in texts:
        starts.append(pos)
        pos += len(t)
    full = ''.join(texts)
    if '/*' not in full:
        return p_xml, 0

    spans = []
    for m in re.finditer(r'/\*(.*?)\*/', full, re.S):
        core = m.group(1).strip()
        if core in TRANS:
            inner = m.group(1)
            lead = inner[:len(inner) - len(inner.lstrip())]
            trail = inner[len(inner.rstrip()):]
            spans.append((m.start(), m.end(), '/*' + lead + TRANS[core] + trail + '*/'))
    if not spans:
        return p_xml, 0

    new_texts = list(texts)
    for cs, ce, rep in sorted(spans, key=lambda x: -x[0]):
        cover = [i for i, t in enumerate(texts)
                 if not (starts[i] + len(t) <= cs or starts[i] >= ce)]
        if not cover:
            continue
        i0, i1 = cover[0], cover[-1]
        if i0 == i1:
            s = starts[i0]
            new_texts[i0] = texts[i0][:cs - s] + rep + texts[i0][ce - s:]
        else:
            new_texts[i0] = texts[i0][:cs - starts[i0]] + rep
            for k in cover[1:-1]:
                new_texts[k] = ''
            new_texts[i1] = texts[i1][ce - starts[i1]:]

    if new_texts == texts:
        return p_xml, 0

    out, last = [], 0
    for idx, m in enumerate(runs):
        out.append(p_xml[last:m.start(2)])
        out.append(new_texts[idx])
        last = m.end(2)
    out.append(p_xml[last:])
    return ''.join(out), len(spans)


FILES = ['21-netprog1_中文.pptx', '16-io_中文.pptx']
for fn in FILES:
    src = os.path.join(BASE, fn)
    zin = zipfile.ZipFile(src)
    tmpout = os.path.join(TMP, fn + '.new')
    zout = zipfile.ZipFile(tmpout, 'w', zipfile.ZIP_DEFLATED)
    total = 0
    for item in zin.infolist():
        data = zin.read(item.filename)
        if re.match(r'ppt/slides/slide\d+\.xml$', item.filename):
            txt = data.decode('utf-8')
            seg, last = [], 0
            for pm in re.finditer(r'<a:p>(.*?)</a:p>', txt, re.S):
                seg.append(txt[last:pm.start()])
                p_new, k = process_para('<a:p>' + pm.group(1) + '</a:p>')
                total += k
                seg.append(p_new[5:-6])
                last = pm.end()
            seg.append(txt[last:])
            data = ''.join(seg).encode('utf-8')
        zout.writestr(item, data)
    zout.close()
    zin.close()
    print('%s 替换 %d 处' % (fn, total))
