# export PYTHONPATH="${PYTHONPATH}:/home/chris/Programs/vspythonscripts"
# vspipe -c y4m jenovasubs_try3.vpy - | x264 --demuxer y4m - --preset slower -v --crf 17 --input-range pc --range pc --input-depth 10 --output-depth 10 --output Jenova_E_SACtranslation_try3.mkv

import vapoursynth as vs
core = vs.core
import kagefunc
import vs_transitions

# read in all sources
# As per SYW, the unsubbed clip is slightly lower quality than the others
unsub = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/jenovasubs/jenova.e.unsubcolorsok.mov')
english = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/jenovasubs/JENOVA_E_english.mkv')
french = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/jenovasubs/JENOVA_E_french.mkv')
german = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/jenovasubs/JENOVA_E_german.mkv')
spanish = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/jenovasubs/JENOVA_E_spanish.mkv')

# histogram for checking levels
#video = core.hist.Classic(video)

# the unsubbed clip is 60 fps, cut to 30
unsub = core.std.SelectEvery(unsub, cycle=2, offsets=0)

# get all clips into full range 444 16-bit
unsub = core.fmtc.bitdepth(unsub, bits=16, fulls=False, fulld=True)
unsub = core.std.SetFrameProp(unsub, prop='_ColorRange', intval=0) # 0 means full range
unsub = core.fmtc.resample(unsub,css='444', fulls=True, fulld=True)
# the unsubbed video needs cropped
unsub = core.std.Crop(unsub, 86, 74, 28, 36) 

english = core.fmtc.bitdepth(english, bits=16, fulls=False, fulld=True)
english = core.std.SetFrameProp(english, prop='_ColorRange', intval=0) # 0 means full range
english = core.fmtc.resample(english,css='444', fulls=True, fulld=True)

french = core.fmtc.bitdepth(french, bits=16, fulls=False, fulld=True)
french = core.std.SetFrameProp(french, prop='_ColorRange', intval=0) # 0 means full range
french = core.fmtc.resample(french,css='444', fulls=True, fulld=True)

german = core.fmtc.bitdepth(german, bits=16, fulls=False, fulld=True)
german = core.std.SetFrameProp(german, prop='_ColorRange', intval=0) # 0 means full range
german = core.fmtc.resample(german,css='444', fulls=True, fulld=True)

spanish = core.fmtc.bitdepth(spanish, bits=16, fulls=False, fulld=True)
spanish = core.std.SetFrameProp(spanish, prop='_ColorRange', intval=0) # 0 means full range
spanish = core.fmtc.resample(spanish,css='444', fulls=True, fulld=True)

# make some masks
mask_e = kagefunc.hardsubmask_fades(english, unsub, expand_n=3)
mask_f = kagefunc.hardsubmask_fades(french, unsub, expand_n=3)
mask_g = kagefunc.hardsubmask_fades(german, unsub, expand_n=3)
mask_s = kagefunc.hardsubmask_fades(spanish, unsub, expand_n=3)

# fill in the subs in spanish with the lower-quality unsubbed version
filler = core.std.MaskedMerge(spanish, unsub, mask_s)
# fill in the gaps in the german with the filler so far
filler = core.std.MaskedMerge(german, filler, mask_g)
# fill in the gaps in the french with the filler so far
filler = core.std.MaskedMerge(french, filler, mask_f)
# finally, fill in the gaps in the english with the filler
video = core.std.MaskedMerge(english, filler, mask_e)

# To speed up processing, we can just copy frames 537+ from english
frontpart = core.std.Trim(video, first=0, last=536)
backpart = core.std.Trim(english, first=537)
goodunsub = core.std.Splice([frontpart, backpart])

# need range=1 for fullrange clip see https://github.com/vapoursynth/subtext/issues/15
video = core.sub.TextFile(goodunsub, file="/home/chris/Data/Games/FF7/Mods/NewWork/jenovasubs/jenova_e_sac_resync_pc_animate.ass", blend=True, range=1, scale=1, margins=[0,16,0,0])

# drop to 15fps as requested for SAC's copy
#video = core.std.SelectEvery(video, cycle=2, offsets=0)

# drop back down to YUV420P10 for encoding
# resample back to 420
video = core.fmtc.resample(video,css='420', fulls=True, fulld=True)
video = core.fmtc.bitdepth(video, bits=10, fulls=True, fulld=True)
video.set_output()
