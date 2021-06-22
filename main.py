import telebot
from telebot import util
from googletrans import Translator
from datetime import datetime
from PIL import Image
from io import BytesIO
import requests
import json
import random
from command import coman

def login(message):
    firstnam = message.chat.first_name
    lasnam = message.chat.last_name
    ttd = datetime.now()
    ttd = ttd.strftime('%d-%B-%Y %H:%M')
    ied = message.chat.id
    commands = message.text
    text_log = (f'{ttd}, id: {ied} {firstnam} {lasnam} \n')
    log_bot = open('log_bot.txt', 'a')
    log_bot.write(text_log)
    log_bot.close()

api = '1679956743:AAGdVrqU543CXmDHgFEH2wi3kFPrJkjYDJM'
apik = [
        '0cb413d1b5bb5d6b280aef02',
        '0a05583410c6fadbedd77265',
        '0a05583410c6fadbedd77265',
        '6561c76f08ae9517606e6896',
        '54e5f630beeab52bc3bcece8',
        '1382b7ecbff60da6ee1ea86d'
        ]
apikey = random.choice(apik)
bot = telebot.TeleBot(api)
tran = Translator()
now = datetime.now()
date = now.strftime("%B-%m-%Y, %H:%M:%S")
ses = requests.session()
headers = {
    'Cache-Control':'max-age=0'
        }
sen = ("Kau hanyalah setitik debu di alam semesta dan dunia tak peduli sedikit pun jika kau mati atau menang hari ini. Kematianmu tidaklah terlalu berharga daripada kematian seekor cacing. Mayat seekor cacing bisa menjadi makanan burung atau pupuk yang menyuburkan tanah. Jika kau mati, tubuhmu akan dikubur atau dibakar dan hanya menjadi asap yang berseliweran tanpa tujuan di angkasa raya. Semua pencapaianmu seperti kerikil-kerikil kecil yang hancur digilas roda waktu. Jika kau hidup, kau pikir kau punya waktu yang panjang dalam kehidupan yang tak terbatas ini? Jika kau mati, alam semesta masih akan tetap sama.")

@bot.message_handler(commands=['start'])
def selamat_datang(msg):
    login(msg)
    na = msg.chat.first_name
    ma = msg.chat.last_name
    cet = msg.chat.id
    print(na,ma,cet, "text:",cet)
    bot.reply_to(msg,f'{date}\nようこそ {na} {ma} id: {cet} i hope you will enjoyed on here.\nThis Bot Created with Python\ntype /help for the command\nAuthor: aldyansyahcp')

@bot.message_handler(commands=['help'])
def perintah(msg):
    cet = msg.chat.id
    #login(msg)
    bot.reply_to(msg, coman())
    ran = random.randint(0,1)
    #if ran == 0:
      #bot.send_message(cet,<a href="https://github.com/kroemen">disini</a>)
    #bot.reply_to(msg,('Okaerinasai Onii-Chan..  :-)\nlist command\n====================\n==>> Randomm \n/surah [surah apa]\n/short_link [url]\n/tiktok_dl [url]\n -tiktok downloader video from url \n/text_sound [keyword]\n -change text to sound\n/text_img [keyword]\n -change text to images\n/nulis [keyword]\n -change text to images in paper\n/qr_code [text]\n/random_quotes\n/chord_gitar [keyword]\n/wiki [keyword]\n/prank_call 898xxx\n/translate_jpan\n/yt_mp3 [code] \n/yt_vid [code]\n\n==>> Animes \n/anim_quotes\n/anim_character [keyword]\n/anim_batch [keyword]\n/animpict_search [keyword]\n/anime_neko\n/anime_loli\n/anime_random\n/anime_baka\n/nsfw_neko\n/nsfw_waifu\n\n==>> Information\n/ig_stalk [username]\n/jadwal_sholat [city]\n/weather [city]\n/earthquake\n======================\nExcept: for yt_mp3 & yt_vid\nyt_mp3 https://www,youtube,com/watch?v=H-Z2elwvBS8\n==>> yt_mp3 H-Z2elwvBS8'))

@bot.message_handler(commands=['ytmp3'])
def ym3(msg):
  cet = msg.chat.id
  tek = msg.text
  login(msg)
  if " " in tek:
    fin = tek.split(" ",1)
    url = ses.get("https://api.zeks.xyz/api/ytplaymp3?apikey=fEnw9oqZKR9OHrxBRoSXdIBBb35&q="+fin[1]).json()
    print(url['status'])
    if url['status'] == 'true':
      bot.send_message(cet,url['status'])
    else:
      bot.send_audio(cet,url['result']['url_audio'])
  else:
    pass

