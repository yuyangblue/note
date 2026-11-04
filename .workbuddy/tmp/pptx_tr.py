import zipfile, re, shutil, os, sys
sys.stdout.reconfigure(encoding='utf-8')

SRC = r'C:/Users/29469/Desktop/大一下计算机科学导论/课件-CSAPP3e/21-netprog1_中文.pptx'
BAK = SRC.replace('.pptx', '.备份.pptx')

TABLE = {
    # 基础角色与网络词
    'Client': '客户端', 'client': '客户端',
    'Server': '服务器', 'server': '服务器',
    'process': '进程', 'Resource': '资源',
    'host': '主机', 'hub': '集线器', 'bridge': '网桥',
    'router': '路由器', 'Router': '路由器',
    'adapter': '适配器', 'data': '数据',
    'protocol': '协议', 'software': '软件',
    'Kernel': '内核', 'Sockets': '套接字',
    'Firewall': '防火墙', 'Internet': '因特网',
    # 组合标签
    'Web server': 'Web 服务器',
    'Echo server': '回显服务器',
    'Host A': '主机 A', 'Host B': '主机 B',
    'network adapter': '网络适配器', 'Network adapter': '网络适配器',
    'Global IP Internet': '全球 IP 因特网',
    'Internet client host': '因特网客户端主机',
    'Internet server host': '因特网服务器主机',
    'main memory': '主存',
    'CPU chip': 'CPU 芯片',
    'register file': '寄存器文件',
    'system bus': '系统总线',
    'memory bus': '内存总线',
    'I/O bus': 'I/O 总线',
    'Expansion slots': '扩展槽',
    'disk controller': '磁盘控制器',
    'graphics adapter': '图形适配器',
    'USB controller': 'USB 控制器',
    'disk': '磁盘', 'controller': '控制器',
    'mouse': '鼠标', 'keyboard': '键盘', 'monitor': '显示器',
    'network': '网络', 'Network': '网络',
    'port': '端口',
    'WAN': '广域网',
    'LAN1': '局域网 1', 'LAN2': '局域网 2',
    'LAN 1': '局域网 1', 'LAN  2': '局域网 2',
    'LAN1 frame': '局域网 1 帧', 'LAN2 frame': '局域网 2 帧',
    'internet packet': '互联网包',
    'PH': '包头', 'FH1': '帧头 1', 'FH2': '帧头 2',
    'unnamed root': '未命名根',
    'Switched': '交换式',
    'Ethernet, Quadrics QSW, …': '以太网、Quadrics QSW 等',
    'Class A': 'A 类', 'Class B': 'B 类', 'Class C': 'C 类',
    'Class D': 'D 类', 'Class E': 'E 类',
    'Client / Server': '客户端 / 服务器',
    'IP address': 'IP 地址',
    'Unix variants, Windows, OS X, IOS, Android, ARM':
        'Unix 各变体、Windows、OS X、iOS、Android、ARM',
    'cliaddr:cliport': '客户端 IP:端口',
    'servaddr:servport': '服务器 IP:端口',
}

if not os.path.exists(BAK):
    shutil.copy2(SRC, BAK)
    print('已备份 →', os.path.basename(BAK))

hit = {}
def repl(m):
    attr, inner = m.group(1), m.group(2)
    key = inner.strip()
    if key in TABLE:
        hit[key] = hit.get(key, 0) + 1
        return f'<a:t{attr}>{TABLE[key]}</a:t>'
    return m.group(0)

zin = zipfile.ZipFile(SRC)
tmp = SRC + '.tmp'
zout = zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED)
changed = 0
for item in zin.infolist():
    raw = zin.read(item.filename)
    if re.match(r'ppt/slides/slide\d+\.xml$', item.filename):
        text = raw.decode('utf-8')
        new = re.sub(r'<a:t([^>]*)>(.*?)</a:t>', repl, text)
        if new != text:
            changed += 1
            raw = new.encode('utf-8')
    zout.writestr(item, raw)
zout.close(); zin.close()
os.replace(tmp, SRC)

print('改动页数', changed)
print('替换次数合计', sum(hit.values()))
for k in sorted(hit, key=lambda x: -hit[x]):
    print(f'  {k!r:38} -> {TABLE[k]}   x{hit[k]}')
