$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$base = 'C:\Users\29469\Desktop\' + [char]0x5927 + [char]0x4E00 + [char]0x4E0B + [char]0x8BA1 + [char]0x7B97 + [char]0x673A + [char]0x79D1 + [char]0x5B66 + [char]0x5BFC + [char]0x8BBA + '\' + [char]0x8BFE + [char]0x4EF6 + '-CSAPP3e\'
$src = $base + '21-netprog1_' + [char]0x4E2D + [char]0x6587 + '.pptx'
$outDir = 'D:\29469\Documents\notes\.workbuddy\tmp\netpages'

$SCALE = 3
# manual crop boxes in slide coordinates: L, T, R, B
$manual = @{
    3  = @(76, 78, 660, 524)
    5  = @(210, 106, 468, 242)
    27 = @(47, 236, 702, 525)
    32 = @(6, 215, 711, 515)
    47 = @(108, 138, 667, 310)
    50 = @(108, 102, 667, 291)
}

$app = New-Object -ComObject PowerPoint.Application
$pres = $app.Presentations.Open($src, $true, $false, $false)
$W = $pres.PageSetup.SlideWidth
$H = $pres.PageSetup.SlideHeight

foreach ($i in (@(27))) {
    $b = $manual[$i]
    $s = $pres.Slides.Item($i)
    $full = Join-Path $outDir ("full_{0:D2}.png" -f $i)
    if (-not (Test-Path $full)) {
        $s.Export($full, "PNG", [int]($W * $SCALE), [int]($H * $SCALE)) | Out-Null
    }
    $x1 = [int]($b[0] * $SCALE); $y1 = [int]($b[1] * $SCALE)
    $cw = [int](($b[2] - $b[0]) * $SCALE); $ch = [int](($b[3] - $b[1]) * $SCALE)
    $crop = Join-Path $outDir ("crop_{0:D2}.png" -f $i)
    $bmp = [System.Drawing.Image]::FromFile($full)
    $rect = New-Object System.Drawing.Rectangle($x1, $y1, $cw, $ch)
    $dst = New-Object System.Drawing.Bitmap($cw, $ch)
    $g = [System.Drawing.Graphics]::FromImage($dst)
    $g.DrawImage($bmp, (New-Object System.Drawing.Rectangle(0,0,$cw,$ch)), $rect, [System.Drawing.GraphicsUnit]::Pixel)
    $g.Dispose()
    $dst.Save($crop, [System.Drawing.Imaging.ImageFormat]::Png)
    $dst.Dispose(); $bmp.Dispose()
    Write-Output ("slide {0}: {1}x{2}" -f $i, $cw, $ch)
}

$pres.Close()
$app.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($pres) | Out-Null
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($app) | Out-Null
Write-Output "done"
