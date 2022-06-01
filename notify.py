# this program was created by MaguRo

from requests import Response
import requests

# Don't rewrite if u r not understand :(
class Maguro():
    def __init__(self, token):
        self.token = token
        self.check_token()


    def sendMessage(self, msg: str, silent: bool=False) -> None:
        """Send text | テキスト送信

        Args:
            msg: Text to be sent | 送信するテキスト
            silent: Push notification when sending messages or not | メッセージ送信時のプッシュ通知有無

        Returns:
            None
        """
        if not msg:
            raise ValueError("plz enter text")
        self._post({"message": msg, "notificationDisabled": silent})


    def sendSticker(self, pkg_id: str="1", stk_id: str="1", msg: str="sticker", silent: bool=False) -> None:
        """Send sticker | スタンプ送信

        Args:
            pkg_id: Sticker Package ID | スタンプのパッケージID
            stk_id: Sticker  ID | スタンプID
            msg: Text to be sent | 送信するテキスト
            silent: Push notification when sending messages or not | メッセージ送信時のプッシュ通知有無

        Returns:
            None
        """
        self._post({"message": msg, "stickerPackageId": pkg_id, "stickerId": stk_id, "notificationDisabled": silent})


    def sendImage(self, path: str, msg: str="image", silent: bool=False) -> None:
        """Send image | 画像送信

        Args:
            path: Image path
            msg: Text to be sent | 送信するテキスト
            silent: Push notification when sending messages or not | メッセージ送信時のプッシュ通知有無

        Returns:
            None
        """
        if not path:
            raise ValueError("plz enter path")
        self._post({"message": msg, "notificationDisabled": silent}, {"imageFile": open(path, "rb")})


    def sendImageWithURL(self, url: str, msg: str="image", silent: bool=False) -> None:
        """Send url image | URLの画像送信

        Args:
            url: Image url
            msg: Text to be sent | 送信するテキスト
            silent: Push notification when sending messages or not | メッセージ送信時のプッシュ通知有無

        Returns:
            None
        """
        if not url:
            raise ValueError("plz enter url")
        with open("tmp.jpg", "wb") as f:
            f.write(requests.get(url).content)
        self._post({"message": msg, "notificationDisabled": silent}, {"imageFile": open("tmp.jpg", "rb")})


    def check_token(self) -> Response:
        """Check if the token is valid | トークンが有効か確認

        Args:
            None

        Returns:
            Request result | リクエスト結果
        """
        r = requests.get(
            url="https://notify-api.line.me/api/status",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        if r.status_code != 200:
            raise Exception("invalid token")
        return r

    def revoke_token(self) -> Response:
        """Deactivate token | トークン無効化

        Args:
            None

        Returns:
            Request result | リクエスト結果
        """
        r = requests.post(
            url="https://notify-api.line.me/api/revoke",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        if r.status_code != 200:
            raise Exception("invalid token")
        return r

    def _post(self, payload: dict, files: dict={}) -> Response:
        """Send request | URLの画像を送る

        Args:
            payload: payload
            files: files

        Returns:
            Request result | リクエスト結果
        """
        r = requests.post(
            url="https://notify-api.line.me/api/notify",
            headers={"Authorization": f"Bearer {self.token}"},
            params=payload,
            files=files
        )
        if r.status_code != 200:
            raise Exception("some error has occurred :(")
        return r
