# this program was created by MaguRo

from requests import Response
import requests

# Don't rewrite if u r not understand :(
class Maguro():
    def __init__(self, token):
        self.token = token
        self.check_token()

    # send text | 文字送信
    def sendMessage(self, msg: str) -> None:
        """ msg : text | msg : 文字"""
        if not msg:
            raise ValueError("plz enter text")
        self._post({"message": msg})

    #　send sticker | スタンプ送信
    def sendSticker(self, pkg_id: str="1", stk_id: str="1", msg: str="sticker") -> None:
        """ pkg_id : package id, stk_id : sticker id, msg : sticker title
            pkg_id : パッケージID, stk_id : スタンプID, msg : スタンプタイトル """
        self._post({"message": msg, "stickerPackageId": pkg_id, "stickerId": stk_id})

    # send image | 画像送信
    def sendImage(self, path: str, msg: str="image") -> None:
        """ path : image path, msg : image title
            path : 画像パス,    msg : 画像タイトル """
        if not path:
            raise ValueError("plz enter path")
        self._post({"message": msg}, {"imageFile": open(path, "rb")})

    # send url-image | URLの画像を送信
    def sendImageWithURL(self, url: str, msg: str="image") -> None:
        """ url : image url, msg : image title
            url : 画像URL     msg : 画像タイトル """
        if not url:
            raise ValueError("plz enter url")
        with open("tmp.jpg", "wb") as f:
            f.write(requests.get(url).content)
        self._post({"message": msg}, {"imageFile": open("tmp.jpg", "rb")})

    def check_token(self) -> Response:
        """ check if the token is valid """
        r = requests.get(
            url="https://notify-api.line.me/api/status",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        if r.status_code != 200:
            raise Exception("invalid token")
        return r

    def revoke_token(self) -> Response:
        """ deactivate token """
        r = requests.post(
            url="https://notify-api.line.me/api/revoke",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        if r.status_code != 200:
            raise Exception("invalid token")
        return r

    def _post(self, payload: dict, files: dict={}) -> Response:
        """ request """
        r = requests.post(
            url="https://notify-api.line.me/api/notify",
            headers={"Authorization": f"Bearer {self.token}"},
            params=payload,
            files=files
        )
        if r.status_code != 200:
            raise Exception("some error has occurred :(")
        return r
