$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$base = 'C:\Users\29469\Desktop\' + [char]0x5927 + [char]0x4E00 + [char]0x4E0B + [char]0x8BA1 + [char]0x7B97 + [char]0x673A + [char]0x79D1 + [char]0x5B66 + [char]0x5BFC + [char]0x8BBA + '\' + [char]0x8BFE + [char]0x4EF6 + '-CSAPP3e\'
$src = $base + '21-netprog1_' + [char]0x4E2D + [char]0x6587 + '.pptx'
$outDir = 'D:\29469\Documents\notes\.workbuddy\tmp\netpages'
if (Test-Path $outDir) { Remove-Item $outDir -Recurse -Force }
New-Item -ItemType Directory -Path $outDir | Out-Null

$SCALE = 3
$PAD = 8
$targets = @(2,3,5,6,7,8,9,12,15,20,27,28,32,33,34,37,46,47,50)

$app = New-Object -ComObject PowerPoint.Application
$pres = $app.Presentations.Open($src, $true, $false, $false)
$W = $pres.PageSetup.SlideWidth
$H = $pres.PageSetup.SlideHeight
$meta = New-Object System.Collections.Generic.List[string]

foreach ($i in $targets) {
    $s = $pres.Slides.Item($i)
    $minL = 1e9; $minT = 1e9; $maxR = -1e9; $maxB = -1e9
    foreach ($sh in $s.Shapes) {
        if ($sh.Type -eq 14) { continue }
        if ($sh.Left -lt $minL) { $minL = $sh.Left }
        if ($sh.Top  -lt $minT) { $minT = $sh.Top }
        if (($sh.Left + $sh.Width)  -gt $maxR) { $maxR = $sh.Left + $sh.Width }
        if (($sh.Top  + $sh.Height) -gt $maxB) { $maxB = $sh.Top  + $sh.Height }
    }
    if ($maxR -lt 0) { continue }

    $full = Join-Path $outDir ("full_{0:D2}.png" -f $i)
    $s.Export($full, "PNG", [int]($W * $SCALE), [int]($H * $SCALE)) | Out-Null

    $x1 = [int]([math]::Max(0, ($minL - $PAD) * $SCALE))
    $y1 = [int]([math]::Max(0, ($minT - $PAD) * $SCALE))
    $x2 = [int]([math]::Min($W * $SCALE, ($maxR + $PAD) * $SCALE))
    $y2 = [int]([math]::Min($H * $SCALE, ($maxB + $PAD) * $SCALE))
    $cw = $x2 - $x1
    $ch = $y2 - $y1

    $crop = Join-Path $outDir ("crop_{0:D2}.png" -f $i)
    $bmp = [System.Drawing.Image]::FromFile($full)
    $rect = New-Object System.Drawing.Rectangle($x1, $y1, $cw, $ch)
    $dst = New-Object System.Drawing.Bitmap($cw, $ch)
    $g = [System.Drawing.Graphics]::FromImage($dst)
    $g.DrawImage($bmp, (New-Object System.Drawing.Rectangle(0,0,$cw,$ch)), $rect, [System.Drawing.GraphicsUnit]::Pixel)
    $g.Dispose()
    $dst.Save($crop, [System.Drawing.Imaging.ImageFormat]::Png)
    $dst.Dispose()
    $bmp.Dispose()

    $meta.Add(("slide {0}: crop {1}x{2} from {3},{4} shapeBox L={5:N0} T={6:N0} R={7:N0} B={8:N0}" -f $i, $cw, $ch, $x1, $y1, $minL, $minT, $maxR, $maxB))
}

$pres.Close()
$app.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($pres) | Out-Null
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($app) | Out-Null
[System.IO.File]::WriteAllLines((Join-Path $outDir 'meta.txt'), $meta, (New-Object System.Text.UTF8Encoding $false))
Write-Output "done $($meta.Count) pages -> $outDir"
