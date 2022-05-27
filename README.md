# Line Notify Sample

Line Notifyを無理矢理まとめた

## Function
- sendMessage
- sendSticker
- sendImage
- sendImageWithURL
- check_token
- revoke_token

## Requirement

* Line-Notify-Token

## Token
LINE Notifyのトークン取得方法

[ここ](https://notify-bot.line.me/ja/)からアカウントを登録してトークンを取得

アカウント作成後、マイページ -> トークンを発行する -> トークン名/トークルームを設定 -> 発行する

発行されたトークンをコピーし以下のようにする

```
self.token = "コピーしたトークン"
```

## Usage

#### 文字送信
```
self.sendMessage("Hello World")
```
#### スタンプ送信
パッケージ・スタンプIDは[ここ](https://developers.line.biz/ja/docs/messaging-api/sticker-list/)から取得

```
self.sendSticker("1070", "17865")
```
#### 画像送信
```
self.sendImage("sample.jpg")
```
#### URLの画像を送信
```
self.sendImageWithURL("https://img.atwiki.jp/niconicomugen/attach/6163/12458/akr.png")
```
#### トークン無効化
```
self.revoke_token()
```
#### いちおう
* send系はmsg="hoge"とする事で送信時のメッセージをカスタム可能
```
self.sendImageWithURL("https://img.atwiki.jp/niconicomugen/attach/6163/12458/akr.png", msg="あっかりーん")
```

## Author

* MaguRo
