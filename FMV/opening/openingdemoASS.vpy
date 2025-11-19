# export PYTHONPATH="${PYTHONPATH}:/home/chris/Programs/vspythonscripts"
# vspipe -c y4m openingdemoASS.vpy - | x264 --demuxer y4m - --preset slower -v --crf 17 --input-range pc --range pc --input-depth 10 --output-depth 10 --output openingdemo_onSYW.mkv

import vapoursynth as vs
core = vs.core
import kagefunc
import vs_transitions
import edi_rpow2

# read in all sources
unsub = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/openingbeta1/OPENING.mkv')
#subbed = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/openingbeta1/openingdemo.mp4')

# histogram for checking levels
#video = core.hist.Classic(video)

# get all clips into full range 444 16-bit
unsub = core.fmtc.bitdepth(unsub, bits=16, fulls=False, fulld=True)
unsub = core.std.SetFrameProp(unsub, prop='_ColorRange', intval=0) # 0 means full range
unsub = core.fmtc.resample(unsub,css='444', fulls=True, fulld=True)

#subbed = core.fmtc.bitdepth(subbed, bits=16, fulls=False, fulld=True)
#subbed = core.std.SetFrameProp(subbed, prop='_ColorRange', intval=0) # 0 means full range
#subbed = core.fmtc.resample(subbed,css='444', fulls=True, fulld=True)

# need range=1 for fullrange clip see https://github.com/vapoursynth/subtext/issues/15
video = core.sub.TextFile(unsub, file="/home/chris/Data/Games/FF7/Mods/NewWork/openingbeta1/demoadjustfastfinal.ass", blend=True, range=1, scale=1, margins=[0,16,0,0])

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
