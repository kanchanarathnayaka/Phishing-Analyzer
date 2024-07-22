import base64
import requests

api_key = ""

url = "https://3.skysky.workers.dev/#/login"
html = """
<!DOCTYPE html><html lang="en" manifest="webogram.appcache" ng-csp="" xmlns:ng="http://angularjs.org" id="ng-app" style="display: block; background: rgb(231, 235, 240);"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"><title>Telegram Web</title><link rel="stylesheet" href="css/app.css"><link rel="manifest" href="manifest.webapp.json"><link rel="shortcut icon" type="image/x-icon" href="favicon.ico"><link rel="apple-touch-icon" href="img/iphone_home120.png"><link rel="apple-touch-icon" sizes="120x120" href="img/iphone_home120.png"><link rel="apple-touch-startup-image" media="(device-width: 320px)" href="img/iphone_startup.png"><meta name="apple-mobile-web-app-title" content="Telegram Web"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"><meta name="theme-color" content="#497495"><meta name="google" content="notranslate"><meta property="og:title" content="Telegram Web"><meta property="og:url" content="https://web.telegram.org/"><meta property="og:image:width" content="236"><meta property="og:image:height" content="236"><meta property="og:image" content="https://web.telegram.org/img/logo_share.png"><meta property="og:site_name" content="Telegram Web"><meta property="description" content="Access your Telegram messages from any mobile or desktop device."><meta property="og:description" content="Access your Telegram messages from any mobile or desktop device."><link rel="stylesheet" href="css/desktop.css"><style type="text/css">ogvjs { display: inline-block; position: relative; -webkit-user-select: none; -webkit-tap-highlight-color: rgba(0,0,0,0); </style></head><body class="non_osx non_msie is_1x"><!----><div class="page_wrap" ng-view=""><div class="login_page_wrap" my-custom-background="#e7ebf0">  <!----><div class="login_try_desktop" ng-if="try_desktop.shown">    <span class="try_desktop_close" ng-click="closeTryDesktop()"></span>    <p class="try_desktop_text" my-i18n="login_try_desktop">For best experience on your computer, try <my-i18n-param name="telegram-link"><a href="https://desktop.telegram.org/" target="_blank">desktop.telegram.org</a></my-i18n-param></p>    <a class="try_desktop_btn" href="https://desktop.telegram.org/" target="_blank" my-i18n="login_try_desktop_btn">Download Telegram</a>  </div><!---->  <div class="login_head_bg"></div>  <div class="login_page">    <div class="login_head_wrap clearfix" ng-switch="progress.enabled">      <!---->      <!----><div ng-switch-default="" class="login_head_submit_wrap">        <!----><a class="login_head_submit_btn" ng-if="!credentials.phone_code_hash" ng-click="sendCode()">          <my-i18n msgid="modal_next">Next</my-i18n><i class="icon icon-next-submit"></i>        </a><!---->        <!---->        <!---->        <!---->      </div><!---->      <a class="login_head_logo_link" href="https://telegram.org" target="_blank">        <i class="icon icon-tg-logo"></i><i class="icon icon-tg-title"></i>      </a>    </div>    <div class="login_form_wrap">      <!---->      <!----><form name="mySendCodeForm" ng-if="!credentials.phone_code_hash" ng-submit="sendCode()" class="ng-pristine ng-invalid ng-invalid-required">        <h3 class="login_form_head" my-i18n="login_sign_in">Sign in</h3>        <p class="login_form_lead" my-i18n="login_enter_number_description_md">Please choose your country and enter your full phone number.<br><br>Note that you need an existing account to log in to Telegram Web. To sign up for Telegram, use one of our <my-i18n-param name="apps-link"><!--            --><a href="https://telegram.org/apps" target="_blank">mobile apps</a><!--          --></my-i18n-param>.</p>        <div class="md-input-group md-input-has-value login_phone_country_input_group" ng-click="chooseCountry()">          <label class="md-input-label" my-i18n="login_country_select_placeholder">Country</label>          <div autocomplete="off" class="md-input" ng-bind="credentials.phone_country_name">United States</div>        </div>        <div class="login_phone_groups_wrap clearfix">          <div class="md-input-group login_phone_code_input_group md-input-has-value md-input-animated md-input-focused" ng-class="{'md-input-error': error.field == 'phone'}" my-labeled-input="">            <label class="md-input-label" my-i18n="login_code_input_placeholder">Code</label>            <input autocomplete="off" class="md-input ng-pristine ng-untouched ng-valid ng-not-empty" my-focused="" name="phone_country" type="tel" ng-model="credentials.phone_country">          </div>          <div class="md-input-group login_phone_num_input_group md-input-animated" ng-class="{'md-input-error': error.field == 'phone'}" my-labeled-input="" ng-switch="error.field == 'phone'">            <!---->            <!----><label ng-switch-default="" class="md-input-label" my-i18n="login_tel_input_placeholder">Phone number</label><!---->            <input required="" autocomplete="off" my-submit-on-enter="" class="md-input ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required" my-focus-on="country_selected" name="phone_number" type="tel" ng-model="credentials.phone_number">          </div>        </div>        <div class="login_form_messaging ng-hide" ng-show="progress.enabled" my-i18n="login_generating_keys_info">Keys are only generated once. This can take a few minutes on slower devices, please be patient.</div>      </form><!---->      <!---->      <!---->      <!---->    </div>    <div ng-switch="about.shown">      <!---->      <!----><div ng-switch-default="" class="login_footer_wrap">        <p my-i18n="login_about_intro">Welcome to the official Telegram web-client.</p>        <a class="logo_footer_learn_more_link" href="" ng-click="about.shown = true" my-i18n="login_about_learn">Learn more</a>      </div><!---->    </div>  </div></div></div><div id="notify_sound"></div><script src="js/app.js"></script></body></html>
"""
text = """
Telegram Web For best experience on your computer, try desktop.telegram.org Download Telegram Next Sign in Please choose your country and enter your full phone number. Note that you need an existing account to log in to Telegram Web. To sign up for Telegram, use one of our mobile apps . Country United States Code Phone number Keys are only generated once. This can take a few minutes on slower devices, please be patient. Welcome to the official Telegram web-client. Learn more
"""
# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "path_to_your_image.jpg"

