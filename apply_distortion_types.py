# start audacity from within the folder of this script before!
import pyaudacity as pa

# put the name of your audio file in this folder:
input_mp3 = "sultans_of_swing.mp3"
basename = input_mp3.replace(".mp3", "")

# see here which parameters exist:
# https://manual.audacityteam.org/man/scripting_reference.html
distortion_types = [
    "Hard Clipping",
    "Soft Clipping",
    "Soft Overdrive",
    "Medium Overdrive",
    # "Hard Overdrive",
    "Cubic Curve (odd harmonics)",
    # "Even Harmonics", 
    # "Expand and Compress",
    "Leveller",
    # "Rectifier Distortion",
    "Hard Limiter 1413",
]
for s in distortion_types:
    pa.do('Import2: Filename="' + input_mp3 + '"')
    pa.do('SelectTime: Start="54.5" End="100"')
    pa.do('Delete')
    pa.do('SelectTime: Start="0" End="2.6"')
    pa.do('Delete')
    pa.do('SelectTracks')
    pa.do('SelectAll')
    pa.do('SelAllTracks')
    pa.do('Normalize')
    pa.do('Compressor: Threshold=-20')
    pa.do('Distortion: Threshold=-40 Type="' + s + '"')
    pa.do('Export2: Filename="' + basename + '_pyaudacity_' + s + '.mp3"')
    pa.do('TrackClose')
