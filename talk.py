from subprocess import getoutput
import sys


arg = sys.argv
content = arg[1]
speed = arg[2]
getoutput('echo "' + content + '" | open_jtalk -x /var/lib/mecab/dic/open-jtalk/naist-jdic -m /usr/share/hts-voice/mei/mei_normal.htsvoice -ow /dev/stdout -fm -5 -r ' + speed + ' | aplay')
