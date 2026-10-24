"""Базовый класс экрана-заглушки."""
from tkinter import ttk


class BaseScreen(ttk.Frame):
    """Экран раздела: заголовок и пояснение. Наследники задают title и note."""

    title = "Раздел"
    note = "Раздел в разработке (этап Э8)."

    def __init__(self, parent):
        super().__init__(parent, padding=24)
        ttk.Label(self, text=self.title, font=("TkDefaultFont", 18, "bold")).pack(anchor="w")
        ttk.Label(self, text=self.note, foreground="#6B7280").pack(anchor="w", pady=(8, 0))