@bot.message_handler(commands=['ytmp4'])
def ym3(msg):
  cet = msg.chat.id
  tek = msg.text
  login(str(msg))
  if " " in tek:
    fin = tek.split(" ",1)
    url = ses.get("https://api.zeks.xyz/api/ytplaymp4?apikey=fEnw9oqZKR9OHrxBRoSXdIBBb35&q="+fin[1]).json()
    print(url['status'])
    if url['status'] == 'true':
      bot.send_message(cet,url['status'])
    else:
      bot.send_video(cet,url['result']['url_video'])
  else:
    pass

@bot.message_handler(commands=['short_link'])
def stlk(msg):
  tek = msg.text
  cet = msg.chat.id
  login(tek)
  if " " in tek:
    fin = tek.split(" ",1)
    url = ses.get("https://backend-ihsandevs.herokuapp.com/api/s.id/?url="+fin[1]).json()
    if url['status'] == 'true':
      bot.send_message(cet,url['result'])
    else:
      bot.send_message(cet, url['message'])
  else:
    pass
      
@bot.message_handler(commande=['surah'])
def mgrnls(msg):
  nam = msg.text
  cet = msg.chat.id
  if " " in nam:
    fin = nam.split(" ",1)
    url = ses.get("https://api.zeks.xyz/api/quran?no="+fin[1]+"&apikey=fEnw9oqZKR9OHrxBRoSXdIBBb35").json()
    if url['status'] == 200:
      bot.send_message(cet, url['result'])
    else:
      bot.send_photo(cet, url['message'])
  else:
    bot.send_message(cet, url['message'])

@bot.message_handler(commands=['qr_code'])
def kuis(msg):
  nam = msg.chat.first_name
  tek = msg.text
  cet = msg.chat.id
  login(msg)
  if " " in tek:
    fin = tek.split(" ",1)
    url = "https://api.zeks.xyz/api/qrencode?apikey=fEnw9oqZKR9OHrxBRoSXdIBBb35&text="+fin[1]
    hasil = ses.get(url, headers=headers).json()
    print(url)
    if hasil['status'] == 200:
      if type(hasil.content) == bytes:
        im = Image.open(BytesIO(hasil.content))
        im.save("pict/"+nam+"qr.png")
        photo = open("pict/"+nam+'qr.png', 'rb')
        bot.send_photo(cet, photo)
      else:
        bot.send_message(cet, "Error!")
    else:
     bot.send_message(cet, hasil['message'])
     
@bot.message_handler(commands=['tiktok_dl'])
def tikdl(msg):
  cet = msg.chat.id
  tek = msg.text
  login(msg)
  if " " in tek:
    fin = tek.split(" ",1)
    res = ses.get("https://tiktokd.herokuapp.com/tiktok?url="+fin[1]).json()
    if res['status'] == 200:
      bot.send_video(cet, res['data']['link'])
    else:
      bot.send_message(cet, res['message'])
  else:
    bot.send_message(cet,"ext://tiktok_dl [url]")
    
@bot.message_handler(commands=['text_sound'])
def teksd(msg):
  cet = msg.chat.id
  tek = msg.text
  nam = msg.chat.first_name
  login(msg)
  if " " in tek:
    fin = tek.split(" ",1)
    url = "https://salism3api.pythonanywhere.com/text2sound/?text="+fin[1]+"&languageCode=ja"
    res = ses.get(url)
    print(url)
    open("sound/sound_"+nam+".mp3", 'wb').write(res.content)
    lagu = open('sound/sound_'+nam+'.mp3','rb')
    bot.send_audio(cet, lagu)

@bot.message_handler(commands=['text_img'])
def tekmg(msg):
  cet = msg.chat.id
  tek = msg.text
  login(msg)
  if " " in tek:
    fin = tek.split(" ",1)
    res = ses.get("https://salism3api.pythonanywhere.com/text2img/?text="+fin[1]).json()
    if res["message"] == "Sukses!":
      bot.send_photo(cet, res["image"])
    else:
      bot.send_message(cet,res["message"])
  else:
    bot.send_message(cet, "ext: //text_img Sumimasen")
    
