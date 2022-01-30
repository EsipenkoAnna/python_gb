import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #переходим на страницу с круизом
    page.goto("https://www.swanhellenic.com/ru/booking/book/490?seats=2", timeout=0)
    #принимаем все куки
    page.get_by_role("button", name="ПРИНЯТЬ").click()
    #находим и кликаем по первой кнопке Выбрать
    page.locator(".button__label").first.click()
    page.wait_for_load_state()
    #пытаемся в попапе выбрать каюту
    page.on("dialog", lambda  dialog: dialog.accept())
    page.evaluate('(() => {window.waitForPrintDialog = new Promise(f => window.print = f);})()')
    page.locator("[g:not(.disabled)]").click()
    page.waitForFunction('window.waitForPrintDialog')



    page.wait_for_load_state()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
