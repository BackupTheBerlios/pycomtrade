#
# pyComtrade: A python Class for read and write IEEE
#             Comtrade files.
#
#
# OBS: - The field names ara iqual to Comtrade 1999 stantard;
#
# Developed by Miguel Moreto
# Federal University of Santa Catarina
# Brazil - 2007
#
#

class pyComtrade:
    """ A python Class for read and write IEEE Comtrade files. """
    filename = ''
    filehandler = 0
    # Station name, identification and revision year:
    station_name = ''
    rec_dev_id = ''
    rev_year = 0000
    # Number and type of channels:
    TT = 0
    A = 0 # Number of analog channels.
    D = 0 # Number of digital channels.
    # Analog channel information:
    An = []
    Ach_id = []
    Aph = []
    Accbm = []
    uu = []
    a = []
    b = []
    skew = []
    min = []
    max = []
    primary = []
    secondary = []
    PS = []
    # Digital channel information:
    Dn = []
    Dch_id = []
    Dph = []
    Dccbm = []
    y = []
    # Line frequency:
    lf = 0
    # Sampling rate information:
    nrates = 0
    samp = []
    endsamp = []
    # Date/time stamps:
    #    difined by: [dd,mm,yyyy,hh,mm,ss.ssssss]
    start = [00,00,0000,00,00,0.0]
    trigger = [00,00,0000,00,00,0.0]
    # Data file type:
    ft = ''
    # Time stamp multiplication factor:
    timemult = 0.0

    def __init__(self):
        """ pyComtrade constructor, prints a message. """
        print 'pyComtrade instance created!'

    def ReadCFG(self,filename):
        self.filename = filename
        self.filehandler = open(filename,'r')
        # Processing first line:
        line = self.filehandler.readline()
        templist = line.split(',')
        self.station_name = templist[0]
        self.rec_dev_id = templist[1]
        self.rev_year = int(templist[2])

        # Processing second line:
        line = self.filehandler.readline()
        templist = line.split(',')
        self.TT = int(templist[0])
        self.A = int(templist[1][0:2])
        self.D = int(templist[2][0:2])

        # Processing analog channel lines:
        for i in range(self.A):
            line = self.filehandler.readline()
            templist = line.split(',')
            self.An.append(int(templist[0]))
            self.Ach_id.append(templist[1])
            self.Aph.append(templist[2])
            self.Accbm.append(templist[3])
            self.uu.append(templist[4])
            self.a.append(float(templist[5]))
            self.b.append(float(templist[6]))
            self.skew.append(float(templist[7]))
            self.min.append(int(templist[8]))
            self.max.append(int(templist[9]))
            self.primary.append(float(templist[10]))
            self.secondary.append(float(templist[11]))
            self.PS.append(templist[12])


        self.filehandler.close()


teste = pyComtrade()
teste.ReadCFG('2006_12_11_17_07_32.CFG')
