<html style="margin:0;padding:0;">
<div style="width:100%;max-width:980px;margin:0 auto;box-sizing:border-box;padding:20px 16px;font-family:'Microsoft YaHei','PingFang SC',Segoe UI,sans-serif;color:#1A1B1C;">

  <h2 style="font-size:21px;margin:0 0 6px;">关系复合运算定律 · 图解</h2>
  <p style="font-size:14px;line-height:1.6;color:#5F6670;margin:0 0 18px;">
    记号 <span style="color:#4F6B9A;font-weight:600;">R₁R₂</span> 表示复合（先走 R₁ 再走 R₂）。
    核心直观：<b>复合 = 在关系图上"走两步"，能经过某个中间结点到达，就连一条边。</b>
  </p>

  <!-- 图1：复合=走两步 -->
  <div style="font-size:15px;font-weight:600;margin:8px 0 4px;">① 复合就是"把两步压成一步"</div>
  <svg viewBox="0 0 900 250" style="width:100%;height:auto;display:block;">
    <defs>
      <marker id="ab" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#4F6B9A"/></marker>
      <marker id="ag" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#35705A"/></marker>
      <marker id="ad" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#1A1B1C"/></marker>
    </defs>
    <text x="120" y="42" text-anchor="middle" font-size="14" fill="#5F6670">A</text>
    <text x="450" y="42" text-anchor="middle" font-size="14" fill="#5F6670">B</text>
    <text x="780" y="42" text-anchor="middle" font-size="14" fill="#5F6670">C</text>
    <line x1="144" y1="130" x2="426" y2="130" stroke="#4F6B9A" stroke-width="2.2" marker-end="url(#ab)"/>
    <line x1="474" y1="130" x2="756" y2="130" stroke="#35705A" stroke-width="2.2" marker-end="url(#ag)"/>
    <text x="285" y="118" text-anchor="middle" font-size="14" fill="#4F6B9A" font-weight="600">R₁</text>
    <text x="615" y="118" text-anchor="middle" font-size="14" fill="#35705A" font-weight="600">R₂</text>
    <path d="M132,150 Q450,238 768,150" fill="none" stroke="#1A1B1C" stroke-width="2" stroke-dasharray="7 6" marker-end="url(#ad)"/>
    <text x="450" y="222" text-anchor="middle" font-size="14" fill="#1A1B1C" font-weight="600">复合 R₁∘R₂：a 走两步能到 c，就有 a→c</text>
    <g font-size="15" font-weight="600">
      <circle cx="120" cy="130" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <circle cx="450" cy="130" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <circle cx="780" cy="130" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <text x="120" y="136" text-anchor="middle">a</text>
      <text x="450" y="136" text-anchor="middle">b</text>
      <text x="780" y="136" text-anchor="middle">c</text>
    </g>
  </svg>

  <!-- 图2：并 → 等号 -->
  <div style="font-size:15px;font-weight:600;margin:20px 0 4px;">② 对"并 ∪"是等号：R₁(R₂∪R₃) = R₁R₂ ∪ R₁R₃</div>
  <svg viewBox="0 0 900 260" style="width:100%;height:auto;display:block;">
    <defs>
      <marker id="bb" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#4F6B9A"/></marker>
      <marker id="bg" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#35705A"/></marker>
      <marker id="bd" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#1A1B1C"/></marker>
    </defs>
    <!-- 分步 -->
    <line x1="113" y1="133" x2="257" y2="87" stroke="#4F6B9A" stroke-width="2.2" marker-end="url(#bb)"/>
    <line x1="113" y1="147" x2="257" y2="193" stroke="#4F6B9A" stroke-width="2.2" marker-end="url(#bb)"/>
    <line x1="303" y1="88" x2="418" y2="132" stroke="#35705A" stroke-width="2.2" marker-end="url(#bg)"/>
    <line x1="303" y1="192" x2="418" y2="148" stroke="#35705A" stroke-width="2.2" marker-end="url(#bg)"/>
    <text x="178" y="128" text-anchor="middle" font-size="13" fill="#4F6B9A" font-weight="600">R₁</text>
    <text x="362" y="122" text-anchor="middle" font-size="13" fill="#35705A" font-weight="600">R₂∪R₃</text>
    <text x="262" y="40" text-anchor="middle" font-size="13" fill="#5F6670">经 b₂ 或 b₃ 都行</text>
    <g font-size="15" font-weight="600">
      <circle cx="90" cy="140" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <circle cx="280" cy="80" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <circle cx="280" cy="200" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <circle cx="440" cy="140" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <text x="90" y="146" text-anchor="middle">a</text>
      <text x="280" y="86" text-anchor="middle">b₂</text>
      <text x="280" y="206" text-anchor="middle">b₃</text>
      <text x="440" y="146" text-anchor="middle">c</text>
    </g>
    <text x="508" y="152" text-anchor="middle" font-size="38" fill="#1A1B1C" font-weight="700">=</text>
    <!-- 净结果 -->
    <line x1="614" y1="140" x2="786" y2="140" stroke="#1A1B1C" stroke-width="2.6" marker-end="url(#bd)"/>
    <g font-size="15" font-weight="600">
      <circle cx="590" cy="140" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <circle cx="810" cy="140" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <text x="590" y="146" text-anchor="middle">a</text>
      <text x="810" y="146" text-anchor="middle">c</text>
    </g>
    <text x="700" y="195" text-anchor="middle" font-size="13" fill="#5F6670">复合结果：a→c</text>
  </svg>
  <p style="font-size:14px;line-height:1.6;color:#35705A;margin:2px 0 0;">
    "走 R₂ <b>或</b>走 R₃ 能到 c" 与 "结果里属于 R₁R₂ <b>或</b>属于 R₁R₃" 完全对应，所以是等号。
  </p>

  <!-- 图3：交 → 只有包含 -->
  <div style="font-size:15px;font-weight:600;margin:22px 0 4px;">③ 对"交 ∩"只有包含：R₁(R₂∩R₃) ⊊ R₁R₂ ∩ R₁R₃（反例）</div>
  <svg viewBox="0 0 980 280" style="width:100%;height:auto;display:block;">
    <defs>
      <marker id="cb" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#4F6B9A"/></marker>
      <marker id="cg" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#35705A"/></marker>
      <marker id="co" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#9A6A2F"/></marker>
      <marker id="cd" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#1A1B1C"/></marker>
    </defs>
    <!-- 分步 -->
    <line x1="102" y1="141" x2="228" y2="94" stroke="#4F6B9A" stroke-width="2.2" marker-end="url(#cb)"/>
    <line x1="102" y1="159" x2="228" y2="206" stroke="#4F6B9A" stroke-width="2.2" marker-end="url(#cb)"/>
    <line x1="272" y1="94" x2="388" y2="141" stroke="#35705A" stroke-width="2.2" marker-end="url(#cg)"/>
    <line x1="272" y1="206" x2="388" y2="159" stroke="#9A6A2F" stroke-width="2.2" marker-end="url(#co)"/>
    <text x="160" y="140" text-anchor="middle" font-size="13" fill="#4F6B9A" font-weight="600">R₁</text>
    <text x="330" y="106" text-anchor="middle" font-size="13" fill="#35705A" font-weight="600">R₂</text>
    <text x="330" y="214" text-anchor="middle" font-size="13" fill="#9A6A2F" font-weight="600">R₃</text>
    <text x="245" y="40" text-anchor="middle" font-size="13" fill="#A14E50" font-weight="600">R₂ 只走 b₂、R₃ 只走 b₃，没有同一中转同时满足 → R₂∩R₃=∅</text>
    <g font-size="15" font-weight="600">
      <circle cx="80" cy="150" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <circle cx="250" cy="85" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <circle cx="250" cy="215" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <circle cx="410" cy="150" r="24" fill="#fff" stroke="#1A1B1C" stroke-width="1.6"/>
      <text x="80" y="156" text-anchor="middle">a</text>
      <text x="250" y="91" text-anchor="middle">b₂</text>
      <text x="250" y="221" text-anchor="middle">b₃</text>
      <text x="410" y="156" text-anchor="middle">c</text>
    </g>
    <!-- 左式结果：空 -->
    <g font-size="15" font-weight="600">
      <circle cx="525" cy="150" r="22" fill="#fff" stroke="#5F6670" stroke-width="1.4"/>
      <circle cx="625" cy="150" r="22" fill="#fff" stroke="#5F6670" stroke-width="1.4"/>
      <text x="525" y="156" text-anchor="middle">a</text>
      <text x="625" y="156" text-anchor="middle">c</text>
    </g>
    <text x="575" y="205" text-anchor="middle" font-size="13" fill="#A14E50" font-weight="600">R₁(R₂∩R₃)=∅</text>
    <text x="668" y="158" text-anchor="middle" font-size="30" fill="#1A1B1C" font-weight="700">⊊</text>
    <!-- 右式结果：有 a→c -->
    <line x1="746" y1="150" x2="838" y2="150" stroke="#1A1B1C" stroke-width="2.6" marker-end="url(#cd)"/>
    <g font-size="15" font-weight="600">
      <circle cx="722" cy="150" r="22" fill="#fff" stroke="#1A1B1C" stroke-width="1.4"/>
      <circle cx="862" cy="150" r="22" fill="#fff" stroke="#1A1B1C" stroke-width="1.4"/>
      <text x="722" y="156" text-anchor="middle">a</text>
      <text x="862" y="156" text-anchor="middle">c</text>
    </g>
    <text x="792" y="205" text-anchor="middle" font-size="13" fill="#35705A" font-weight="600">R₁R₂∩R₁R₃ = {a→c}</text>
  </svg>
  <p style="font-size:14px;line-height:1.6;color:#A14E50;margin:2px 0 0;">
    右边允许"走 R₂ 时经 b₂、走 R₃ 时经 b₃"——<b>两个不同的中转点</b>；左边却要求<b>同一个中转</b>同时在 R₂ 和 R₃ 中。
    所以右边更松：左边能推出右边（⊆），但此例中 ∅ ⊊ {a→c}，等号不成立。
  </p>

  <div style="margin-top:22px;padding:12px 14px;background:#F7F7F5;border-radius:8px;font-size:14px;line-height:1.6;">
    <b>一句话记忆：</b>复合 = 走两步；对<b>并</b>，"或"的中转可以自然合并 → <b>等号</b>；
    对<b>交</b>，右边的中转能"分裂"成两个点 → 只有 <b>包含 ⊆</b>。第⑤条结合律 (R₁R₂)R₄=R₁(R₂R₄) 则说明"先走哪两步先合并"不影响最终结果。
  </div>

</div>
</html>