@bot.message_handler(commands=['nulis'])
def nulis(msg):
    cet = msg.chat.id
    tek = msg.text
    login(msg)
    if " " in tek:
      fin = tek.split(" ",1)
      res = ses.get("https://salism3api.pythonanywhere.com/write?text="+fin[1]).json()
      if res["message"] == "Sukses!":
        bot.send_photo(cet, res["images"][0])
      else:
        bot.send_message(cet, res["success"])
    else:
      bot.send_message(cet,"ext://nulis Dareka arimasuka")
 
@bot.message_handler(commands=['ig_stalk'])
def igstalk(msg):
    cet = msg.chat.id
    tek = msg.text
    login(msg)
    if " " in tek:
        fin = tek.split(" ",1)
        url = ses.get("https://lolhuman.herokuapp.com/api/stalkig/"+fin[1]+"?apikey="+apikey).json()
        print(url)
        if url['status'] == 200:
            bot.send_photo(cet, url['result']['photo_profile'])
            nam = url['result']['username']
            fuln = url['result']['fullname']
            bio = url['result']['bio']
            folr = url['result']['followers']
            folg = url['result']['following']
            pos = url['result']['posts']
            bot.send_message(cet,f"Name : {fuln}\nUsername : {nam}\nFollower : {folr}\nFollowing : {folg}\nPosts : {pos}\nBio : {bio}")
        else:
            bot.send_message(cet, url['message'])
    else:
        bot.send_message(cet,"ext: //ig_stalk jokowi")
@bot.message_handler(commands=['anim_quotes'])
def animquot(msg):
    cet = msg.chat.id
    url = requests.get("https://lolhuman.herokuapp.com/api/random/quotesnime?apikey="+apikey).json()
    if url['status'] == 200:
        bot.send_message(cet, f"{url['result']['quote']}\n\t- {url['result']['character']} -\nAnime {url['result']['anime']}")
    else:
        url['message']

@bot.message_handler(commands=['anim_character'])
def animchar(msg):
    cet = msg.chat.id
    tek = msg.text
    if " " in tek:
        fin = tek.split(" ",1)
        url = requests.get("https://lolhuman.herokuapp.com/api/character?apikey="+apikey+"&query="+fin[1]).json()
        print(url)
        if url['status'] == 200:
            bot.send_photo(cet, url['result']['image']['large'])
            rom = url['result']['name']['full']
            jep = url['result']['name']['native']
            des = url['result']['description'][slice(2000)]
            mov1 = f"{url['result']['media']['nodes'][0]['type']}\n{url['result']['media']['nodes'][0]['title']['romaji']}\n{url['result']['media']['nodes'][0]['title']['native']}"
            mov2 = f"{url['result']['media']['nodes'][1]['type']}\n{url['result']['media']['nodes'][1]['title']['romaji']}\n{url['result']['media']['nodes'][1]['title']['native']}"
            mov3 = f"{url['result']['media']['nodes'][2]['type']}\n{url['result']['media']['nodes'][2]['title']['romaji']}\n{url['result']['media']['nodes'][2]['title']['native']}"
            bot.send_message(cet, f"{rom}\n{jep}\n{des}\n{mov1}\n{mov2}\n{mov3}")
        else:
            bot.send_message(cet, url['message'])
    else:
        bot.send_message(cet, "ext//anim_character Zerotwo")

@bot.message_handler(commands=['anim_batch'])
def animsinop(msg):
    cet = msg.chat.id
    tek = msg.text
    if " " in tek:
        fin = tek.split(" ",1)
        url = requests.get("https://mhankbarbar.herokuapp.com/api/kuso?q="+fin[1]).json()
        if url['status'] == 200:
            bot.send_photo(cet, url['thumb'])
            bot.send_message(cet, f"{url['link_dl']}\n{url['info']}\n==========Sinopsis==========\n{url['sinopsis']}")
        else:
            bot.send_message(cet, url['error'])
    else:
        bot.send_message(cet, url['error'])

@bot.message_handler(commands=['weather'])
def weather(msg):
    brp = msg.text
    cet = msg.chat.id
    if " " in brp:
        cari = brp.split(" ",1)
        url = "https://lolhuman.herokuapp.com/api/cuaca/"+cari[1]+"?apikey="+apikey
        res = ses.get(url).json()
        if res['status'] == 200:
            bot.send_message(cet, f"Kota: {res['result']['tempat']}\nCuaca: {res['result']['cuaca']}\nKecptn Angin: {res['result']['angin']}\nKelembapan: {res['result']['kelembapan']}\nSuhu: {res['result']['suhu']}")
        else:
            bot.send_message(cet, hasil['status'])
    else:
        bot.send_message(cet, "ext:   //weather Jakarta")

