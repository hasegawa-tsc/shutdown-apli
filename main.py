import customtkinter as ctk
import os
import subprocess
import sys

class ShutdownApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Shutdown Timer")
        self.geometry("400x280")
        self.resizable(False, False)

        # Appearance
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        # UI Elements
        self.label_title = ctk.CTkLabel(self, text="シャットダウンタイマー", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=(20, 10))

        self.label_time = ctk.CTkLabel(self, text="設定時間: 60 分", font=ctk.CTkFont(size=16))
        self.label_time.pack(pady=10)

        self.slider = ctk.CTkSlider(self, from_=1, to=120, number_of_steps=119, command=self.slider_event)
        self.slider.set(60)
        self.slider.pack(pady=10, padx=20, fill="x")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20)

        self.execute_button = ctk.CTkButton(self.button_frame, text="実行", command=self.execute_shutdown, fg_color="#2c3e50", hover_color="#34495e")
        self.execute_button.grid(row=0, column=0, padx=10)

        self.cancel_button = ctk.CTkButton(self.button_frame, text="キャンセル", command=self.cancel_shutdown, fg_color="#c0392b", hover_color="#e74c3c")
        self.cancel_button.grid(row=0, column=1, padx=10)

    def slider_event(self, value):
        self.label_time.configure(text=f"設定時間: {int(value)} 分")

    def execute_shutdown(self):
        minutes = int(self.slider.get())
        seconds = minutes * 60
        try:
            # Windows shutdown command
            subprocess.run(["shutdown", "/s", "/t", str(seconds)], check=True)
            self.label_time.configure(text=f"{minutes} 分後にシャットダウンします", text_color="#27ae60")
        except subprocess.CalledProcessError as e:
            self.label_time.configure(text="エラーが発生しました", text_color="#c0392b")

    def cancel_shutdown(self):
        try:
            # Cancel Windows shutdown
            subprocess.run(["shutdown", "/a"], check=True)
        except subprocess.CalledProcessError:
            # Ignore error if no shutdown is scheduled
            pass
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    app = ShutdownApp()
    app.mainloop()
