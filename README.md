# Line Notify Sample

Line Notifyを無理矢理まとめた

雑なのは我慢してk(ry

## Function
- sendMessage
- sendSticker
- sendImage
- sendImageWithURL
- check
- revoke

## Requirement

* requests

## Token
LINE Notifyのトークン取得方法

[ここ](https://notify-bot.line.me/ja/)からアカウントを登録してトークンを取得

アカウント作成後、マイページ -> トークンを発行する -> トークン名/トークルームを設定 -> 発行する

発行されたトークンをコピーし"main.py"を開き以下のようにする

```
msg = Maguro("コピーしたトークン")
```

## Usage

#### 文字送信
```
msg.sendMessage("Hello World")
```
#### スタンプ送信
* パッケージ・スタンプIDは[ここ](https://developers.line.biz/ja/docs/messaging-api/sticker-list/)から取得

```
msg.sendSticker("1070", "17865")
```
#### 画像送信
```
msg.sendImage("sample.jpg")
```
#### URLの画像を送信
```
msg.sendImageWithURL("https://img.atwiki.jp/niconicomugen/attach/6163/12458/akr.png")
```
#### トークン無効化
```
msg.revoke()
```
#### 一応かいてみる
* 以下の関数はmsg="hoge"で送信時のメッセージをカスタム可能
```
msg.sendSticker("1070", "17865", msg="すたんぷだよ")
msg.sendImage("sample.jpg", "ヲレの嫁！")
msg.sendImageWithURL("https://img.atwiki.jp/niconicomugen/attach/6163/12458/akr.png", あっかりーん")
```

* 以下の関数はsilent=Trueで送信時のプッシュ通知をオフに可能
```
msg.sendMessage("ゆなしゅきぃ///", silent=True)
msg.sendSticker("1070", "17865", msg="すたんぷだよ", True)
msg.sendImage("sample.jpg", "ヲレの嫁！", True)
msg.sendImageWithURL("https://img.atwiki.jp/niconicomugen/attach/6163/12458/akr.png", あっかりーん", True)
```

## Author

* MaguRo
