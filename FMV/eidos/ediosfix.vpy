# export PYTHONPATH="${PYTHONPATH}:/home/chris/Programs/vspythonscripts"
# vspipe -c y4m ediosfix.vpy - | x264 --demuxer y4m - --preset slower -v --crf 17 --input-range pc --range pc --input-depth 10 --output-depth 10 --output ediosfix.mkv

import vapoursynth as vs
core = vs.core
import vs_transitions

video = core.bs.VideoSource('/home/chris/Data/Games/FF7/Mods/fixedios/EIDOS TEST 1.avi')

video = core.fmtc.bitdepth(video, bits=16, fulls=False, fulld=True)
video = core.std.SetFrameProp(video, prop='_ColorRange', intval=0) # 0 means full range
video = core.fmtc.resample(video,css='444', fulls=True, fulld=True)

#video = core.hist.Classic(video)
# 10/7, same as PSX videos and SYW videos
# No crash
#video = core.resize.Spline36(video, width=1280, height=896)

# Just cropping to 1600x1120 crashes
#video = core.std.Crop(video, 0, 0, 40, 40)

# Scale to 1280x960
# doesn't crash
video = core.resize.Spline36(video, width=1280, height=960)

# Scale to 1280x960, then crop to 1280x896
# doesn't crash
# Should match the aspect ratio of FFNx scissors
#video = core.resize.Spline36(video, width=1280, height=960)
#video = core.std.Crop(video, 0, 0, 32, 32)

video = core.std.AssumeFPS(video, fpsnum=30, fpsden=1)

whiteframe = core.std.Trim(video, first=297)
# 30 for 328 frames
# 36 for 334 frames
# 6 for 304 frames
whiteframe = core.std.Loop(whiteframe, 6)
blackframe = core.std.BlankClip(whiteframe)
transition = vs_transitions.fade(whiteframe, blackframe)


video = video + transition

video = core.fmtc.resample(video,css='420', fulls=True, fulld=True)
video = core.fmtc.bitdepth(video, bits=10, fulls=True, fulld=True)

video.set_output()