# hi there (˙꒳​˙)
# this program was created by MaguRo
# i'd be happy to help u all learn how to program
# have a nice programming life!!

import requests

class Maguro():
    def __init__(self):
        # Line-Notify token
        self.token = ""

    def main(self) -> None:
        """ write the process here | ここに処理を書く """
        
        # 例:
        #   send text | 文字送信
        #   self.sendMessage("まぐろしかかたん!")
        #
        #   send sticker | スタンプ送信
        #   self.sendSticker("1070", "17865")
        #
        #   send image | 画像送信
        #   self.sendImage("sample.jpg")
        #
        #   send url-image | URLの画像を送信
        #   self.sendImageWithURL("https://img.atwiki.jp/niconicomugen/attach/6163/12458/akr.png", "あっかりーん")
        
        self.sendMessage("hi tuna")

    # 文字送信
    def sendMessage(self, msg: str) -> None:
        """ msg : text | msg : 文字"""
        self.post({"message": msg})

    #　スタンプ送信
    def sendSticker(self, pkg_id: str, stk_id: str, msg: str="sticker") -> None:
        """ pkg_id : package id, stk_id : sticker id, msg : sticker title
            pkg_id : パッケージID, stk_id : スタンプID, msg : スタンプタイトル """
        self.post({"message": msg, "stickerPackageId": pkg_id, "stickerId": stk_id})

    # 画像送信
    def sendImage(self, path: str, msg: str="image") -> None:
        """ path : image path, msg : image title
            path : 画像パス,    msg : 画像タイトル """
        self.post({"message": msg}, {"imageFile": open(path, "rb")})

    # URLの画像を送信
    def sendImageWithURL(self, url: str, msg: str="image") -> None:
        """ url : image url, msg : image title
            url : 画像URL     msg : 画像タイトル """
        with open("tmp.jpg", "wb") as f:
            f.write(requests.get(url).content)
        self.post({"message": msg}, {"imageFile": open("tmp.jpg", "rb")})

    def post(self, payload: dict, files: dict={}) -> requests.models.Response:
        """ request """
        return requests.post(
            url="https://notify-api.line.me/api/notify",
            headers={"Authorization": f"Bearer {self.token}"},
            params=payload,
            files=files
        )


if __name__ == "__main__":
    Maguro().main()
