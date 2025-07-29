from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy


class Design:
    def __init__(self, board):
        self.board = board
        self.apply_styles()
        self.setup_fonts()
        self.setup_layout_spacing()

    # apply styles to the board
    def apply_styles(self):
        self.board.setStyleSheet("""
                QWidget {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                        stop:0 #0f0f23, stop:1 #1a1a2e);
                    color: #f8f9fa;
                    font-family: 'Inter', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    font-size: 16px;
                    font-weight: 500;
                }

                QLabel#botLabel {
                    color: #64ffda;
                    font-weight: 600;
                    text-shadow: 0 0 10px rgba(100, 255, 218, 0.3);
                }

                QLineEdit {
                    background: rgba(255, 255, 255, 0.05);
                    border: 1px solid rgba(100, 255, 218, 0.2);
                    border-radius: 12px;
                    padding: 12px 16px;
                    color: #f8f9fa;
                    font-size: 16px;
                    backdrop-filter: blur(10px);
                    transition: all 0.3s ease;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    white-space: nowrap;
                    qproperty-alignment: 'AlignVCenter | AlignLeft';
                }

            QLineEdit:focus {
                border: 2px solid #64ffda;
                background: rgba(255, 255, 255, 0.08);
                box-shadow: 0 0 20px rgba(100, 255, 218, 0.2);
            }

            QLineEdit:hover {
                border: 1px solid rgba(100, 255, 218, 0.4);
                background: rgba(255, 255, 255, 0.07);
            }

            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #64ffda, stop:1 #4fc3f7);
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
                font-weight: 600;
                color: #0f0f23;
                min-width: 90px;
                font-size: 15px;
                letter-spacing: 0.5px;
            }

            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #4ecdc4, stop:1 #29b6f6);
                transform: translateY(-1px);
                box-shadow: 0 4px 15px rgba(100, 255, 218, 0.3);
            }

            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #26a69a, stop:1 #0288d1);
                transform: translateY(0px);
            }

            QPushButton#cancel {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ff4757, stop:1 #c44569);
                color: #ffffff;
                border: 2px solid #ff3742;
                font-weight: 700;
            }

            QPushButton#cancel:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ff3742, stop:1 #b33951);
                color: #ffffff;
                border: 2px solid #ff2832;
                box-shadow: 0 6px 20px rgba(255, 71, 87, 0.5);
                transform: translateY(-1px);
            }

            QPushButton#cancel:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #e73c4e, stop:1 #a73244);
                transform: translateY(0px);
                box-shadow: 0 2px 8px rgba(255, 71, 87, 0.3);
            }
            
            QScrollArea {
            background: transparent;
            border: none;
            }
        
            QScrollArea > QWidget > QWidget {
                background: transparent;
            }
            
            QLabel#greetingLabel {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(100, 255, 218, 0.7), stop:1 rgba(79, 195, 247, 0.7));
                color: #0f0f23;
                border-radius: 18px 18px 18px 4px;
                padding: 14px 18px;
                margin: 20px 0;
                font-weight: 600;
                font-size: 18px;
                line-height: 1.4;
                box-shadow: 0 4px 15px rgba(100, 255, 218, 0.3);
                border-left: 4px solid #64ffda;
            }
        """)

    def setup_fonts(self):
        # Modern font hierarchy with better typography
        font_label = QFont("Inter", 18, QFont.Weight.DemiBold)
        font_input = QFont("Inter", 14, QFont.Weight.Normal)
        font_buttons = QFont("Inter", 13, QFont.Weight.DemiBold)

        # Enable font smoothing
        font_label.setStyleHint(QFont.StyleHint.System)
        font_input.setStyleHint(QFont.StyleHint.System)
        font_buttons.setStyleHint(QFont.StyleHint.System)

        self.board.label.setFont(font_label)
        self.board.input.setFont(font_input)
        self.board.ok.setFont(font_buttons)
        self.board.cancel.setFont(font_buttons)

    def style_message_label(self, label, sender='bot'):
        label.setWordWrap(True)

        if sender == 'bot':
            label.setStyleSheet("""
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(100, 255, 218, 0.9), stop:1 rgba(79, 195, 247, 0.9));
                color: #0f0f23;
                border-radius: 18px 18px 18px 4px;
                max-width: 800px;
                qproperty-wordWrap: true;
                qproperty-minimumWidth: 300px;
                padding: 12px 16px;
                margin: 8px 8px 8px 16px;
                font-weight: 500;
                font-size: 16px;
                line-height: 1.4;
                box-shadow: 0 2px 10px rgba(100, 255, 218, 0.2);
            """)
            label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        else:
            label.setStyleSheet("""
                background: rgba(255, 255, 255, 0.08);
                color: #f8f9fa;
                max-width: 800px;
                qproperty-wordWrap: true;
                qproperty-minimumWidth: 300px;
                border-radius: 18px 18px 4px 18px;
                padding: 12px 16px;
                margin: 8px 16px 8px 8px;
                font-weight: 600;
                font-size: 16px;
                line-height: 1.4;
                border: 1px solid rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
            """)
            label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

    def setup_layout_spacing(self):
        # Modern spacing with better visual hierarchy
        self.board.layout.setSpacing(20)
        self.board.layout.setContentsMargins(24, 24, 24, 24)
        self.board.messages_layout.setSpacing(6)
        self.board.messages_layout.setContentsMargins(16, 16, 16, 16)

    def add_glassmorphism_effect(self, widget):
        widget.setStyleSheet(widget.styleSheet() + """
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
        """)

    # implement some transitions
    def add_subtle_animation_class(self):
        return """
            transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        """

    # Modern color palette for consistent theming
    def get_theme_colors(self):
        return {
            'primary': '#64ffda',
            'primary_hover': '#4ecdc4',
            'primary_pressed': '#26a69a',
            'secondary': '#4fc3f7',
            'background_primary': '#0f0f23',
            'background_secondary': '#1a1a2e',
            'surface': 'rgba(255, 255, 255, 0.05)',
            'surface_hover': 'rgba(255, 255, 255, 0.08)',
            'text_primary': '#f8f9fa',
            'text_secondary': '#b0bec5',
            'border': 'rgba(255, 255, 255, 0.1)',
            'shadow': 'rgba(100, 255, 218, 0.2)'
        }