
' vbs打开ie两种方法 在VBScript中启动IE浏览器的实现代码
' http://hant.ask.helplib.com/javascript/post_5938169
' Split("42, 12, 19")

rem imcat,imhouse,
rem start chrome.exe --kiosk http://imcat.txjia.com/
rem http://www.dongguan.net.cn/index.html
rem http://txjia.com/
rem http://qiyeweb.dongguan.net.cn/
rem http://www.pswpower.com


Dim tab,wsh,ie 

Set ie = WScript.CreateObject("InternetExplorer.Application") 
ie.visible = True 


tab = Split("imcat,imblog,ourhouse,wepy,im3n,txjia.com,qiyeweb.dongguan.net.cn,www.pswpower.com", ",")
For i=0 to 7
    'print tab(i)
    If inStr(".", tab(i))>0 Then
        url = "http://" & tab(i)
    Else
        url = "http://" & tab(i) & ".txjia.com"
    End If
    ie.navigate tab(i)
    WScript.Sleep 3000
Next

WScript.Sleep 3000
ie.Quit()