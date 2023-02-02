class Control:
    def __init__(self, kp, setpt):
        self.kp = kp
        self.setpt = setpt

    def run(self, pos):
        error = self.setpt - pos
        psi = self.kp*error
        return psi

    def set_setpoint(self, setpt_new):
        self.setpt = setpt_new
        return self.setpt

    def set_Kp(self, kp_new):
        self.kp = kp_new
        print('kp is:', self.kp)
        return self.kp
    
if __name__ == '__main__':
    con = Control(4, 180)
    con.set_Kp(5)