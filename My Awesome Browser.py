
import sys
# Core Qt classes (signals, slots, URLs, etc.)
from PyQt5.QtCore import *
# Basic GUI widgets (window, buttons, input fields)
from PyQt5.QtWidgets import *
# Web engine for rendering web pages
from PyQt5.QtWebEngineWidgets import *


# Main window class for the browser
class MainWindow(QMainWindow):
    def __init__(self):
        # Initialize the parent QMainWindow class
        super(MainWindow, self).__init__()

        # Create a web browser view
        self.browser = QWebEngineView()
        # Load Google homepage by default
        self.browser.setUrl(QUrl('http://google.com'))

        # Set the browser as the central widget of the window
        self.setCentralWidget(self.browser)

        # Open the window in maximized mode
        self.showMaximized()

        # ---------------- NAVIGATION BAR ----------------
        # Create a toolbar for navigation buttons
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # URL bar (address bar)
        self.url_bar = QLineEdit()
        # When Enter is pressed, navigate to the entered URL
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Update URL bar whenever the browser URL changes
        self.browser.urlChanged.connect(self.update_url)

    # Navigate to the home page
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    # Navigate to the URL typed in the address bar
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    # Update the address bar with the current URL
    def update_url(self, q):
        self.url_bar.setText(q.toString())


# Create the Qt application
app = QApplication(sys.argv)

# Set application name
QApplication.setApplicationName('My Awesome Browser')

# Create and show the main window
window = MainWindow()

# Start the application event loop
app.exec_()