# Getting the base64 string
# base64_image = encode_image(image_path)
image_url = "https://lh3.googleusercontent.com/u/1/drive-viewer/AKGpihawXhDX8erXaTyKOEpW_dMgCW3UzDfrO4_0O76vvTDrWBj4aZaKCjh6BWaeF1yAlpZslPDMPUv1sZWxma3gpem8cpFvFBr_iQ=w1008-h912"


headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"""
        You are a Security Analyst and security expert tasked
        with examining a web page to determine if it is a
        phishing site or a legitimate site. To complete this
        task, follow these sub-tasks:
        1. Analyze the HTML, URL, and extracted text
        screenshot image will be encoded in base 64, Decode it and look for any SE techniques often used in
        phishing attacks. Point out any suspicious elements
        found in the HTML, URL, or text.
        2. Identify the brand name. If the HTML appears to
        resemble a legitimate web page, verify if the URL
        matches the legitimate domain name associated with
        the brand, if known.
        3. State your conclusion on whether the site is a
        phishing site or a legitimate one, and explain your
        reasoning. If there is insufficient evidence to make
        a determination, answer "unknown".
        4. Submit your findings as JSON-formatted output with
        the following keys:
        phishing_score: int (indicates phishing risk on a
        scale of 0 to 10)
        brands: str (identified brand name or None if not
        applicable)
        phishing: boolean (whether the site is a phishing
        site or a legitimate site)
        suspicious_domain: boolean (whether the domain name
        is suspected to be not legitimate)
        Limitations:
        The HTML may be shortened and simplified.
        The OCR-extracted text may not always be accurate.
        Examples of social engineering techniques:
        Alerting the user to a problem with their account
        Offering unexpected rewards
        Informing the user of a missing package or additional
        payment required
        Displaying fake security warnings
        URL:
        {url}
        HTML:{html}Text extracted using OCR:{text}Screen Shot image (Base 64 encoded):
          """
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"{image_url}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print(response.json())
