"""
GUI to independently run the Trading_Bot.py file multiple times for different types of cryptocurrencies.
You need to
1) run the code,
2) fill in the input fields
3) click the "Start" button to run Trading_Bot.py for the currency
4) click the "Stop" button to terminate the trading
"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
import sys, signal
import subprocess


class TradingBotGUI(QWidget):
    def __init__(self):
        super().__init__()
        QWidget.resize(self, 1300, 500)

        # Input fields for the first symbol
        self.symbol_1_label = QLabel('Symbol 1')
        self.symbol_1_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.symbol_1_input = QLineEdit()
        self.s1_amount_label = QLabel('Amount 1')
        self.s1_amount_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.s1_amount_input = QLineEdit()
        self.s1_interval_label = QLabel('Interval 1')
        self.s1_interval_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.s1_interval_input = QLineEdit()
        self.s1_a_label = QLabel('a1')
        self.s1_a_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s1_a_input = QLineEdit()
        self.s1_b_label = QLabel('b1')
        self.s1_b_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s1_b_input = QLineEdit()
        self.s1_c_label = QLabel('c1')
        self.s1_c_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s1_c_input = QLineEdit()
        self.s1_d_label = QLabel('d1')
        self.s1_d_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s1_d_input = QLineEdit()
        self.s1_enable_label = QLabel('1enable/disable')
        self.s1_enable_label.setStyleSheet('font-size: 12px; font-weight: bold')
        self.s1_enablebtn = QPushButton('Start 1')
        self.s1_disablebtn = QPushButton('Stop 1')


        # Input fields for the second symbol
        self.symbol_2_label = QLabel('Symbol 2')
        self.symbol_2_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.symbol_2_input = QLineEdit()
        self.s2_amount_label = QLabel('Amount 2')
        self.s2_amount_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.s2_amount_input = QLineEdit()
        self.s2_interval_label = QLabel('Interval 2')
        self.s2_interval_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.s2_interval_input = QLineEdit()
        self.s2_a_label = QLabel('a2')
        self.s2_a_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s2_a_input = QLineEdit()
        self.s2_b_label = QLabel('b2')
        self.s2_b_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s2_b_input = QLineEdit()
        self.s2_c_label = QLabel('c2')
        self.s2_c_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s2_c_input = QLineEdit()
        self.s2_d_label = QLabel('d2')
        self.s2_d_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s2_d_input = QLineEdit()
        self.s2_enable_label = QLabel('2enable/disable')
        self.s2_enable_label.setStyleSheet('font-size: 12px; font-weight: bold')
        self.s2_enablebtn = QPushButton('Start 2')
        self.s2_disablebtn = QPushButton('Stop 2')

        # Input fields for the third symbol
        self.symbol_3_label = QLabel('Symbol 3')
        self.symbol_3_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.symbol_3_input = QLineEdit()
        self.s3_amount_label = QLabel('Amount 3')
        self.s3_amount_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.s3_amount_input = QLineEdit()
        self.s3_interval_label = QLabel('Interval 3')
        self.s3_interval_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.s3_interval_input = QLineEdit()
        self.s3_a_label = QLabel('a3')
        self.s3_a_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s3_a_input = QLineEdit()
        self.s3_b_label = QLabel('b3')
        self.s3_b_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s3_b_input = QLineEdit()
        self.s3_c_label = QLabel('c3')
        self.s3_c_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s3_c_input = QLineEdit()
        self.s3_d_label = QLabel('d3')
        self.s3_d_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s3_d_input = QLineEdit()
        self.s3_enable_label = QLabel('3enable/disable')
        self.s3_enable_label.setStyleSheet('font-size: 12px; font-weight: bold')
        self.s3_enablebtn = QPushButton('Start 3')
        self.s3_disablebtn = QPushButton('Stop 3')

        # Input fields for the forth symbol
        self.symbol_4_label = QLabel('Symbol 4')
        self.symbol_4_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.symbol_4_input = QLineEdit()
        self.s4_amount_label = QLabel('Amount 4')
        self.s4_amount_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.s4_amount_input = QLineEdit()
        self.s4_interval_label = QLabel('Interval 4')
        self.s4_interval_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.s4_interval_input = QLineEdit()
        self.s4_a_label = QLabel('a4')
        self.s4_a_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s4_a_input = QLineEdit()
        self.s4_b_label = QLabel('b4')
        self.s4_b_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s4_b_input = QLineEdit()
        self.s4_c_label = QLabel('c4')
        self.s4_c_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s4_c_input = QLineEdit()
        self.s4_d_label = QLabel('d4')
        self.s4_d_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s4_d_input = QLineEdit()
        self.s4_enable_label = QLabel('4enable/disable')
        self.s4_enable_label.setStyleSheet('font-size: 12px; font-weight: bold')
        self.s4_enablebtn = QPushButton('Start 4')
        self.s4_disablebtn = QPushButton('Stop 4')

        # Input fields for the fifth symbol
        self.symbol_5_label = QLabel('Symbol 5')
        self.symbol_5_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.symbol_5_input = QLineEdit()
        self.s5_amount_label = QLabel('Amount 5')
        self.s5_amount_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.s5_amount_input = QLineEdit()
        self.s5_interval_label = QLabel('Interval 5')
        self.s5_interval_label.setStyleSheet('font-size: 13px; font-weight: bold')
        self.s5_interval_input = QLineEdit()
        self.s5_a_label = QLabel('a5')
        self.s5_a_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s5_a_input = QLineEdit()
        self.s5_b_label = QLabel('b5')
        self.s5_b_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s5_b_input = QLineEdit()
        self.s5_c_label = QLabel('c5')
        self.s5_c_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s5_c_input = QLineEdit()
        self.s5_d_label = QLabel('d5')
        self.s5_d_label.setStyleSheet('font-size: 14px; font-weight: bold')
        self.s5_d_input = QLineEdit()
        self.s5_enable_label = QLabel('5enable/disable')
        self.s5_enable_label.setStyleSheet('font-size: 12px; font-weight: bold')
        self.s5_enablebtn = QPushButton('Start 5')
        self.s5_disablebtn = QPushButton('Stop 5')

        # enable and disable buttons
        self.s1_enablebtn.clicked.connect(lambda: self.start_bot(1))
        self.s1_disablebtn.clicked.connect(lambda: self.stop_bot(1))

        self.s2_enablebtn.clicked.connect(lambda: self.start_bot(2))
        self.s2_disablebtn.clicked.connect(lambda: self.stop_bot(2))

        self.s3_enablebtn.clicked.connect(lambda: self.start_bot(3))
        self.s3_disablebtn.clicked.connect(lambda: self.stop_bot(3))

        self.s4_enablebtn.clicked.connect(lambda: self.start_bot(4))
        self.s4_disablebtn.clicked.connect(lambda: self.stop_bot(4))

        self.s5_enablebtn.clicked.connect(lambda: self.start_bot(5))
        self.s5_disablebtn.clicked.connect(lambda: self.stop_bot(5))

        # Layouts
        s1_layout = QHBoxLayout()
        s1_layout.addWidget(self.symbol_1_label)
        s1_layout.addWidget(self.s1_amount_label)
        s1_layout.addWidget(self.s1_interval_label)
        s1_layout.addWidget(self.s1_a_label)
        s1_layout.addWidget(self.s1_b_label)
        s1_layout.addWidget(self.s1_c_label)
        s1_layout.addWidget(self.s1_d_label)
        s1_layout.addWidget(self.s1_enable_label)

        s1_input = QHBoxLayout()
        s1_input.addWidget(self.symbol_1_input)
        s1_input.addWidget(self.s1_amount_input)
        s1_input.addWidget(self.s1_interval_input)
        s1_input.addWidget(self.s1_a_input)
        s1_input.addWidget(self.s1_b_input)
        s1_input.addWidget(self.s1_c_input)
        s1_input.addWidget(self.s1_d_input)
        s1_input.addWidget(self.s1_enablebtn)
        s1_input.addWidget(self.s1_disablebtn)

        s2_layout = QHBoxLayout()
        s2_layout.addWidget(self.symbol_2_label)
        s2_layout.addWidget(self.s2_amount_label)
        s2_layout.addWidget(self.s2_interval_label)
        s2_layout.addWidget(self.s2_a_label)
        s2_layout.addWidget(self.s2_b_label)
        s2_layout.addWidget(self.s2_c_label)
        s2_layout.addWidget(self.s2_d_label)
        s2_layout.addWidget(self.s2_enable_label)

        s2_input = QHBoxLayout()
        s2_input.addWidget(self.symbol_2_input)
        s2_input.addWidget(self.s2_amount_input)
        s2_input.addWidget(self.s2_interval_input)
        s2_input.addWidget(self.s2_a_input)
        s2_input.addWidget(self.s2_b_input)
        s2_input.addWidget(self.s2_c_input)
        s2_input.addWidget(self.s2_d_input)
        s2_input.addWidget(self.s2_enablebtn)
        s2_input.addWidget(self.s2_disablebtn)

        s3_layout = QHBoxLayout()
        s3_layout.addWidget(self.symbol_3_label)
        s3_layout.addWidget(self.s3_amount_label)
        s3_layout.addWidget(self.s3_interval_label)
        s3_layout.addWidget(self.s3_a_label)
        s3_layout.addWidget(self.s3_b_label)
        s3_layout.addWidget(self.s3_c_label)
        s3_layout.addWidget(self.s3_d_label)
        s3_layout.addWidget(self.s3_enable_label)

        s3_input = QHBoxLayout()
        s3_input.addWidget(self.symbol_3_input)
        s3_input.addWidget(self.s3_amount_input)
        s3_input.addWidget(self.s3_interval_input)
        s3_input.addWidget(self.s3_a_input)
        s3_input.addWidget(self.s3_b_input)
        s3_input.addWidget(self.s3_c_input)
        s3_input.addWidget(self.s3_d_input)
        s3_input.addWidget(self.s3_enablebtn)
        s3_input.addWidget(self.s3_disablebtn)

        s4_layout = QHBoxLayout()
        s4_layout.addWidget(self.symbol_4_label)
        s4_layout.addWidget(self.s4_amount_label)
        s4_layout.addWidget(self.s4_interval_label)
        s4_layout.addWidget(self.s4_a_label)
        s4_layout.addWidget(self.s4_b_label)
        s4_layout.addWidget(self.s4_c_label)
        s4_layout.addWidget(self.s4_d_label)
        s4_layout.addWidget(self.s4_enable_label)

        s4_input = QHBoxLayout()
        s4_input.addWidget(self.symbol_4_input)
        s4_input.addWidget(self.s4_amount_input)
        s4_input.addWidget(self.s4_interval_input)
        s4_input.addWidget(self.s4_a_input)
        s4_input.addWidget(self.s4_b_input)
        s4_input.addWidget(self.s4_c_input)
        s4_input.addWidget(self.s4_d_input)
        s4_input.addWidget(self.s4_enablebtn)
        s4_input.addWidget(self.s4_disablebtn)

        s5_layout = QHBoxLayout()
        s5_layout.addWidget(self.symbol_5_label)
        s5_layout.addWidget(self.s5_amount_label)
        s5_layout.addWidget(self.s5_interval_label)
        s5_layout.addWidget(self.s5_a_label)
        s5_layout.addWidget(self.s5_b_label)
        s5_layout.addWidget(self.s5_c_label)
        s5_layout.addWidget(self.s5_d_label)
        s5_layout.addWidget(self.s5_enable_label)

        s5_input = QHBoxLayout()
        s5_input.addWidget(self.symbol_5_input)
        s5_input.addWidget(self.s5_amount_input)
        s5_input.addWidget(self.s5_interval_input)
        s5_input.addWidget(self.s5_a_input)
        s5_input.addWidget(self.s5_b_input)
        s5_input.addWidget(self.s5_c_input)
        s5_input.addWidget(self.s5_d_input)
        s5_input.addWidget(self.s5_enablebtn)
        s5_input.addWidget(self.s5_disablebtn)

        main_layout = QVBoxLayout()
        main_layout.addLayout(s1_layout)
        main_layout.addLayout(s1_input)
        main_layout.addLayout(s2_layout)
        main_layout.addLayout(s2_input)
        main_layout.addLayout(s3_layout)
        main_layout.addLayout(s3_input)
        main_layout.addLayout(s4_layout)
        main_layout.addLayout(s4_input)
        main_layout.addLayout(s5_layout)
        main_layout.addLayout(s5_input)

        self.setLayout(main_layout)

    # function to run the trading bot
    def start_bot(self, bot_id):
        script_path = 'Trading_Bot.py'
        if bot_id == 1:
            symbol = self.symbol_1_input.text()
            amount = self.s1_amount_input.text()
            interval = self.s1_interval_input.text()
            a1 = self.s1_a_input.text()
            b1 = self.s1_b_input.text()
            c1 = self.s1_c_input.text()
            d1 = self.s1_d_input.text()
            self.process_1 = subprocess.Popen(['python', script_path, symbol, interval, amount, a1, b1, c1, d1])
            self.process_1.pid

        elif bot_id == 2:
            symbol = self.symbol_2_input.text()
            amount = self.s2_amount_input.text()
            interval = self.s2_interval_input.text()
            a2 = self.s2_a_input.text()
            b2 = self.s2_b_input.text()
            c2 = self.s2_c_input.text()
            d2 = self.s2_d_input.text()
            self.process_2 = subprocess.Popen(['python', script_path, symbol, interval, amount, a2, b2, c2, d2])
            self.process_2.pid

        elif bot_id == 3:
            symbol = self.symbol_3_input.text()
            amount = self.s3_amount_input.text()
            interval = self.s3_interval_input.text()
            a3 = self.s3_a_input.text()
            b3 = self.s3_b_input.text()
            c3 = self.s3_c_input.text()
            d3 = self.s3_d_input.text()
            self.process_3 = subprocess.Popen(['python', script_path, symbol, interval, amount, a3, b3, c3, d3])
            self.process_3.pid

        elif bot_id == 4:
            symbol = self.symbol_4_input.text()
            amount = self.s4_amount_input.text()
            interval = self.s4_interval_input.text()
            a4 = self.s4_a_input.text()
            b4 = self.s4_b_input.text()
            c4 = self.s4_c_input.text()
            d4 = self.s4_d_input.text()
            self.process_4 = subprocess.Popen(['python', script_path, symbol, interval, amount, a4, b4, c4, d4])
            self.process_4.pid

        elif bot_id == 5:
            symbol = self.symbol_5_input.text()
            amount = self.s5_amount_input.text()
            interval = self.s5_interval_input.text()
            a5 = self.s5_a_input.text()
            b5 = self.s5_b_input.text()
            c5 = self.s5_c_input.text()
            d5 = self.s5_d_input.text()
            self.process_5 = subprocess.Popen(['python', script_path, symbol, interval, amount, a5, b5, c5, d5])
            self.process_5.pid

    # function to stop the bot
    def stop_bot(self, bot_id):
        if bot_id == 1:
            symbol = self.symbol_1_input.text()
            self.process_1.send_signal(signal.SIGTERM)
            print(f'\nBot process stopped for {symbol.upper()}')

        elif bot_id == 2:
            symbol = self.symbol_2_input.text()
            self.process_2.send_signal(signal.SIGTERM)
            print(f'\nBot process stopped for {symbol.upper()}')

        elif bot_id == 3:
            symbol = self.symbol_3_input.text()
            self.process_3.send_signal(signal.SIGTERM)
            print(f'\nBot process stopped for {symbol.upper()}')

        elif bot_id == 4:
            symbol = self.symbol_4_input.text()
            self.process_4.send_signal(signal.SIGTERM)
            print(f'\nBot process stopped for {symbol.upper()}')

        elif bot_id == 5:
            symbol = self.symbol_5_input.text()
            self.process_5.send_signal(signal.SIGTERM)
            print(f'\nBot process stopped for {symbol.upper()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    gui = TradingBotGUI()
    gui.show()
    sys.exit(app.exec_())
