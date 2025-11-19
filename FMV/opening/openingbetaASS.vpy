# export PYTHONPATH="${PYTHONPATH}:/home/chris/Programs/vspythonscripts"
# vspipe -c y4m openingbetaASS.vpy - | x264 --demuxer y4m - --preset slower -v --crf 17 --input-range pc --range pc --input-depth 10 --output-depth 10 --output openingbeta_onSYW.mkv

import vapoursynth as vs
core = vs.core
import kagefunc
import vs_transitions
import edi_rpow2

# read in all sources
unsub = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/openingbeta1/OPENING.mkv')
#hardsubbed = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/openingbeta1/openingbeta.mkv')

# histogram for checking levels
#video = core.hist.Classic(video)

# get all clips into full range 444 16-bit
unsub = core.fmtc.bitdepth(unsub, bits=16, fulls=False, fulld=True)
unsub = core.std.SetFrameProp(unsub, prop='_ColorRange', intval=0) # 0 means full range
unsub = core.fmtc.resample(unsub,css='444', fulls=True, fulld=True)

#hardsubbed = core.fmtc.bitdepth(hardsubbed, bits=16, fulls=False, fulld=True)
#hardsubbed = core.std.SetFrameProp(hardsubbed, prop='_ColorRange', intval=0) # 0 means full range
#hardsubbed = core.fmtc.resample(hardsubbed,css='444', fulls=True, fulld=True)

# double the framerate on the hardsubbed clip
#hardsubbedfast = core.std.Interleave([hardsubbed, hardsubbed])

# need range=1 for fullrange clip see https://github.com/vapoursynth/subtext/issues/15
#video = core.sub.TextFile(hardsubbed, file="/home/chris/Data/Games/FF7/Mods/NewWork/openingbeta1/beta.ass", blend=True, range=1, scale=1, margins=[0,16,0,0])

softsub = core.sub.TextFile(unsub, file="/home/chris/Data/Games/FF7/Mods/NewWork/openingbeta1/beta.ass", blend=True, range=1, scale=1, margins=[0,16,0,0])

#video = core.std.StackHorizontal([softsub, hardsubbedfast])

blackclip = core.std.BlankClip(unsub)
whiteclip = core.std.BlankClip(unsub, color=[65535,32767,32767])

# full size is 1280x896

# line1 "The Shinra..." 35-52 core.std.Crop(video, 220, 220, 270, 560)
# line2 "next generation..." 53-87 core.std.Crop(video, 220, 220, 340, 470)
# line3 "The first..." 99-126 core.std.Crop(video, 220, 220, 566, 260)
# line4 "Similar power..." 127-150 core.std.Crop(video, 90, 90, 666, 172)

# line5 "Construction finishes... " 293-324 core.std.Crop(video, 88, 88, 246, 590)
# line6 "Shinra erects..." 325-348 core.std.Crop(video, 312, 312, 330, 508)
# line7 "Hostilities escalate..." 365-386 core.std.Crop(video, 196, 196, 576, 260)
# line8 "known as..." 387-408 core.std.Crop(video, 380, 380, 648, 176)

# line9 "The leader..." 549-585 core.std.Crop(video, 230, 230, 276, 556)

# line10 "The conflict..." 605-636 core.std.Crop(video, 30, 380, 556, 282)
# line11 "balances on..." 637-666 core.std.Crop(video, 506, 42, 640, 140)

# line12    "12/9"    837-883 core.std.Crop(video, 786, 96, 330, 350)

pre1mask = core.std.Trim(whiteclip, first=0, last=34)

