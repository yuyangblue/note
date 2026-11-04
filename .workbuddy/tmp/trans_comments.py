# -*- coding: utf-8 -*-
"""把中译课件里代码的英文注释翻成中文（只动 /* */ 内部，代码不动）"""
import zipfile, re, sys, os, shutil

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

FILES = ['21-netprog1_中文.pptx', '16-io_中文.pptx']


def fix_text(text):
    """替换一个 a:t 内的 /* */ 注释，返回 (新文本, 替换数)"""
    n = [0]

    def f(m):
        inner = m.group(1)
        core = inner.strip()
        if core in TRANS:
            lead = inner[:len(inner) - len(inner.lstrip())]
            trail = inner[len(inner.rstrip()):]
            n[0] += 1
            return '/*' + lead + TRANS[core] + trail + '*/'
        return m.group(0)

    return re.sub(r'/\*(.*?)\*/', f, text, flags=re.S), n[0]


for fn in FILES:
    src = os.path.join(BASE, fn)
    if not os.path.exists(src):
        print('缺失', fn); continue

    zin = zipfile.ZipFile(src)
    tmpout = os.path.join(TMP, fn + '.new')
    zout = zipfile.ZipFile(tmpout, 'w', zipfile.ZIP_DEFLATED)
    total = 0
    missed = []
    for item in zin.infolist():
        data = zin.read(item.filename)
        if re.match(r'ppt/slides/slide\d+\.xml$', item.filename):
            txt = data.decode('utf-8')
            new, k = fix_text(txt)
            total += k
            # 记录仍存在的英文注释
            for m in re.finditer(r'/\*(.*?)\*/', new, flags=re.S):
                c = m.group(1).strip()
                if c and re.search(r'[A-Za-z]{2,}', c) and not re.search(r'[\u4e00-\u9fff]', c):
                    missed.append((item.filename, c))
            data = new.encode('utf-8')
        zout.writestr(item, data)
    zout.close()
    zin.close()

    print('%s: 替换 %d 处' % (fn, total))
    if missed:
        print('  仍为英文的注释 %d 条:' % len(missed))
        seen = set()
        for f_, c in missed:
            if c in seen: continue
            seen.add(c)
            print('    ', c)
    else:
        print('  没有剩余英文注释')
