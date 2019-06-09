# -*- coding: utf8 -*-


import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from tkinter import PhotoImage
import subprocess
from subprocess import getoutput
import time
import random
import urllib.request
import re
import os


nameOfThisSoftware = 'ORIZIN　AIアシスタント'
dictionary = ''
index = 0
notAdjustedQuestion = ''
response = ''
knownQuestion = False


def where_am_i():
    global thisDir
    thisDir = os.path.abspath(os.path.dirname(__file__))


def read_dictionary():
    f = open(thisDir + '/response.txt', encoding='utf-8_sig')
    global dictionary
    global index
    dictionary_file = f.read()
    index = dictionary_file.count('\n') + 1
    if index != dictionary_file.count(':'):
        bigger_num = 0
        if index > dictionary_file.count(':'):
            bigger_num = index
        else:
            bigger_num = dictionary_file.count(':')
        dictionary_checker = dictionary_file
        bad_point = ''
        for num in range(bigger_num):
            if dictionary_checker[0:dictionary_checker.find('\n')].count(':') != 1:
                bad_point += '\n"' + dictionary_checker[0:dictionary_checker.find('\n')] + '"(' + str(num + 1) + '行目)'
            dictionary_checker = dictionary_checker[dictionary_checker.find('\n') + 1:]
        tk.messagebox.showinfo(nameOfThisSoftware, '辞書ファイルの単語リストの数(' + str(index) + '個）と応答の数(' + str(dictionary_file.count(':')) + '個）が一致しません。\n' + '問題のある箇所:' + bad_point)
    dictionary = dictionary_file
    f.close()


def worker():
    global notAdjustedQuestion
    notAdjustedQuestion = requestBox.get()
    question = adjust_question(notAdjustedQuestion)
    if judge(question, ['catlife', 'キャットライフ']):
        speak('私の好きな曲は、キャットライフです。キャットライフを再生します。', '私の好きな曲は、Cat lifeです。Cat lifeを再生します。')
        play_sound(thisDir + '/sounds/musics/wav/catLife.wav')
    elif judge(question, ['曲', '音楽', '楽曲', '歌', '唄', 'うた', 'ミュージック', 'music']):
        if random.randint(0, 1) == 0:
            speak('私の好きな曲は、キャットライフです。キャットライフを再生します。', '私の好きな曲は、Cat lifeです。Cat lifeを再生します。')
            play_sound(thisDir + '/sounds/musics/wav/catLife.wav')
        else:
            speak('私の好きな曲は、せんじんです。せんじんを再生します。', '私の好きな曲は、戦神です。戦神を再生します。')
            play_sound(thisDir + '/sounds/musics/wav/senjin.wav')
    elif judge(question, ['昔話', '昔噺', 'むかしばなし', 'むかし話', 'むかし噺', '昔ばなし']):
        speak('昔話ですか。では一つ、お聞かせします。')
        resultBox.insert('end', open(thisDir + '/sounds/musics/wav/mukashibanashi.txt', encoding='utf-8_sig').read())
        play_sound(thisDir + '/sounds/musics/wav/mukashibanashi.wav')
    elif judge(question, ['じゃんけん', 'ジャンケン']):
        randomInt = random.randint(0, 2)
        if randomInt == 0:
            speak('ジャンケンですか。良いですね。やりましょう。それではいきますよ。ジャン　ケン　ポン。私はグーです。')
        elif randomInt == 1:
            speak('ジャンケンですか。良いですね。やりましょう。それではいきますよ。ジャン　ケン　ポン。私はチョキです。')
        else:
            speak('ジャンケンですか。良いですね。やりましょう。それではいきますよ。ジャン　ケン　ポン。私はパーです。')
    elif judge(question, ['ニュース', 'news']):
        speak('最新のニュースを3件、日本テレビのウェブサイトより取得します。')
        newsTitle, newsContent = get_news(3)
        for num in range(3):
            if num != 0:
                speak('次のニュースです。', '', prompt=False)
            speak(newsTitle[num], '[' + newsTitle[num] + ']', prompt=False)
            speak(newsContent[num], prompt=False)
            time.sleep(3)
        speak('以上、ニュースをお伝えしました。', prompt=False)
    elif judge(question, ['早口言葉', '早口ことば', 'はやくち言葉', 'はやくちことば']):
        speak('早口言葉を言いますね。')
        speak('生ごみ生米生卵。赤巻紙青巻紙黄巻紙。東京特許許可局。', prompt=False, speed=1.5)
        speak('もう一度。', prompt=False)
        speak('生ごみ生米生卵。赤巻紙青巻紙黄巻紙。東京特許許可局。', prompt=False, speed=2)
    elif judge(question, ['イースターエッグ', 'ゲーム', '宇宙船', '宇宙戦艦', 'spacebattleship', 'game', 'easteregg']):
        subprocess.Popen(['python3', thisDir + '/easter_egg.py'])
    elif judge(question, ['orizin', 'origin', 'オリジン', 'ロゴ', 'イメージ', 'アスキーアート', 'aa']):
        resultBox.insert('end', open(thisDir + '/ORIZIN_Agent_AA.txt', encoding='utf-8_sig').read())
    else:
        searchresponse(question)