# line1 "The Shinra..." 35-52 core.std.Crop(video, 220, 220, 270, 560)
black1 = core.std.Trim(blackclip, first=35, last=52)
black1 = core.std.Crop(black1, 220, 220, 270, 560)
white1 = core.std.Trim(whiteclip, first=35, last=52)
white1 = core.std.Crop(white1, 220, 220, 270, 560)
trans1 = vs_transitions.peel(black1, white1, direction="right")
trans1 = core.std.BoxBlur(trans1, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans1 = core.std.AddBorders(trans1, 220, 220, 270, 560, color=[65535,32767,32767])

# line2 "next generation..." 53-87 core.std.Crop(video, 220, 220, 340, 470)
black2 = core.std.Trim(blackclip, first=53, last=87)
black2 = core.std.Crop(black2, 220, 220, 340, 470)
white2 = core.std.Trim(whiteclip, first=53, last=87)
white2 = core.std.Crop(white2, 220, 220, 340, 470)
trans2 = vs_transitions.peel(black2, white2, direction="right")
trans2 = core.std.BoxBlur(trans2, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans2 = core.std.AddBorders(trans2, 220, 220, 340, 470, color=[65535,32767,32767])

gap2to3 = core.std.Trim(whiteclip, first=88, last=98)

# line3 "The first..." 99-126 core.std.Crop(video, 220, 220, 566, 260)
black3 = core.std.Trim(blackclip, first=99, last=126)
black3 = core.std.Crop(black3, 220, 220, 566, 260)
white3 = core.std.Trim(whiteclip, first=99, last=126)
white3 = core.std.Crop(white3, 220, 220, 566, 260)
trans3 = vs_transitions.peel(black3, white3, direction="right")
trans3 = core.std.BoxBlur(trans3, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans3 = core.std.AddBorders(trans3, 220, 220, 566, 260, color=[65535,32767,32767])

# line4 "Similar power..." 127-150 core.std.Crop(video, 90, 90, 666, 172)
black4 = core.std.Trim(blackclip, first=127, last=150)
black4 = core.std.Crop(black4, 90, 90, 666, 172)
white4 = core.std.Trim(whiteclip, first=127, last=150)
white4 = core.std.Crop(white4, 90, 90, 666, 172)
trans4 = vs_transitions.peel(black4, white4, direction="right")
trans4 = core.std.BoxBlur(trans4, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans4 = core.std.AddBorders(trans4, 90, 90, 666, 172, color=[65535,32767,32767])

gap4to5 = core.std.Trim(whiteclip, first=151, last=292)

# line5 "Construction finishes... " 293-324 core.std.Crop(video, 88, 88, 246, 590)
black5 = core.std.Trim(blackclip, first=293, last=324)
black5 = core.std.Crop(black5, 88, 88, 246, 590)
white5 = core.std.Trim(whiteclip, first=293, last=324)
white5 = core.std.Crop(white5, 88, 88, 246, 590)
trans5 = vs_transitions.peel(black5, white5, direction="right")
trans5 = core.std.BoxBlur(trans5, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans5 = core.std.AddBorders(trans5, 88, 88, 246, 590, color=[65535,32767,32767])

# line6 "Shinra erects..." 325-348 core.std.Crop(video, 312, 312, 330, 508)
black6 = core.std.Trim(blackclip, first=325, last=348)
black6 = core.std.Crop(black6, 312, 312, 330, 508)
white6 = core.std.Trim(whiteclip, first=325, last=348)
white6 = core.std.Crop(white6, 312, 312, 330, 508)
trans6 = vs_transitions.peel(black6, white6, direction="right")
trans6 = core.std.BoxBlur(trans6, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans6 = core.std.AddBorders(trans6, 312, 312, 330, 508, color=[65535,32767,32767])

gap6to7 = core.std.Trim(whiteclip, first=349, last=364)

# line7 "Hostilities escalate..." 365-386 core.std.Crop(video, 196, 196, 576, 260)
black7 = core.std.Trim(blackclip, first=365, last=386)
black7 = core.std.Crop(black7, 196, 196, 576, 260)
white7 = core.std.Trim(whiteclip, first=365, last=386)
white7 = core.std.Crop(white7, 196, 196, 576, 260)
trans7 = vs_transitions.peel(black7, white7, direction="right")
trans7 = core.std.BoxBlur(trans7, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans7 = core.std.AddBorders(trans7, 196, 196, 576, 260, color=[65535,32767,32767])

# line8 "known as..." 387-408 core.std.Crop(video, 380, 380, 648, 176)
black8 = core.std.Trim(blackclip, first=387, last=408)
black8 = core.std.Crop(black8, 380, 380, 648, 176)
white8 = core.std.Trim(whiteclip, first=387, last=408)
white8 = core.std.Crop(white8, 380, 380, 648, 176)
trans8 = vs_transitions.peel(black8, white8, direction="right")
trans8 = core.std.BoxBlur(trans8, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans8 = core.std.AddBorders(trans8, 380, 380, 648, 176, color=[65535,32767,32767])

gap8to9 = core.std.Trim(whiteclip, first=409, last=548)

# line9 "The leader..." 549-585 core.std.Crop(video, 230, 230, 276, 556)
black9 = core.std.Trim(blackclip, first=549, last=585)
black9 = core.std.Crop(black9, 230, 230, 276, 556)
white9 = core.std.Trim(whiteclip, first=549, last=585)
white9 = core.std.Crop(white9, 230, 230, 276, 556)
trans9 = vs_transitions.peel(black9, white9, direction="right")
trans9 = core.std.BoxBlur(trans9, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans9 = core.std.AddBorders(trans9, 230, 230, 276, 556, color=[65535,32767,32767])

gap9to10 = core.std.Trim(whiteclip, first=586, last=604)

# line10 "The conflict..." 605-636 core.std.Crop(video, 30, 380, 556, 282)
black10 = core.std.Trim(blackclip, first=605, last=636)
black10 = core.std.Crop(black10, 30, 380, 556, 282)
white10 = core.std.Trim(whiteclip, first=605, last=636)
white10 = core.std.Crop(white10, 30, 380, 556, 282)
trans10 = vs_transitions.peel(black10, white10, direction="right")
trans10 = core.std.BoxBlur(trans10, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans10 = core.std.AddBorders(trans10, 30, 380, 556, 282, color=[65535,32767,32767])

# line11 "balances on..." 637-666 core.std.Crop(video, 506, 42, 640, 140)
black11 = core.std.Trim(blackclip, first=637, last=666)
black11 = core.std.Crop(black11, 506, 42, 640, 140)
white11 = core.std.Trim(whiteclip, first=637, last=666)
white11 = core.std.Crop(white11, 506, 42, 640, 140)
trans11 = vs_transitions.peel(black11, white11, direction="right")
trans11 = core.std.BoxBlur(trans11, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans11 = core.std.AddBorders(trans11, 506, 42, 640, 140, color=[65535,32767,32767])

gap11to12 = core.std.Trim(whiteclip, first=667, last=836)

# line12    "12/9"    837-883 core.std.Crop(video, 786, 96, 330, 350)
black12 = core.std.Trim(blackclip, first=837, last=883)
black12 = core.std.Crop(black12, 786, 96, 330, 350)
white12 = core.std.Trim(whiteclip, first=837, last=883)
white12 = core.std.Crop(white12, 786, 96, 330, 350)
trans12 = vs_transitions.peel(black12, white12, direction="right")
trans12 = core.std.BoxBlur(trans12, planes=0, hradius=16, vradius=0, hpasses=8, vpasses=0)
trans12 = core.std.AddBorders(trans12, 786, 96, 330, 350, color=[65535,32767,32767])

postmask = core.std.Trim(whiteclip, first=884)

fullmask = pre1mask + trans1 + trans2 + gap2to3 + trans3 + trans4 + gap4to5 + trans5 + trans6 + gap6to7 + trans7 + trans8 + gap8to9 + trans9 + gap9to10 + trans10 + trans11 + gap11to12 + trans12 + postmask
video = core.std.MaskedMerge(unsub, softsub, fullmask)


#video = softsub
#video = core.std.Crop(video, 786, 96, 330, 350)


# HelveticaNeueLTStd-BdCn
# HelveticaNeueLTStd-Cn

# decimate for 15fps
#video = core.std.SelectEvery(video, cycle=2, offsets=0)
# OK, now we have frame issues...
# our video has 1792 frames
# original pc video has only 1791 frames
# old cmh video had 1793 frames (and apparently worked)
# beta video has only 1790 frames
# all except beta video lock background on frame 1760
# SWY's audio length is 1792.155 15-fps frames
# for now, we'll assume it will sync OK, and revist later if it does not.
#pc = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/openingbeta1/openingpc.avi')
#video = pc
#cmh = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/openingbeta1/openingcmh.mp4')
#video = cmh
#video = subbed

# drop back down to YUV420P10 for encoding
# resample back to 420
video = core.fmtc.resample(video,css='420', fulls=True, fulld=True)
video = core.fmtc.bitdepth(video, bits=10, fulls=True, fulld=True)
video.set_output()
