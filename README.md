# Line Notify Sample

Line Notifyを無理矢理まとめた

雑なのは我慢してk(ry

## Function
- sendMessage
- sendSticker
- sendImage
- sendImageWithURL
- check_token
- revoke_token

## Requirement

* requests

## Token
LINE Notifyのトークン取得方法

[ここ](https://notify-bot.line.me/ja/)からアカウントを登録してトークンを取得

アカウント作成後、マイページ -> トークンを発行する -> トークン名/トークルームを設定 -> 発行する

発行されたトークンをコピーし以下のようにする

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
msg.revoke_token()
```
#### 一応かいてみる
* 以下の関数はmsg="hoge"で送信時のメッセージをカスタム可能(もちろん"msg="略可)
```
msg.sendSticker("1070", "17865", msg="すたんぷだよ")
msg.sendImage("sample.jpg", "ヲレの嫁！")
msg.sendImageWithURL("https://img.atwiki.jp/niconicomugen/attach/6163/12458/akr.png", msg="あっかりーん")
```

## Author

* MaguRo
