import tkinter as tk
from tkinter import font

from l3_interface_adapters.calculator_controller import CalculatorController


class CalculatorView:
    """
    The main view for the calculator, built using Tkinter.

    This is part of the Frameworks & Drivers layer. It is responsible for
    rendering the UI and delegating user actions to the controller.
    """

    def __init__(self, controller: CalculatorController):
        self._controller = controller

        self.window = tk.Tk()
        self.window.title("Clean Architecture Calculator")
        self.window.geometry("400x600")
        self.window.resizable(False, False)
        self.window.configure(bg="white")

        self.display_var = tk.StringVar()

        self._create_widgets()

    def _create_widgets(self):
        # Display
        display_font = font.Font(family="Helvetica", size=72, weight="bold")
        display_label = tk.Label(
            self.window,
            textvariable=self.display_var,
            font=display_font,
            anchor="e",
            bg="#2E2E2E",
            fg="white",
            padx=20,
            pady=20,
        )
        display_label.pack(expand=True, fill="both")

        # Buttons Frame
        buttons_frame = tk.Frame(self.window, bg="white")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        button_layout = [
            ("C", 1, 0),
            ("", 1, 1),
            ("", 1, 2),
            ("÷", 1, 3),
            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),
            ("x", 2, 3),
            ("4", 3, 0),
            ("5", 3, 1),
            ("6", 3, 2),
            ("-", 3, 3),
            ("1", 4, 0),
            ("2", 4, 1),
            ("3", 4, 2),
            ("+", 4, 3),
            ("0", 5, 0, 2),
            (".", 5, 2),
            ("=", 5, 3),
        ]

        for text, row, col, *span in button_layout:
            if not text:
                continue

            button = self._create_button(buttons_frame, text)

            colspan = span[0] if span else 1
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

    def _create_button(self, parent, text):
        btn_font = font.Font(family="Helvetica", size=24, weight="bold")

        # Determine button colors
        if text in "÷x-+=":
            bg_color = "#FF9500"  # Orange for operators
        elif text == "C":
            bg_color = "#D4D4D2"  # Light gray for top controls
        else:
            bg_color = "#505050"  # Dark gray for digits

        fg_color = "black"  # Set all text to black for high contrast

        return tk.Button(
            parent,
            text=text,
            font=btn_font,
            command=lambda t=text: self._on_button_click(t),
            bg=bg_color,
            fg=fg_color,
            relief="flat",
            borderwidth=0,
        )

    def _on_button_click(self, caption: str):
        if caption.isdigit():
            self._controller.handle_digit(caption)
        elif caption == ".":
            self._controller.handle_decimal()
        elif caption == "C":
            self._controller.handle_clear()
        elif caption == "=":
            self._controller.handle_equals()
        else:
            self._controller.handle_operator(caption)

    def start(self):
        self.window.mainloop()
