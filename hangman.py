from flask import Flask, render_template, send_file
app = Flask(__name__)
import pandas as pd
import numpy as ny

def hang(ch,x1,l1):
    flag = 0
    while ch>0:
        a=input()
        q=0
        for b in x1:
            q+=1
            if b==a:
                l1[q-1]=a
                flag=0
                #print('-',q)
            else :
                #print('*')
                flag+=1
        if q<=flag:
            print('incorrect!!!')
            ch-=1
            print('chances left', ch)
        else:
            print(l1)
        if l1==x1:
            break
    return ch


def this_is_start():
    f=pd.read_excel('D:\\hangman.xlsx')
    i=0
    chances = 10
    while i<len(f.axes[0]):
        if pd.isnull(f.iat[i,1]):
            count=1
        if count==1:
            x=list(f.iat[i, 0])
            l = ['_'] * len(x)
        else:
            x=list(f.iat[i, 0])+list(f.iat[i, 1])
            l = ['_'] *len(x)
        temp=hang(chances,x,l)
        chances=temp
        if chances==0:
            print('Game Over!!!!')
            break
        elif chances>0:
            print('Congratulations You have ',chances,' chances left!!!')
            print('_____________________________________________________________')
            print('Enter char for new words')
        i +=1

def start_app():
    return render_template("hangmanMain.html")
    
@app.route("/highScore")
def highScore():
    return render_template("highScore.html")


@app.route("/play")
def play():
    return render_template("play.html")



@app.route("/images")
def images():
    return send_file("download.gif", mimetype='image/gif')


@app.route("/")
def hello():
    return start_app()

if __name__ == "__main__":
    app.run(debug=True)