

IFC VM ассинхронный поток __--__ функция async def read


async def read(self, client):
    # for elem in range(1, self.num+1):
    #     result = await client.read_holding_registers(slave_id=elem, starting_address=0, quantity=1)
    #     print(result)
    # result = []

    for elem in range(len(self.all_signal)):
        # for elem in range(len(self.all_signal)):
        result = await client.read_holding_registers(slave_id=1, starting_address=0, quantity=1)
        print(result[0])

        # self.all_signal[elem].result.emit(str(result[0]))

    # for elem in range(len(self.all_signal)):
    #     self.all_signal[elem].result.emit(str(result[0]))
    #     self.all_signal2[elem].result.emit(str(result[1]))
    #     print(result[0])

    # result.append(  await client.read_holding_registers(slave_id=1, starting_address=0, quantity=1))
    # result.append(  await client.read_holding_registers(slave_id=elem+1, starting_address=0, quantity=1))
    # self.all_signal[elem].emit(str(result[0]))

    # self.all_signal[elem].result.emit(str(result[elem][0]))
    # await asyncio.sleep(0.002)
    # print("    ",result)
    # for elem in range(len(self.all_signal)):
    #     print(result[elem][0])

    # self.all_signal.emit(str( await client.read_holding_registers(slave_id=1, starting_address=0, quantity=10)))





CREP VM ------ отдельныцй потоу для чтения передачи сигнала



class Changer(QtCore.QThread):
    dat1 = QtCore.pyqtSignal(str)
    dat2 = QtCore.pyqtSignal(str)
    dat3 = QtCore.pyqtSignal(str)
    clientRTU = None
    # clientRTU = ModbusTcpClient("127.0.0.1",502)
    SlaveID = None

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

        self.running = False

    text = ['', '', '']

    def run(self):
        self.running = True

        while self.running == True:
            if self.clientRTU:
                try:
                    self.text = self.clientRTU.read_holding_registers \
                        (address=0, count=3, slave=self.SlaveID).registers
                    print(self.text)

                except:

                    self.text = ['', '', '']

            self.dat1.emit(str(self.text[0]))
            self.dat2.emit(str(self.text[1]))
            self.dat3.emit(str(self.text[2]))

            QtCore.QThread.msleep(1000)


ПЕРЕБОР     ВСЕХ ЛАЙАУТОВ С КНОПКАМИ


# for layout in layout_list:
        #     if layout == self.layout_300:
        #         btn = ButtonForPressureSection(elem + 1)
        #         self.list_all_crep[-1].sensors1_lineEdit.textChanged.connect(
        #             lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
        #                 g.show_sensor1_data(g.sensors1_lineEdit)))
        #         # self.list_all_crep[-1].sensors2_lineEdit.textChanged.connect(
        #         #     lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size1(g.show_sensor2_data()))
        #
        #     elif layout == self.layout_400:
        #         btn = ButtonForPressureSection(elem + 1)
        #         self.list_all_crep[-1].sensors2_lineEdit.textChanged.connect(
        #             lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
        #                 g.show_sensor1_data(g.sensors2_lineEdit)))
        #
        #     elif layout == self.layout_100:
        #         btn = ButtonForPressureSection(elem + 1)
        #         self.list_all_crep[-1].CP_lineEdit.textChanged.connect(
        #             lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
        #                 g.show_sensor1_data(g.CP_lineEdit)))
        #
        #     elif layout == self.layout_200:
        #         btn = ButtonForPressureSection(elem + 1)
        #         self.list_all_crep[-1].sensors3_lineEdit.textChanged.connect(
        #             lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
        #                 g.show_sensor1_data(g.sensors3_lineEdit)))
        #     elif layout == self.layout_500:
        #         btn = ButtonForPressureSection(elem + 1)
        #         self.list_all_crep[-1].sensors5_lineEdit.textChanged.connect(
        #             lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
        #                 g.show_sensor1_data(g.sensors5_lineEdit)))
        #     elif layout == self.layout_600:
        #         btn = ButtonForPressureSection(elem + 1)
        #         self.list_all_crep[-1].pozition_lineEdit.textChanged.connect(
        #             lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
        #                 g.show_sensor1_data(g.pozition_lineEdit)))
        #
        #
        #     elif layout == self.layout_700:
        #         btn = ButtonForPressureSection(elem + 1)
        #         self.list_all_crep[-1].sensors4_lineEdit.textChanged.connect(
        #             lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
        #                 g.show_sensor1_data(g.sensors4_lineEdit)))
        #
        #
        #     elif layout == self.layout_800:
        #         btn = ButtonForPressureSection(elem + 1)
        #         self.list_all_crep[-1].prod_lineEdit.textChanged.connect(
        #             lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
        #                 g.show_sensor1_data(g.prod_lineEdit)))
        #
        #
        #     elif layout == self.layout_900:
        #         btn = ButtonForPressureSection(elem + 1)
        #         self.list_all_crep[-1].poper_lineEdit.textChanged.connect(
        #             lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
        #                 g.show_sensor1_data(g.poper_lineEdit)))
        #
        #     elif layout == self.layout_1000:
        #         btn = ButtonForPressureSection(elem + 1)
        #         self.list_all_crep[-1].end_section_lineEdit.textChanged.connect(
        #             lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
        #                 g.show_sensor1_data(g.end_section_lineEdit)))
        #
        #
        #     elif layout == self.layout_1100:
        #         btn = ButtonForPressureSection(elem + 1)
        #         self.list_all_crep[-1].poper_hieght_lineEdit.textChanged.connect(
        #             lambda checked, b=btn, g=self.list_all_crep[-1]: b.change_rectangle_size(
        #                 g.show_sensor1_data(g.poper_hieght_lineEdit)))
        #
        #
        #
        #     else:
        #         btn = ButtonForSection(elem + 1)