def worker_from_shortcut(event):
    worker()


def searchresponse(request):
    global response
    global knownQuestion
    knownQuestion = False
    candidate_for_dictionary = re.split('[\n:]', dictionary)[::2]
    candidate_for_response = re.split('[\n:]', dictionary)[1::2]
    for num in range(index):
        if judge(request, candidate_for_dictionary[num].split('/')):
            response_and_insert_content = candidate_for_response[num].split('/')
            speak(response_and_insert_content[0], response_and_insert_content[candidate_for_response[num].count('/')])
            knownQuestion = True
            break
    if knownQuestion == False:
        f = open(thisDir + '/unknownQuestions.txt', 'a', encoding='utf-8_sig')
        f.write(request + '\n')
        f.close()
        speak('そうですか。')


def speak(content, insert_content='no arg', *, request='no arg', prompt=True, speed=1.0):
    global response
    response = content
    subprocess.Popen(['python3', thisDir + '/talk.py', content, str(speed)])
    # getoutput('echo "' + content + '" | open_jtalk -x /var/lib/mecab/dic/open-jtalk/naist-jdic -m /usr/share/hts-voice/mei/mei_normal.htsvoice -ow /dev/stdout -fm -5 -r ' + str(speed) + ' | aplay')
    if insert_content == 'no arg':
        insert_content = content
    prompt_mark = '\n\n>>>'
    request_sentence = notAdjustedQuestion
    if prompt == False:
        prompt_mark = ''
        request_sentence = ''
    resultBox.insert('end', prompt_mark + request_sentence + '\n' + insert_content)


def play_sound(sound_file):
    command = 'aplay ' + sound_file
    global soundPlayer
    soundPlayer = subprocess.Popen(command.split())


def stop_sound():
    soundPlayer.terminate()


def fullpitch_to_highpitch(sentence):
    return sentence.translate(str.maketrans('ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))


def remove_unnecessary(sentence):
    return sentence.translate(str.maketrans({' ': None, '　': None, '・': None, '_': None}))


def adjust_question(sentence):
    return remove_unnecessary(fullpitch_to_highpitch(sentence.lower()))


def judge(character, array):
    for num in range(len(array)):
        if array[num] in character:
            return True
    return False


def get_news(num_of_item):
    url = 'http://www.news24.jp/rss/index.rdf'
    rss_file = urllib.request.urlopen(url).read().decode('shift_jis')
    news = rss_file[rss_file.find('</channel>'):]
    news = news[news.find('<title>') + 7:]
    summary = []
    details = []
    for num in range(num_of_item):
        news = news[news.find('<title>') + 7:]
        summary.append(news[:news.find('</title>') - 12])
        details.append(news[news.find('<description>') + 13:news.find('</description>')])
        news = news[news.find('</description>'):]
    return summary, details


def shutdown():
    quit()


def shutdown_from_shortcut(event):
    shutdown()


def reset():
    resultBox.delete('1.0', 'end')


def reset_from_shortcut(event):
    reset()


where_am_i()
read_dictionary()

root = tk.Tk()
root.title(nameOfThisSoftware)
root.geometry("800x450")
icon = [PhotoImage(file=thisDir + '/ORIZIN_Agent_Oのみ_透明.png')]
root.wm_iconphoto(True, *icon)

root.bind('<Control-q>', shutdown_from_shortcut)
root.bind('<Control-Delete>', reset_from_shortcut)
root.bind('<Return>', worker_from_shortcut)

mainFrame = tk.Frame(root, height=300)
mainFrame.pack(anchor=tk.NW, expand=1, fill=tk.BOTH)

controllerFrame = tk.Frame(mainFrame, height=100)
controllerFrame.pack(anchor=tk.NW, pady=5, expand=1, fill=tk.X)

requestBox = tk.Entry(controllerFrame)
requestBox.pack(anchor=tk.NW, side=tk.LEFT, expand=1, fill=tk.BOTH)

startButton = tk.Button(controllerFrame, text='実行', command=worker)
startButton.pack(side=tk.LEFT, anchor=tk.NW)

stopFrame = tk.Frame(mainFrame, height=100)
stopFrame.pack(anchor=tk.NW, side=tk.TOP, expand=1, fill=tk.X)

stopButton = tk.Button(stopFrame, text='音楽をストップ', command=stop_sound)
stopButton.pack(side=tk.LEFT, anchor=tk.NW)

resultFrame = tk.Frame(mainFrame)
resultFrame.pack(anchor=tk.NW, expand=1, fill=tk.BOTH)

resultBox = tk.Text(resultFrame)
resultBox.pack(side=tk.LEFT, anchor=tk.NW, expand=1, fill=tk.BOTH)

resultBox.insert('end', open(thisDir + '/ORIZIN_Agent_AA.txt', encoding='utf-8_sig').read())


root.mainloop()
