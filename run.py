import wx
import api
import wikipedia
import wolframalpha
import pyttsx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="SolutionBot")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hi, I'm SolutionBot. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

        engine = pyttsx.init()
        engine.say("Welcome, how can I help you today?")
        engine.runAndWait()

    def OnEnter(self, event):
        engine = pyttsx.init()
        input = self.txt.GetValue()
        input = input.lower()

        if input in api.greetings:
	        	engine.say(api.greetings[input])
	        	engine.runAndWait()
       	elif input in api.compliment:
        	engine.say(api.compliment[input])
        	engine.runAndWait()
        elif input in api.profanities:
        	engine.say(api.profanities[input])
        	engine.runAndWait()	
        else:
        	try:      	
	            #wolfram
	            app_id = "6JYVT2-Q96H4QYQJR"
	            client = wolframalpha.Client(app_id)
	            res = client.query(input)
	            answer = next(res.results).text 
	            print answer
	            engine.say("Answer is " + answer)
	            engine.runAndWait()
	           #Wikipidia
	       	except:
	            try:
	                input = input.split(' ')
	                input = ' '.join(input[2:])
	                print wikipedia.summary(input, sentences=3)
	                engine.say("Searched for " + input)
	                engine.runAndWait()
	                print input
	       	    except:
	                engine.say("I don't know the answer to that question, please ask something else.")
	                engine.runAndWait()

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
