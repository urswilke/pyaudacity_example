# start audacity from within the folder of this script before!
import pyaudacity as pa

for s in ["Hard Clipping", "Soft Clipping", "Soft Overdrive", "Medium Overdrive", "Hard Overdrive", "Cubic Curve (odd harmonics)", "Even Harmonics", "Expand and Compress", "Leveller", "Rectifier Distortion", "Hard Limiter 1413"]:
    pa.do('Import2: Filename="sultans_of_swing.mp3"')
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
    pa.do('Export2: Filename="sultans_of_swing_pyaudacity_' + s + '.mp3"')
    pa.do('TrackClose')
