import subprocess
class CE:
    def __init__(self, p):
        self.e = subprocess.Popen([p],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        self._i()
    def _i(self):
        self._s("uci")
        while True:
            o = self._r()
            if o == "uciok": break
        self._s("setoption name Hash value 1")
        self._s("setoption name ContemptDrawPenalty value 0")
        self._s("setoption name ContemptComplexity value 0")
    def _s(self, command):
        self.e.stdin.write(command + "\n")
        self.e.stdin.flush()
    def _r(self):
        o = self.e.stdout.readline().strip()
        return o
    def g(self, fen, m=160):
        self._s(f"position fen {fen}")
        self._s(f"go movetime {m}")
        b = None
        while True:
            o = self._r()
            if o.startswith("bestmove"):
                b = o.split()[1]
                break
        self._s("setoption name Clear Hash")
        return b
    def stop(self):
        self._s("quit")
        self.e.terminate()
        self.e.wait()
u = None
def chess_bot(obs):
    global u
    fen = obs['board']
    p = '/kaggle_simulations/agent/Ethereal' #'/kaggle/working/Ethereal'
    if u is None: u = CE(p)
    b = u.g(fen)
    return b