@bot.message_handler(commands=['jadwal_sholat'])
def jadwalsholat(msg):
    brp = msg.text
    cet = msg.chat.id
    if " " in brp:
        cari = brp.split(" ",1)
        url = "https://lolhuman.herokuapp.com/api/sholat/"+cari[1]+"?apikey="+apikey
        print(url)
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_message(cet, f"{hasil['result']['wilayah']}\n{hasil['result']['tanggal']}\nSubuh - {hasil['result']['subuh']}\nDzuhur - {hasil['result']['dzuhur']}\nAshar - {hasil['result']['ashar']}\nMaghrib - {hasil['result']['maghrib']}\nIsya - {hasil['result']['isya']}")
        else:
            bot.send_message(cet, hasil['status'])
    else:
        bot.send_message(cet, "ext:   //jadwal_sholat Jakarta")

@bot.message_handler(commands=['earthquake'])
def earthquake(msg):
    cet= msg.chat.id
    res = requests.get("https://mhankbarbar.herokuapp.com/api/infogempa", headers = headers).json()
    if res['status'] == 200:
        bot.send_photo(cet,res['map'])
        bot.send_message(cet,f"Kedalaman : {res['kedalaman']}\nKoordinat:  {res['koordinat']}\nLokasi : {res['lokasi']}\nMagnitude : {res['magnitude']}\nPotensi : {res['potensi']}\nWaktu : {res['waktu']}")
    else:
        pass

@bot.message_handler(commands=['random_quotes'])
def quotes(msg):
    cet= msg.chat.id
    res = requests.get("https://mhankbarbar.herokuapp.com/api/randomquotes", headers = headers)
    ser = res.json()
    if res.status_code == 200:
      bot.send_message(cet,ser['quotes']+'\n- '+ser['author'])
    else:
      bot.send_message(cet,ser['status'])

@bot.message_handler(commands=['chord_gitar'])
def gitar(msg):
    brp = msg.text
    cet = msg.chat.id
    if " " in brp:
        cari = brp.split(" ",1)
        url = "https://mhankbarbar.herokuapp.com/api/chord?q="+cari[1]
        print(cari)
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_message(cet, hasil['result'])
        else:
            bot.send_message(cet, hasil['status'])
    else:
        bot.send_message(cet, "ext:   //chord_gitar dear god")

@bot.message_handler(commands=['translate_jpan'])
def translat(msg):
    kir = bot.send_message(msg.chat.id,'Type something for translate to Japanese. ')
    bot.register_next_step_handler(kir,jpan)
def jpan(msg):
    tr = msg.text
    res = tran.translate(tr,dest='ja')
    bot.send_message(msg.chat.id,f"{res.text}\n{res.pronunciation}")
    print(msg.chat.id,'ok')
    pass

@bot.message_handler(commands=['animpict_search'])
def pict(message):
    cet = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "https://lolhuman.herokuapp.com/api/wallpaper2?apikey="+apikey+"&query="+cari[1]
        print(url)
        hasil = requests.get(url).json()
        if hasil['status'] == 200:
            bot.send_photo(cet, hasil['result'])
        else:
            bot.send_message(cet, hasil['message'])
    else:
        bot.send_message(cet, "ext:   //pict_search keyword")

@bot.message_handler(commands=['anime_loli'])
def anim1(msg):
    cet = msg.chat.id
    nam = msg.chat.first_name
    url = requests.get("https://lolhuman.herokuapp.com/api/random/loli"+"?apikey="+apikey)
    print(url.status_code)
    if url.status_code == 200:
      if type(url.content) == bytes:
        im = Image.open(BytesIO(url.content))
        im.save("pict/"+nam+"ll.png")
        photo = open("pict/"+nam+'ll.png', 'rb')
        bot.send_photo(cet, photo)
      else:
        bot.send_message(cet,url.status_code)
    else:
      pass

@bot.message_handler(commands=['anime_random'])
def send_animepict(message):
    cet = message.chat.id
    response = requests.get("http://public-restapi.herokuapp.com/api/anime-random-image", headers = headers).json()
    bot.send_photo(cet, response['image'])

