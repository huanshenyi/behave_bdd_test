

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # ページを開く
    def get_url(self, url):
        self.driver.get(url)

    # title取得
    def get_title(self):
        return self.driver.title

    # 要素を特定
    def find_element(self, *loc):
        # ここでconfigファイル読み込みの方法定義してもよい
        return self.driver.find_element(*loc)