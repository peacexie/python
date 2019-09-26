
' vbs打开ie两种方法 在VBScript中启动IE浏览器的实现代码
' http://hant.ask.helplib.com/javascript/post_5938169
' Split("42, 12, 19")

rem imcat,imhouse,
rem start chrome.exe --kiosk http://imcat.txjia.com/
rem http://www.dongguan.net.cn/index.html
rem http://txjia.com/
rem http://qiyeweb.dongguan.net.cn/
rem http://www.pswpower.com


Dim tab,wsh,ie,url

tab = Split("imcat.txjia.com,imblog.txjia.com,ourhouse.txjia.com,wepy.txjia.com,im3n.txjia.com,txjia.com,qiyeweb.dongguan.net.cn,www.pswpower.com", ",")
For i=0 to 7

  Set ie = WScript.CreateObject("InternetExplorer.Application") 
  ie.visible = True 

    'print tab(i)
    'If inStr(".", tab(i))>0 Then
        url = tab(i)
    'Else
        'url = tab(i) & ".txjia.com"
    'End If
    ie.navigate url
    WScript.Sleep 4000

  ie.Quit()

Next

WScript.Sleep 3000
