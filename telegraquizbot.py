# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 22:29:18 2021

@author: abaha
"""


import telepot
import logging
import json, requests
#from telegram import TelegramObject, constants
import datetime
from typing import TYPE_CHECKING, Any, List, Optional, Union, Tuple
import time
import requests
import sqlite3
import random
import tweepy_bot as tw
import sys





from telegram.utils.helpers import (
    mention_html as util_mention_html,
    DEFAULT_NONE,
    DEFAULT_20,)


from telegram import (
    Poll,
    ParseMode,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,InlineKeyboardButton,PollAnswer, InlineKeyboardMarkup,
    
    
    User, Message, Update, Chat, ChatMember, UserProfilePhotos, File,
                      ReplyMarkup, TelegramObject, WebhookInfo, GameHighScore, StickerSet,
                      PhotoSize, Audio, Document, Sticker, Video, Animation, Voice, VideoNote,
                      Location, Venue, Contact, InputFile, Poll,ChatPermissions,TelegramObject, constants
)



from telegram.ext import (
    Updater,
    CommandHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
    CallbackContext,ChatMemberHandler,
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

import pandas as pd
dfexcel=pd.read_excel('test.xlsx')
df2=pd.read_excel('telegram.xlsx')
sor=pd.read_excel("merkez_bankasi.xlsx")

updater = Updater("1989147614:AAHL-LmGLahobeLAJKUakLY3KRjfEeSfsDg")
bot = telepot.Bot('1989147614:AAHL-LmGLahobeLAJKUakLY3KRjfEeSfsDg')
chat_id1 = "-1001480725025" #banquiz
chat_id2 = "-1001593134678" 
chat_id3 = "-1001511873455" #deneme

#telegram id


chat_id11="1507938293"

# bot.sendMessage(chat_id1,"Merhaba Arkadaşlar 5 dakika sonra test başlayacaktır.")


# time.sleep(240)
#bot.sendMessage(chat_id1,"Test içi son bir dakika")


#time.sleep(60)


i=0
a=0


def BanQuizSozluk(update: Update, context: CallbackContext) -> None:
    soru_bul=random.randint(0, 314)
    id_bul=update.message.chat_id
    
    bot.sendMessage(id_bul,str(sor.iloc[soru_bul,1])+" nedir?")
    #update.message.reply_text(str(sor.iloc[soru_bul,1])+" nedir?")
    #bot.sendMessage(chat_id1,"--------------------------")
    
    time.sleep(5)
    bot.sendMessage(id_bul,str(sor.iloc[soru_bul,2]))
    #update.message.reply_text(str(sor.iloc[soru_bul,2]))
    print(str(soru_bul))
    a=str(sor.iloc[soru_bul,1])+" nedir?"+"\n"
    
    b=str(sor.iloc[soru_bul,2])
    mesaj=a+b
    tw.twitat(mesaj)

   
   
def BanQuizDeneme(update: Update, context: CallbackContext) -> None: #bunu kullanıyorum
    
    gelen3=update.effective_user.id
    id_bul=update.message.chat_id
    con = sqlite3.connect("kartest1.sqlite")
    df=pd.read_sql('SELECT * FROM test2', con) 
    
    
    print(gelen3)
    
    if gelen3==1507938293 or gelen3==1087968824:
        sorusayisi=50
        
        bot.sendMessage(id_bul,"Bu deneme "+str(sorusayisi)+" sorudan oluşmaktadır.")
        #bot.sendMessage(id_bul,"Sorular 20 saniye ara ile gelecektir.")
        
        time.sleep(20)
        
        
        global i,rdb,rdbu
        
        for i in range(sorusayisi):
            time.sleep(20)
        
        
    
            
            rdb=1
            rdbu=6832
            explanation1="Bu sorular BanQuiz uygulamasından alınmıştır. Daha fazla soru için BanQuiz uygulamasını Google Play'den indirmeyi unutmayınız."
        
            
            
            while True:
                
              random_sayı=random.randint(rdb,rdbu)
              
              if df.iloc[random_sayı,6] is None:
                  
                  if(len(df.iloc[random_sayı,1])<245 and len(df.iloc[random_sayı,2])<100 
                         and len(df.iloc[random_sayı,3])<100 and len(df.iloc[random_sayı,4])<100 
                         and len(df.iloc[random_sayı,5])<100 ):
                      
                      break
                     
              else:
                  
                  if(len(df.iloc[random_sayı,1])<245 and len(df.iloc[random_sayı,2])<100 
                        and len(df.iloc[random_sayı,3])<100 and len(df.iloc[random_sayı,4])<100 
                        and len(df.iloc[random_sayı,5])<100  and len(df.iloc[random_sayı,6])<100 ):
                                            
                      break
                  
          
              
                        
               
                
                
           
            if i<sorusayisi :
                i=i+1
                    #for m in range(7):
                """Send a predefined poll"""
                #time.sleep(60)
            
                if df.iloc[random_sayı,6] is None:
                    
                    questions = [str( df.iloc[random_sayı,2]), str( df.iloc[random_sayı,3]), str( df.iloc[random_sayı,4]), str( df.iloc[random_sayı,5])]
                   
                else:
                    
                    questions = [str( df.iloc[random_sayı,2]), str( df.iloc[random_sayı,3]), str( df.iloc[random_sayı,4]), str( df.iloc[random_sayı,5]), str( df.iloc[random_sayı,6])]
                    
                    
                   
                dogru_cevap_yaz=dogrucevap( df.iloc[random_sayı,7])
                message = update.effective_message.reply_poll(
                    "["+str(i)+"/"+str(sorusayisi)+"]."+str( df.iloc[random_sayı,1]), questions, is_anonymous=False  ,type=Poll.QUIZ, explanation=explanation1 ,correct_option_id=int( dogru_cevap_yaz)
                )
                # Save some info about the poll the bot_data for later use in receive_quiz_answer
                payload = {
                message.poll.id: {
                    "questions": questions,
                    "message_id": message.message_id,
                    "chat_id": update.effective_chat.id,
                    "answers": df.iloc[random_sayı,7],
                }
                
            }
                context.bot_data.update(payload)
            # global a
            # a=a+1    
            # dfexcel['a'].loc[1,1]=str(questions)
            # dfexcel['b'].loc[2,2]=str(message.message_id)
            # dfexcel['c'].loc[3,3]=str(update.effective_chat.id)
            time.sleep(2)
            
            
                
            if i>=sorusayisi :
                update.message.reply_text("Test Bitmiştir. Herkese Teşekkürler")
                time.sleep(5)
                button = [[InlineKeyboardButton("Daha Fazla Soru için Google Play'den Uygulamayı Yükleyiniz", url = 'https://play.google.com/store/apps/details?id=test.ilk.test')],
                          [InlineKeyboardButton("İnstagram'dan Takip İçin", url = 'https://www.instagram.com/banquiz_tr/')],
                          [InlineKeyboardButton("Twitter'dan Takip İçin", url = 'https://twitter.com/banquiz_tr')]
                          ]
                message2 = "Bu sorular BanQuiz uygulaması denemelerinden alınmıştır. Daha fazla soru için BanQuiz uygulamasını Google Play'den indirmeyi unutmayınız"
        
            # using one_time_keyboard to hide the keyboard
                update.effective_message.reply_text(
                message2, reply_markup=InlineKeyboardMarkup(button, one_time_keyboard=True)
                )
               
    else:
        
        
        bot.sendMessage(id_bul,"/BanQuizDeneme komutunu sadece Yöneticiler çalıştırabilir")
            

def BanQuizTest(update: Update, context: CallbackContext) -> None: #bunu kullanıyorum
    
    gelen3=update.effective_user.id
    id_bul=update.message.chat_id
    #ziraat = sqlite3.connect("ziraatbank1.sqlite")
    #gkultur = sqlite3.connect("genelkultur1.sqlite")
    #parabanka = sqlite3.connect("parabanka1.sqlite")
    gekonomi = sqlite3.connect("genelekonomibank1.sqlite")
    #df=pd.read_sql('SELECT * FROM test21', ziraat)
    #df=pd.read_sql('SELECT * FROM test10', gkultur)
    #df=pd.read_sql('SELECT * FROM test1', parabanka)
    df=pd.read_sql('SELECT * FROM test52', gekonomi)
    
    #sorusayisi=pd.read_sql('SELECT * FROM test21', ziraat).count()["sira"]
    #sorusayisi=pd.read_sql('SELECT * FROM test10', gkultur).count()["sira"]
    #sorusayisi=pd.read_sql('SELECT * FROM test1', parabanka).count()["sira"]
    sorusayisi=pd.read_sql('SELECT * FROM test52', gekonomi).count()["sira"]
    
    print(gelen3)
    
    if gelen3==1507938293 or gelen3==1087968824:
        
        
        bot.sendMessage(id_bul,"Bu deneme "+str(sorusayisi)+" sorudan oluşmaktadır.")
        #bot.sendMessage(id_bul,"Sorular 20 saniye ara ile gelecektir.")
        
        time.sleep(20)
        
        
        global i,rdb,rdbu
        
        
       
    
        
        explanation1="Bu sorular BanQuiz uygulamasından alınmıştır. Daha fazla soru için BanQuiz uygulamasını Google Play'den indirmeyi unutmayınız."
    
        
        random_sayı=1
        i=0
        for random_sayı in range(int(sorusayisi)):
            
          
          
          
       
          if i<int(sorusayisi) :
                i=i+1
                if df.iloc[random_sayı,6] is None:
                      
                      questions = [str( df.iloc[random_sayı,2]), str( df.iloc[random_sayı,3]), str( df.iloc[random_sayı,4]), str( df.iloc[random_sayı,5])]
                     
                else:
                      
                      questions = [str( df.iloc[random_sayı,2]), str( df.iloc[random_sayı,3]), str( df.iloc[random_sayı,4]), str( df.iloc[random_sayı,5]), str( df.iloc[random_sayı,6])]
                      
                      
                     
                      dogru_cevap_yaz=dogrucevap( df.iloc[random_sayı,7])
                      message = update.effective_message.reply_poll(
                      "["+str(i)+"/"+str(sorusayisi)+"]."+str( df.iloc[random_sayı,1]), questions, is_anonymous=False  ,type=Poll.QUIZ, explanation=explanation1 ,correct_option_id=int( dogru_cevap_yaz)
                  )
                  # Save some info about the poll the bot_data for later use in receive_quiz_answer
                      payload = {
                      message.poll.id: {
                      "questions": questions,
                      "message_id": message.message_id,
                      "chat_id": update.effective_chat.id,
                      "answers": df.iloc[random_sayı,7],
                  }
                  
              }
                context.bot_data.update(payload)
            
                time.sleep(20)
              
              
                  
          if i>=sorusayisi :
                  update.message.reply_text("Test Bitmiştir. Herkese Teşekkürler")
                  time.sleep(5)
                  button = [[InlineKeyboardButton("Daha Fazla Soru için Google Play'den Uygulamayı Yükleyiniz", url = 'https://play.google.com/store/apps/details?id=test.ilk.test')],
                            [InlineKeyboardButton("İnstagram'dan Takip İçin", url = 'https://www.instagram.com/banquiz_tr/')],
                            [InlineKeyboardButton("Twitter'dan Takip İçin", url = 'https://twitter.com/banquiz_tr')]
                            ]
                  message2 = "Bu sorular BanQuiz uygulaması denemelerinden alınmıştır. Daha fazla soru için BanQuiz uygulamasını Google Play'den indirmeyi unutmayınız"
          
              # using one_time_keyboard to hide the keyboard
                  update.effective_message.reply_text(
                  message2, reply_markup=InlineKeyboardMarkup(button, one_time_keyboard=True)
                  )
                 
    else:
        bot.sendMessage(id_bul,"/BanQuizTest komutunu sadece Yöneticiler çalıştırabilir")
            

def BanQuizSoru(update: Update, context: CallbackContext) -> None: #bunu kullanıyorum
    
    sorusayisi=1
    id_bul=update.message.chat_id
    con = sqlite3.connect("kartest1.sqlite")
    df=pd.read_sql('SELECT * FROM test2', con) 
    #bot.sendMessage(id_bul,"Bu deneme "+str(sorusayisi)+" sorudan oluşmaktadır.")
    #bot.sendMessage(id_bul,"Sorular 20 saniye ara ile gelecektir.")
    
    #time.sleep(5)
    
    
    global i,rdb,rdbu
    
    for i in range(sorusayisi):
        #time.sleep(5)
    
    

        
        rdb=1
        rdbu=6832
        explanation1="Bu sorular BanQuiz uygulamasından alınmıştır. Daha fazla soru için BanQuiz uygulamasını Google Play'den indirmeyi unutmayınız."
    
        random_sayı=random.randint(rdb,rdbu) 
        
        while True:
            
          random_sayı=random.randint(rdb,rdbu)
          
          if df.iloc[random_sayı,6] is None:
              
              if(len(df.iloc[random_sayı,1])<245 and len(df.iloc[random_sayı,2])<100 
                     and len(df.iloc[random_sayı,3])<100 and len(df.iloc[random_sayı,4])<100 
                     and len(df.iloc[random_sayı,5])<100 ):
                  
                  break
                 
          else:
              
              if(len(df.iloc[random_sayı,1])<245 and len(df.iloc[random_sayı,2])<100 
                    and len(df.iloc[random_sayı,3])<100 and len(df.iloc[random_sayı,4])<100 
                    and len(df.iloc[random_sayı,5])<100  and len(df.iloc[random_sayı,6])<100 ):
                                        
                  break
                
        
        
    
            
            
       
        if i<sorusayisi :
            i=i+1
                #for m in range(7):
            """Send a predefined poll"""
            #time.sleep(60)
        
            if df.iloc[random_sayı,6] is None:
                
                questions = [str( df.iloc[random_sayı,2]), str( df.iloc[random_sayı,3]), str( df.iloc[random_sayı,4]), str( df.iloc[random_sayı,5])]
               
            else:
                
                questions = [str( df.iloc[random_sayı,2]), str( df.iloc[random_sayı,3]), str( df.iloc[random_sayı,4]), str( df.iloc[random_sayı,5]), str( df.iloc[random_sayı,6])]
                
                
               
            dogru_cevap_yaz=dogrucevap( df.iloc[random_sayı,7])
            message = update.effective_message.reply_poll(
                "["+str(i)+"/"+str(sorusayisi)+"]."+str( df.iloc[random_sayı,1]), questions, is_anonymous=False  ,type=Poll.QUIZ, explanation=explanation1 ,correct_option_id=int(dogru_cevap_yaz)
            )
            # Save some info about the poll the bot_data for later use in receive_quiz_answer
            payload = {
            message.poll.id: {
                "questions": questions,
                "message_id": message.message_id,
                "chat_id": update.effective_chat.id,
                "answers": df.iloc[random_sayı,7],
            }
            
        }
            context.bot_data.update(payload)
        # global a
        # a=a+1    
        # dfexcel['a'].loc[1,1]=str(questions)
        # dfexcel['b'].loc[2,2]=str(message.message_id)
        # dfexcel['c'].loc[3,3]=str(update.effective_chat.id)
        #time.sleep(20)
        
        
            
        if i>=sorusayisi :
           # update.message.reply_text("Test Bitmiştir. Herkese Teşekkürler")
            time.sleep(1)
            button = [[InlineKeyboardButton("Daha Fazla Soru için Google Play'den Uygulamayı Yükleyiniz", url = 'https://play.google.com/store/apps/details?id=test.ilk.test')],
                      [InlineKeyboardButton("İnstagram'dan Takip İçin", url = 'https://www.instagram.com/banquiz_tr/')],
                      [InlineKeyboardButton("Twitter'dan Takip İçin", url = 'https://twitter.com/banquiz_tr')]
                      ]
            message2 = "Bu sorular BanQuiz uygulaması denemelerinden alınmıştır. Daha fazla soru için BanQuiz uygulamasını Google Play'den indirmeyi unutmayınız"
    
        # using one_time_keyboard to hide the keyboard
            update.effective_message.reply_text(
            message2, reply_markup=InlineKeyboardMarkup(button, one_time_keyboard=True)
            )
           
 

def Twitter_kullanici(update: Update, context: CallbackContext) -> None:
    
  
    id_bul=update.message.chat_id
    

   
   
    
    
    texte=update.message.text
    id_bul=update.message.chat_id
   
    
    ara=texte.split(" ")
    yaz=ara[1]
    i=1
  
    bot.sendMessage(id_bul,"-----"+yaz.upper()+" tarafından atılan son 10 tweet------------")
    m=tw.kullanıcı_veri_cek(yaz)
    for yazdir in m:
        bot.sendMessage(id_bul,str(i)+"- "+yazdir.text)
        
        time.sleep(5)
        #print(yazdir)
        i+=1
    
    
def Twitter(update: Update, context: CallbackContext) -> None:
    
    texte=update.message.text
    id_bul=update.message.chat_id
    yaz=[]
   
    ara=texte.split(" ")
    print(len(ara))
    
    if len(ara)<3:
        ara.append(" ")
        print(ara[2])
    yaz.append(ara[1]) 
    yaz.append(ara[2]) 
    
    i=1
    
    bot.sendMessage(id_bul,"-----"+"Popüler tweetler------------")
    
    #update.message.reply_text("-------ilk 5------------")  
    m=tw.hastag_ozet_pandas(yaz).sort_values("retweet_count",ascending=False)
   # df.iloc[random_sayı,1]
    for yazdir in range(0,10):
       bot.sendMessage(id_bul,str(i)+"-"+"Twitter Kullanıcısı: "+m["screen_name"][yazdir]+"\n"
                                 +"Twitter Mesajı: "+ m["text"][yazdir]+ "\n Retweet Sayısı:"+
                                 str(m["retweet_count"][yazdir]) +
                                     "\n Tweet tarihi: "+str(m["created_at"][yazdir])
                                 )
       time.sleep(5)
       i+=1
       if i==11:
           break
      
                                   
def sonuclar(update: Update, context: CallbackContext) -> None:
    
    
    
    
    gelen3=update.effective_user.id
    id_bul=update.message.chat_id
    
    
    if gelen3==1507938293 or gelen3==1087968824:
        
     
        context.bot.send_document(id_bul, document=open('sonuclar.xlsx', 'rb'), filename="sonuclar.xlsx")
        #bot.sendMessage(id_bul,dosya)
        
        
    
        
       
                
            
        
        #dosya = open("sonuclar2.txt", "r").read()
        
        
       #bot.sendMessage(id_bul,dosya)
        #dosya.close()
    else: 
        bot.sendMessage(id_bul,"/Sonuclar komutunu sadece Yöneticiler çalıştırabilir")

def Trendtopic(update: Update, context: CallbackContext) -> None:
    id_bul=update.message.chat_id
    id_bul2=update.message.message_id
      
  
    m=tw.trendleri_ozet_cek()
    i=1
      
    toplu=[]
    dosya = open("trend.txt", "w")
    
    bot.sendMessage(id_bul,"Twitter TT listesi yükleniyor lütfen bekleyiniz")
   
   
    
   
    for yazdir in m:
        #bot.sendMessage(id_bul,"Twitter TT listesi yükleniyor lütfen bekleyiniz")
        #id_bul2=update.message.message_id
        #id_bul=update.message.message_id
        
        toplu.append(yazdir["name"])
        dosya.write(str(i)+"- "+yazdir["name"]+"\n")
        #update.message.reply_text(str(i)+"-"+yazdir["name"])
        #print(f'{i} - {yazdir["name"]}')
        #toplu.append(str(i)+"-"+yazdir["name"]+"\n")
        time.sleep(1)
        i+=1
        
       
            
         
    dosya.close()
    time.sleep(5) 
    dosya = open("trend.txt", "r").read()
    
    
    bot.sendMessage(id_bul,"-------Twitter TT Liste------------")
    bot.sendMessage(id_bul,dosya)
    dosya.close()
    print(toplu)
  
def deneme(update: Update, context: CallbackContext) -> None:
    gelen=update.message.text
    gelen2=update.effective_user.name
    gelen3=update.effective_user.id
    
    
    """Inform user about what this bot can do"""
    if gelen.lower().find("kullanci_id")!=-1:
        
        #gelen3=update.message.username_id
        print (gelen2)
        print(gelen3)
        update.message.reply_text(str(gelen2)+" kullanıcı id'niz: "+str(gelen3))
        #update.message.delete()
    
   
    
    # if gelen.lower().find("BanQuizyeni")!=-1:
    #     update.message.reply_text("Lütfen şu şekilde yazınız /BanQuizyeni")
        
        
    if gelen.lower().find("hata")!=-1 or gelen.lower().find("yanlış")!=-1:
        s=update.effective_user.name
        update.message.reply_text(s+" Dikkatiniz için teşekkürler. Bir kontrol edelim.")
        updater = Updater("1989147614:AAHL-LmGLahobeLAJKUakLY3KRjfEeSfsDg")

s=0
def receive_poll_answer(update: Update, context: CallbackContext) -> None:
    
    """Summarize a users poll vote"""
    
    
    global s,d
    s=s+1
    answer= update.poll_answer
    #danswer=update.poll.correct_option_id
    answer1=str(answer['option_ids']).replace("[","")
    answer2=answer1.replace("]","")
    print(answer2)
    poll_id = answer.poll_id
    questions = context.bot_data[poll_id]["questions"]
    correct_option=context.bot_data[poll_id]["answers"]
    df2.loc[s,'index']=answer['poll_id']
    df2.loc[s,'d.index']=questions
    correct_option2=dogrucevap(correct_option)
    df2.loc[s,'d.cevap']=correct_option2
    
    df2.loc[s,'soyad']=answer.user['last_name']   
    df2.loc[s,'ad']=answer.user['first_name'] 
    df2.loc[s,'id']=answer.user['id'] 
    
    kullanici=str(answer.user['first_name']) +" "+str(answer.user['last_name'])
    df2.loc[s,'Kullanici']= kullanici.replace("None", "")
    
    df2.loc[s,'cevap']=answer2
    df2.loc[s,'Dogru']=int(df2.loc[s,'cevap'])-int(df2.loc[s,'d.cevap'])
    if df2.loc[s,'Dogru']==0:
        df2.loc[s,'Dogru']=1
        df2.loc[s,'Yanlis']=0
        df2.loc[s,'Toplam']=1
    else:
        df2.loc[s,'Dogru']=0
        df2.loc[s,'Yanlis']=1
        df2.loc[s,'Toplam']=1
        
        
    
    
    # pd.DataFrame({ 'Open' : [10]})
    #df2["kadi"] = answer['username']
    # df2["cevaplar"] = pd.DataFrame(answer['option_ids'])
    # #cevap=answer['option_ids']
   
    
    #df2['cevaplar'].loc[0]=answer['option_ids']
    #y=json.dumps(answer)
    
    df3=pd.DataFrame(df2,columns=["Kullanici","Dogru","Yanlis","Toplam"])
    df4=df3.groupby("Kullanici").sum()
    df4.sort_values("Dogru",ascending=False)
    
   
    #df3.groupby("ad")["cevap"].count()
    
   # bot.sendMessage(chat_id2,str(df2))


   
        


    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)   

def BanQuizYardım(update: Update, context: CallbackContext) -> None:
    

    id_bul=update.message.chat_id
 

    bot.sendMessage(id_bul,"BanQuiz Komutlar")
    bot.sendMessage(id_bul,"****************")
    time.sleep(2)
    bot.sendMessage(id_bul,"/BanQuizSoru ----->Rastgele Bir Soru Gönderir")
    bot.sendMessage(id_bul,"")
    time.sleep(2)
    bot.sendMessage(id_bul,"/BanQuizSozluk ----->Rastgele Bir Ekonomik Terim Gönderir")
    bot.sendMessage(id_bul,"")
    time.sleep(2)
    bot.sendMessage(id_bul,"/Twitter konu ----->Konu kısmına yazdığınız herhangi bir şeyin Twitterda ilk 5 popüler Tweetini gönderir. ")
    bot.sendMessage(id_bul,"")
    time.sleep(2)
    bot.sendMessage(id_bul,"/Twitter_kullanici kullanıcı ----->kullanıcı kısmına yazdığınız twitter kullanıcısının Twitterdaki 10 popüler Tweetini gönderir. ")
    bot.sendMessage(id_bul,"")
    time.sleep(2)
    bot.sendMessage(id_bul,"/Trendtopic ----->Twitter Güncel Trend Topic Listesini Gönderiri ")
    bot.sendMessage(id_bul,"") 
    time.sleep(2)
    bot.sendMessage(id_bul,"/BanQuizTest ----->Sadece Yöneticiler Çalıştırabilir") 
    bot.sendMessage(id_bul,"") 
    time.sleep(2)
    bot.sendMessage(id_bul,"/BanQuizDeneme ----->Sadece Yöneticiler Çalıştırabilir") 
    bot.sendMessage(id_bul,"") 
    time.sleep(2)
    bot.sendMessage(id_bul,"/Sonuclar ----->Sadece Yöneticiler Çalıştırabilir") 
    bot.sendMessage(id_bul,"") 
    time.sleep(2)
 
   


def main() -> None:
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1989147614:AAHL-LmGLahobeLAJKUakLY3KRjfEeSfsDg")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('BanQuizYardım', BanQuizYardım))
    dispatcher.add_handler(CommandHandler('BanQuizDeneme', BanQuizDeneme))
    dispatcher.add_handler(CommandHandler('BanQuizTest', BanQuizTest))
    dispatcher.add_handler(CommandHandler('BanQuizSoru', BanQuizSoru))
    dispatcher.add_handler(CommandHandler('Twitter', Twitter))
    dispatcher.add_handler(CommandHandler('Twitter_kullanici', Twitter_kullanici))
    dispatcher.add_handler(CommandHandler('BanQuizSozluk', BanQuizSozluk))
    dispatcher.add_handler(CommandHandler('sonuclar', sonuclar))
    
    #dispatcher.add_handler(PollHandler(receive_quiz_answer))
    
    
    dispatcher.add_handler(CommandHandler('Trendtopic', Trendtopic))
    #dispatcher.add_handler(MessageHandler(Filters.text, deneme))
    dispatcher.add_handler(PollAnswerHandler(receive_poll_answer))
    #dispatcher.add_handler(PollHandler(receive_quiz_answer))
    
    
    
    
    

    # Start the Bot
    updater.start_polling()
    

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


def sonuclari_yazdir():
    dosya = open("sonuclar.txt", "r")
    satirlar=dosya.readlines()
    
    




    sonuc=[]
    x=0
    h=0
    for dizi in satirlar:
        
        if (x==0):
            sonuc.append(dizi)
        
        if (x==1) or (x==0):
            print("a")
            
        else:
            sonuc.append(str(h-1)+"-"+dizi)
            
        x=x+1
        h=h+1
    dosya.close()
    dosya = open("sonuclar2.txt", "w")

    for sonuclari_yaz in sonuc:
        
        dosya.write(sonuclari_yaz)

    dosya.close()

def dogrucevap(cevap_cevir):
    if cevap_cevir=="A":
        return "0"
    if cevap_cevir=="B":
        return "1"
    if cevap_cevir=="C":
        return "2"
    if cevap_cevir=="D":
        return "3"
    if cevap_cevir=="E":
        return "4"

if __name__ == '__main__':
    main()
    df3=pd.DataFrame(df2,columns=["Kullanici","Dogru","Yanlis","Toplam"])
    df4=df3.groupby("Kullanici").sum()
    df5=df4.sort_values(by='Dogru', ascending=False)
    time.sleep(15)
    df5.to_excel("sonuclar.xlsx")
    #dosya = open("sonuclar.txt", "w")
    #dosya.write(str(df5))
    #dosya.close()
    
   
    

