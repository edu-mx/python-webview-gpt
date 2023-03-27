import wx
import wx.html2

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Chat gpt")

        panel = wx.Panel(self, wx.ID_ANY)

        # Criar um rótulo descritivo para o componente wx.html2.WebView
        desc_label = wx.StaticText(panel, wx.ID_ANY, "Painel")
        
        # Criar um componente wx.html2.WebView
        self.webview = wx.html2.WebView.New(panel)
        
        # carregar a url
        self.webview.LoadURL("https://chat.openai.com/chat")

        # Criar um botão para permitir interação com o componente
        button = wx.Button(panel, wx.ID_ANY, "Fechar")

        # Associar evento do botão para fechar a janela
        button.Bind(wx.EVT_BUTTON, self.onClose)

        # Criar um sizer para organizar o componente e o botão
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(desc_label, 0, wx.ALL, 5)
        sizer.Add(self.webview, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(button, 0, wx.ALL, 5)

        # Configurar o sizer para o painel
        panel.SetSizer(sizer)

    def onClose(self, event):
        self.Close()
        exit()

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