@bot.message_handler(commands=['anime_baka'])
def anim4(message):
    cet = message.chat.id
    nam = message.chat.first_name
    url = "https://lolhuman.herokuapp.com/api/random2/baka"+"?apikey="+apikey
    hasil = requests.get(url, headers=headers)
    print(url)
    if type(hasil.content) == bytes:
        im = Image.open(BytesIO(hasil.content))
        im.save("pict/"+nam+"bk.gif")
        photo = open("pict/"+nam+'bk.gif', 'rb')
        bot.send_animation(cet, photo)
    else:
        bot.send_message(cet, "//error")
    

@bot.message_handler(commands=['nsfw_neko'])
def anim5(message):
    cet = message.chat.id
    nam = message.chat.first_name
    url = "https://lolhuman.herokuapp.com/api/random/nsfw/neko"+"?apikey="+apikey
    hasil = requests.get(url, headers=headers)
    print(url)
    if hasil.status_code == 200:
      if type(hasil.content) == bytes:
        im = Image.open(BytesIO(hasil.content))
        im.save("pict/"+nam+"nsnk.png")
        photo = open("pict/"+nam+'nsnk.png', 'rb')
        bot.send_photo(cet, photo)
      else:
        bot.send_message(cet, hasil.status_code)
    else:
      bot.send_message(cet, hasil.status_code)

@bot.message_handler(commands=['nsfw_waifu'])
def anim6(message):
    cet = message.chat.id
    nam = message.chat.first_name
    url = "https://lolhuman.herokuapp.com/api/random/nsfw/waifu"+"?apikey="+apikey
    hasil = requests.get(url, headers=headers)
    print(url)
    if hasil.status_code == 200:
       if type(hasil.content) == bytes:
        im = Image.open(BytesIO(hasil.content))
        im.save("pict/"+nam+"nswf.png")
        photo = open("pict/"+nam+'nswf.png', 'rb')
        bot.send_photo(cet, photo)
    else:
        bot.send_message(cet, hasil.status_code)

@bot.message_handler(commands=['anime_neko'])
def anim7(message):
    cet = message.chat.id
    url = requests.get("https://mhankbarbar.herokuapp.com/api/nekonime",headers = headers).json()
    if url['status'] == 200:
        bot.send_photo(cet,url['result'])
    else:
        bot.reply_to(cet,url['status'])
        pass

@bot.message_handler(commands=['prank_call'])
def spam(msg):
    try:
        no = msg.text
        catid = msg.chat.id
        if ' ' in no:
            usr = no.split(' ',1)
            nomor = usr[1]
            res = requests.get('https://mhankbarbar.herokuapp.com/api/spamcall?no='+nomor).json()
            bot.send_message(catid,res['logs'])
        else:
            bot.send_message(catid,'ext: /prank_call 898xxx')
            pass
    except Exception as e:
        pass

@bot.message_handler(commands=['wiki'])
def send_wiki(msg):
    try:
        bagi = msg.text
        chat_id = msg.chat.id
        if ' ' in bagi:
            user = bagi.split(' ',1)
            cari = user[1]
            url = requests.get('https://mhankbarbar.herokuapp.com/api/wiki?q='+cari+'&lang=id&apiKey=api-key').json()
            if url['status'] == 200:
                hasil = url['result']
                bot.send_message(chat_id, hasil[slice(3000)])
            else:
                bot.send_message(chat_id, url['error'])
        else:
            bot.reply_to(message, '[!]404\next: /wiki Jokowi')
            pass
    except Exception as e:
        pass
"""
@bot.message_handler(commands=['yt_mp3'])
def yutub(msg):
    try:
        cet = msg.chat.id
        pesan = msg.text
        dl = pesan.split(' ',1)
        find = dl[1]
        url = requests.get('https://mhankbarbar.herokuapp.com/api/yta?url=https://youtu.be/'+find).json()
        if url['status'] == 200:
            bot.send_message(cet,url['result'])
        else:
            bot.send_message(cet,url['error'])
            pass
    except Exception as e:
        pass
@bot.message_handler(commands=['yt_vid'])
def yutub2(msg):
    try:
        cet = msg.chat.id
        pesan = msg.text
        dl = pesan.split(' ',1)
        find = dl[1]
        url = requests.get('https://mhankbarbar.herokuapp.com/api/ytv?url=https://youtu.be/'+find).json()
        if url['status'] == 200:
            bot.send_message(cet,url['result'])
        else:
            bot.send_message(cet,url['error'])
            pass
    except Exception as e:
        pass
"""
#bot.enable_save_next_step_handlers(delay=3)
#bot.load_next_step_handlers()
print('\t'+date)
print('\t'+'BOT STARTEDD'.center(30,'='))
bot.polling()