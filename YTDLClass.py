import pytube
import threading

class YTDL:
    def __init__(self):
        return
    
    def set_pb(self, pb, tx):
        self.pb = pb
        self.tx = tx
    
    def set_url(self, s:str):
        self.yt = pytube.YouTube(s)
        threading.Thread(target=self.yt.register_on_progress_callback, args=[self.on_download_progress]).start()
        threading.Thread(target=self.yt.register_on_complete_callback, args=[self.on_complete]).start()
        self.st = self.yt.streams
        
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
    
    def download(self, id):
        if (len(self.st.all()) <= id):
            return 1
        self.tx.SetLabel(u"Download in progress")
        self.tx.GetParent().Layout()
        t = self.st.all()[id]
        self.done = 0
        self.all = -1
        t.download()
        return 0
    
    def on_download_progress(self, stream, chunk, file_handler, bytes_remaining):
        if self.all == -1:
            self.all = bytes_remaining
        print(100 * self.done / self.all)
        self.done = self.all - bytes_remaining
        self.pb.SetValue(self.done/self.all * 100)        
    
    def on_complete(self, stream, file_handler):
        self.tx.SetLabel(u"Download complete")
        self.tx.GetParent().Layout()
        self.pb.SetValue(0)
        print("Download complete")
        return