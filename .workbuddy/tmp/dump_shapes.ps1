$ErrorActionPreference = 'Stop'
$src = 'C:\Users\29469\Desktop\' + [char]0x5927 + [char]0x4E00 + [char]0x4E0B + [char]0x8BA1 + [char]0x7B97 + [char]0x673A + [char]0x79D1 + [char]0x5B66 + [char]0x5BFC + [char]0x8BBA + '\' + [char]0x8BFE + [char]0x4EF6 + '-CSAPP3e\21-netprog1_' + [char]0x4E2D + [char]0x6587 + '.pptx'
$out = 'D:\29469\Documents\notes\.workbuddy\tmp\shapes21.txt'

$app = New-Object -ComObject PowerPoint.Application
$pres = $app.Presentations.Open($src, $true, $false, $false)

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("Slides=$($pres.Slides.Count) PageW=$($pres.PageSetup.SlideWidth) PageH=$($pres.PageSetup.SlideHeight)")

foreach ($s in $pres.Slides) {
    $idx = $s.SlideIndex
    $shapes = $s.Shapes
    $lines.Add("=== slide $idx  shapes=$($shapes.Count) ===")
    foreach ($sh in $shapes) {
        $t = ''
        try { if ($sh.HasTextFrame -eq -1 -and $sh.TextFrame.HasText -eq -1) { $t = $sh.TextFrame.TextRange.Text -replace "`r", ' / ' } } catch {}
        $t = $t.Trim()
        if ($t.Length -gt 40) { $t = $t.Substring(0, 40) + '...' }
        $line = "  [" + $sh.Id + "] type=" + $sh.Type + " name='" + $sh.Name + "' L=" + [math]::Round($sh.Left) + " T=" + [math]::Round($sh.Top) + " W=" + [math]::Round($sh.Width) + " H=" + [math]::Round($sh.Height) + " :: " + $t
        $lines.Add($line)
    }
}

$pres.Close()
$app.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($pres) | Out-Null
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($app) | Out-Null
[System.IO.File]::WriteAllLines($out, $lines, (New-Object System.Text.UTF8Encoding $false))
Write-Output "written $($lines.Count) lines -> $out"
