# export PYTHONPATH="${PYTHONPATH}:/home/chris/Programs/vspythonscripts"
# vspipe -c y4m endingsubs.vpy - | x264 --demuxer y4m - --preset slower -v --crf 17 --input-range pc --range pc --input-depth 10 --output-depth 10 --output Ending2_SACtranslation.mkv

import vapoursynth as vs
core = vs.core

video = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/NewWork/endingsubs/Ending2.mkv')
#video = core.ffms2.Source('/home/chris/Videos/AKATSUKI_NO_DASSOU/A1_t00.mkv')



# histogram for checking levels
# yeah, fuck, it's wrong -- gonna have to convert
video = core.fmtc.bitdepth(video, bits=16, fulls=False, fulld=True)
video = core.std.SetFrameProp(video, prop='_ColorRange', intval=0) # 0 means full range
#video = core.hist.Classic(video)

#resample to 4:4:4 so we may crop freely, at least while testing
video = core.fmtc.resample(video,css='444', fulls=True, fulld=True)

# tried debanding to fix the limited range a little better, but it artifacted
# so skip that

# chop off the existing subs by crop and border
video = core.std.Crop(video, bottom=128)
video = core.std.AddBorders(video, bottom=128)





# need range=1 for fullrange clip see https://github.com/vapoursynth/subtext/issues/15
video = core.sub.TextFile(video, file="/home/chris/Data/Games/FF7/Mods/NewWork/endingsubs/storyboard.ass", blend=True, range=1, scale=1, margins=[0,48,0,0])


# drop back down to YUV420P10 for encoding
# resample back to 420
video = core.fmtc.resample(video,css='420', fulls=True, fulld=True)
video = core.fmtc.bitdepth(video, bits=10, fulls=True, fulld=True)
video.set_output()