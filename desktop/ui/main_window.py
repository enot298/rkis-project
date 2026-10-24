"""Главное окно: меню сверху, навигация слева, рабочая область, строка состояния.

Структура окна соответствует каркасу ДИ (design/mockups/desktop-frame.svg).
"""
import tkinter as tk
from tkinter import messagebox, ttk

import config
from ui.screens.clients import ClientsScreen
from ui.screens.orders import OrdersScreen
from ui.screens.payments import PaymentsScreen

# Порядок разделов в навигации: ключ -> (название, класс экрана)
SCREENS = {
    "orders": ("Заказы", OrdersScreen),
    "clients": ("Клиенты", ClientsScreen),
    "payments": ("Платежи", PaymentsScreen),
}


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(config.APP_TITLE)
        self.geometry(config.WINDOW_SIZE)
        self.minsize(*config.WINDOW_MIN_SIZE)

        self._screens = {}
        self._nav_buttons = {}
        self._status = tk.StringVar(value="Готово")

        self._build_menu()
        self._build_layout()
        self.show_screen("orders")

    # --- построение интерфейса ---

    def _build_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="Выход", command=self.destroy)
        menubar.add_cascade(label="Файл", menu=file_menu)

        sections_menu = tk.Menu(menubar, tearoff=False)
        for key, (label, _cls) in SCREENS.items():
            sections_menu.add_command(label=label, command=lambda k=key: self.show_screen(k))
        menubar.add_cascade(label="Разделы", menu=sections_menu)

        help_menu = tk.Menu(menubar, tearoff=False)
        help_menu.add_command(label="О программе", command=self._show_about)
        menubar.add_cascade(label="Справка", menu=help_menu)

        self.config(menu=menubar)

    def _build_layout(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Левая навигация
        nav = ttk.Frame(self, padding=8)
        nav.grid(row=0, column=0, sticky="ns")
        for key, (label, _cls) in SCREENS.items():
            btn = ttk.Button(nav, text=label, width=18, command=lambda k=key: self.show_screen(k))
            btn.pack(fill="x", pady=2)
            self._nav_buttons[key] = btn

        # Рабочая область: все экраны лежат друг на друге, показывается один
        container = ttk.Frame(self)
        container.grid(row=0, column=1, sticky="nsew")
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        for key, (_label, screen_cls) in SCREENS.items():
            screen = screen_cls(container)
            screen.grid(row=0, column=0, sticky="nsew")
            self._screens[key] = screen

        # Строка состояния
        statusbar = ttk.Frame(self, padding=(8, 4))
        statusbar.grid(row=1, column=0, columnspan=2, sticky="ew")
        ttk.Label(statusbar, textvariable=self._status).pack(side="left")
        ttk.Label(statusbar, text="Сервер: " + config.API_BASE_URL, foreground="#6B7280").pack(side="right")

    # --- поведение ---

    def show_screen(self, key):
        self._screens[key].tkraise()
        self._status.set("Раздел: " + SCREENS[key][0])

    def _show_about(self):
        messagebox.showinfo(
            "О программе",
            "Учёт заказов для малого бизнеса\nДесктоп-клиент (каркас)\nСервер: " + config.API_BASE_URL,
        )
