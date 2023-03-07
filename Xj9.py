import threading
import pyautogui
import tkinter as tk
import time
import keyboard


class ClickBotGUI:
    def __init__(self):
        self.is_running = False
        self.is_paused = False
        self.thread = None
        self.total_clicks = 0

        self.window = tk.Tk()
        self.window.title("Xj9")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        self.window.configure(bg="#222222")

        # Create a frame for the interface
        self.frame = tk.Frame(self.window, bg="#444444", bd=5)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create the Start button
        self.start_button = tk.Button(
            self.frame, text="Start", command=self.start_click_bot, bg="#008CBA", fg="#FFFFFF")
        self.start_button.pack(pady=10)

        # Create the Close button
        self.close_button = tk.Button(
            self.frame, text="Close", command=self.close_click_bot, bg="#BA0000", fg="#FFFFFF")
        self.close_button.pack(pady=10)

        # Create the Pause button
        self.pause_button = tk.Button(
            self.frame, text="Pause", command=self.pause_click_bot, bg="#FDB813", fg="#000000", state=tk.DISABLED)
        self.pause_button.pack(pady=10)

        # Create the click counter label
        self.click_counter_label = tk.Label(
            self.frame, text="Clicks: 0", fg="#FFFFFF", bg="#444444", font=("Arial", 14))
        self.click_counter_label.pack(pady=10)

        # Add a note to let the user know how to start and stop the bot
        self.note_label = tk.Label(
            self.frame, text="Press Spacebar to Start, P to Pause and S to Close the ClickBoTT.", fg="#FFFFFF", bg="#444444", font=("Arial", 10))
        self.note_label.pack(pady=10)

        # Add a theme to the interface
        style = self.window.tk.call("ttk::style", "theme", "use", "clam")

        # Bind hotkey for start
        keyboard.add_hotkey("spacebar", self.start_click_bot)

        # Bind hotkey for pause
        keyboard.add_hotkey("p", self.pause_click_bot)

        # Bind hotkey for close
        keyboard.add_hotkey("s", self.close_click_bot)

    def start_click_bot(self):
        if not self.is_running:
            self.is_running = True
            self.pause_button.config(state=tk.NORMAL)
            self.thread = threading.Thread(target=self.click_bot)
            self.thread.start()

    def close_click_bot(self):
        self.is_running = False
        self.window.destroy()

    def pause_click_bot(self):
        if self.is_paused:
            self.is_paused = False
            self.pause_button.config(text="Pause")
        else:
            self.is_paused = True
            self.pause_button.config(text="Paused")

    def click_bot(self):
        while self.is_running:
            if not self.is_paused and pyautogui.position() == pyautogui.position():
                pyautogui.click()
                self.total_clicks += 1
                clicks_str = f"{self.total_clicks:,}"
                self.click_counter_label.config(text=f"Clicks: {clicks_str}")
                time.sleep(1 / 40)
            else:
                time.sleep(0.1)

    def run(self):
        self.window.mainloop()





if __name__ == "__main__":
    ClickBotGUI().run()
