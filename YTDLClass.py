import pytube
import threading
import sys

class YTDL:
    def __init__(self):
        self.diff = 1
        return
    
    def set_parent(self, par):
        self.par = par
    
    def set_url(self, s:str):
        self.yt = pytube.YouTube(s)
        #threading.Thread(target=self.yt.register_on_progress_callback, args=[self.on_download_progress]).start()
        #threading.Thread(target=self.yt.register_on_complete_callback, args=[self.on_complete]).start()
        self.yt.register_on_progress_callback(self.on_download_progress)
        self.yt.register_on_complete_callback(self.on_complete)
        #self.st = self.yt.streams.filter(progressive=True)
        
    def set_filters(self, fil:dict):
        ### Supported filters are : [""]
        self.reset_filters()
        for i in fil:
            if (fil[i] == "any"):
                continue
            if (i == "mime_type"):
                self.st = self.st.filter(mime_type=fil[i])
            if (i == "res"):
                self.st = self.st.filter(res=fil[i])
            if (i == "fps"):
                self.st = self.st.filter(fps=int(fil[i]))
            if (i == "vcodec"):
                self.st = self.st.filter(video_codec=fil[i])
    
    def get_streams_list(self):
        return self.st.all()
    
    def reset_filters(self):
        self.st = self.yt.streams
        #filter(progressive=True)
    
    def download(self, id):
        self.per = 0
        if (len(self.st.all()) <= id):
            return 1
        #self.par.tx.SetLabel("0%")
        #self.par.Fit()
        #self.par.Refresh()
        #self.par.Update()        
        #self.par.tx.GetParent().Layout()
        t = self.st.all()[id]
        self.done = 0
        self.all = -1
        self.last = "0%"
        t.download()
        #print("download finished")
        #self.par.PrtPb()
        return 0
    
    def rep_prt(self, s):
        for i in range(len(self.last)):
            print(chr(8), end="")
        #print("\8" * len(self.last), end="")
        print(s, end="")
        self.last = s
        sys.stdout.flush()
    
    def on_download_progress(self, stream, chunk, file_handler, bytes_remaining):
        if self.all == -1:
            self.all = bytes_remaining
        #print(100 * self.done / self.all, self.per)
        self.done = self.all - bytes_remaining
        if (self.done / self.all * 100 - self.per >= self.diff):
            #self.par.pb.SetValue(self.done/self.all * 100)  
            self.per = int(self.done / self.all * 100) 
            self.rep_prt(str(self.per) + "%")            
            #self.par.tx.SetLabel(str(self.per)+"%")
            #self.par.pb.GetParent().Layout()
            #self.pb.GetParent().GetParent().Refresh()
            #self.pb.GetParent().GetParent().Update()
            #self.par.Fit()
            #self.par.Refresh()
            #self.par.Update()
    
    def on_complete(self, stream, file_handler):
        #self.par.tx.SetLabel("Download complete")
        #self.par.tx.GetParent().Fit()
        #self.par.pb.SetValue(0)
        #self.par.Refresh()
        print("Download complete")
        return
