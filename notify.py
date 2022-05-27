# hi there (˙꒳​˙)
# this program was created by MaguRo
# i'd be happy to help u all learn how to program
# have a nice programming life!!
#
# plz check:https://github.com/MocA-Love/Notify-Sample

import requests

class Maguro():
    def __init__(self):
        # Line-Notify token
        self.token = ""
        
        self.check_token()

    def main(self) -> None:
        """ write the process here | ここに処理を書く """

        self.sendMessage("hi tuna")

    # send text | 文字送信
    def sendMessage(self, msg: str) -> None:
        """ msg : text | msg : 文字"""
        if not msg:
            raise Exception("plz enter text")
        self.post({"message": msg})

    #　send sticker | スタンプ送信
    def sendSticker(self, pkg_id: str="1", stk_id: str="1", msg: str="sticker") -> None:
        """ pkg_id : package id, stk_id : sticker id, msg : sticker title
            pkg_id : パッケージID, stk_id : スタンプID, msg : スタンプタイトル """
        self.post({"message": msg, "stickerPackageId": pkg_id, "stickerId": stk_id})

    # send image | 画像送信
    def sendImage(self, path: str, msg: str="image") -> None:
        """ path : image path, msg : image title
            path : 画像パス,    msg : 画像タイトル """
        if not path:
            raise Exception("plz enter path")
        self.post({"message": msg}, {"imageFile": open(path, "rb")})

    # send url-image | URLの画像を送信
    def sendImageWithURL(self, url: str, msg: str="image") -> None:
        """ url : image url, msg : image title
            url : 画像URL     msg : 画像タイトル """
        if not url:
            raise Exception("plz enter url")
        with open("tmp.jpg", "wb") as f:
            f.write(requests.get(url).content)
        self.post({"message": msg}, {"imageFile": open("tmp.jpg", "rb")})

    # Don't rewrite if u r not understand :(
    def check_token(self) -> None:
        """ check if the token is valid """
        r = requests.get(
            url="https://notify-api.line.me/api/status",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        if r.status_code != 200:
            raise Exception("invalid token")

    # Don't rewrite if u r not understand :(
    def revoke_token(self) -> None:
        """ deactivate token """
        r = requests.post(
            url="https://notify-api.line.me/api/revoke",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        if r.status_code != 200:
            raise Exception("invalid token")

    # Don't rewrite if u r not understand :(
    def post(self, payload: dict, files: dict={}) -> None:
        """ request """
        r = requests.post(
            url="https://notify-api.line.me/api/notify",
            headers={"Authorization": f"Bearer {self.token}"},
            params=payload,
            files=files
        )
        if r.status_code != 200:
            raise Exception("some error has occurred :(")

if __name__ == "__main__":
    Maguro().main()
