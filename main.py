import os
from PIL import Image
import customtkinter
from tkinter.filedialog import asksaveasfile
from tkinter.colorchooser import askcolor

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("QR Code Generator")
        self.geometry(f"{885}x{650}")

        # configure grid layout (4x4)
        self.grid_columnconfigure((0, 1, 2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=0)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Please enter text")
        self.entry.grid(row=0, column=0, columnspan=4, padx=(10, 10), pady=(10, 10), sticky="nsew")

        def generate_qr_code():
            print("generate")

        def save_qr_code():
            print("save")

        self.generate_qr_code_btn = customtkinter.CTkButton(master=self, text="Generate QR Code", fg_color="transparent",
                                                            border_width=2, text_color=("gray10", "#DCE4EE"),
                                                            command=generate_qr_code)

        self.generate_qr_code_btn.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew", columnspan=2)

        self.save_qr_code_btn = customtkinter.CTkButton(master=self, text="Save QR Code", fg_color="transparent",
                                                     border_width=2, text_color=("gray10", "#DCE4EE"),
                                                     command=save_qr_code)

        self.save_qr_code_btn.grid(row=1, column=2, padx=(10, 10), pady=(10, 10), sticky="nsew", columnspan=2)

        # error correction mode
        self.error_correction_mode_frame = customtkinter.CTkFrame(self)
        self.error_correction_mode_frame.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.error_correction_mode_label = customtkinter.CTkLabel(master=self.error_correction_mode_frame, text="Error Correction Mode:")
        self.error_correction_mode_label.grid(row=3, column=0, padx=10, pady=10, sticky="")

        self.error_correction_mode_combobox = customtkinter.CTkComboBox(self.error_correction_mode_frame,
                                                                        width=160,
                                                                        values=["ERROR_CORRECT_L",
                                                                                "ERROR_CORRECT_M",
                                                                                "ERROR_CORRECT_Q",
                                                                                "ERROR_CORRECT_H"])
        self.error_correction_mode_combobox.grid(row=4, column=0, pady=10, padx=20)

        # box size
        self.box_size_frame = customtkinter.CTkFrame(self)
        self.box_size_frame.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.box_size_label = customtkinter.CTkLabel(master=self.box_size_frame, text="Box Size:")
        self.box_size_label.grid(row=3, column=1, padx=10, pady=10, sticky="")

        self.box_size_combobox = customtkinter.CTkComboBox(self.box_size_frame,
                                                                        width=160,
                                                                        values=["100x100",
                                                                                "250x250",
                                                                                "500x500"])
        self.box_size_combobox.grid(row=4, column=1, pady=10, padx=20)

        # border
        self.border_frame = customtkinter.CTkFrame(self)
        self.border_frame.grid(row=2, column=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.border_label = customtkinter.CTkLabel(master=self.border_frame, text="Border:")
        self.border_label.grid(row=3, column=2, padx=10, pady=10, sticky="")

        self.border_combobox = customtkinter.CTkComboBox(self.border_frame,
                                                           width=160,
                                                           values=["4",
                                                                   "8",
                                                                   "12",
                                                                   "16"])
        self.border_combobox.grid(row=4, column=2, pady=10, padx=20)

        # color main frame
        self.color_frame = customtkinter.CTkFrame(self)
        self.color_frame.grid(row=2, column=3, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # fill color label
        self.fill_color_label = customtkinter.CTkLabel(master=self.color_frame, text="Fill Color:")
        self.fill_color_label.grid(row=3, column=3, padx=10, pady=10, sticky="")

        # back color label
        self.back_color_label = customtkinter.CTkLabel(master=self.color_frame, text="Back Color:")
        self.back_color_label.grid(row=4, column=3, padx=10, pady=10, sticky="")

        # fill color pick frame
        self.fill_color_pick_frame = customtkinter.CTkFrame(master=self.color_frame, width=100, height=25)

        def fill_color_pick(event):
            colors = askcolor(title="Choose Fill Color")
            self.fill_color_pick_frame.configure(fg_color=colors[1])

        self.fill_color_pick_frame.bind('<Button-1>', fill_color_pick)
        self.fill_color_pick_frame.grid(row=3, column=4, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # back color pick frame
        self.back_color_pick_frame = customtkinter.CTkFrame(master=self.color_frame, width=100, height=25)

        def back_color_pick(event):
            colors = askcolor(title="Choose Back Color")
            self.back_color_pick_frame.configure(fg_color=colors[1])

        self.back_color_pick_frame.bind('<Button-1>', back_color_pick)
        self.back_color_pick_frame.grid(row=4, column=4, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "empty.png")),
                                                       size=(400, 400))

        self.home_frame_large_image_label = customtkinter.CTkLabel(self, text="",
                                                                   image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=5, column=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

    def save_qr_code(self):
        f = asksaveasfile(initialfile='Untitled.txt',
                          defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

if __name__ == "__main__":
    app = App()
    app.resizable(width=False, height=False)
    app.mainloop()