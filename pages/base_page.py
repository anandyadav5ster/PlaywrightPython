class BasePage:

    def __init__(self,page):
        self.page= page

    def open_application(self,url:str):
        self.page.goto(url)

    def get_title(self) -> str :
        return self.page.title()