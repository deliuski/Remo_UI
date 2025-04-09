import qrcode

from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame


# Define paths
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\tmp\Documents\Python folder\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class App:
    def __init__(self, root):
        self.root = root
        root.geometry("800x480")
        root.configure(bg="#FFFFFF")
        root.resizable(False, False)

        self.container = Frame(root)
        self.container.pack(fill="both", expand=True)

        self.startPage = Frame(self.container, bg="#FFFFFF")
        self.mainPage = Frame(self.container, bg="#D9D9D9")
        self.lastPage = Frame(self.container, bg="#FFFFFF")

        for page in (self.startPage, self.mainPage, self.lastPage):
            page.place(x=0, y=0, relwidth=1, relheight=1)

        self.setup_start_page()
        self.setup_main_page()
        self.setup_last_page()

        self.startPage.tkraise()

    def setup_start_page(self):
        canvas = Canvas(self.startPage, bg="#FFFFFF", height=480, width=800, bd=0, highlightthickness=0)
        canvas.place(x=0, y=0)

        image_image_0 = PhotoImage(file=relative_to_assets("image_0.png"))
        canvas.create_image(400.0, 144.0, image=image_image_0)
        self.startPage.image_image_0 = image_image_0

        button_image_0 = PhotoImage(file=relative_to_assets("button_0.png"))
        button_0 = Button(
            self.startPage,
            image=button_image_0,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_main_page,
            relief="flat"
        )
        button_0.place(x=267.0, y=300.0, width=265.0, height=74.0)
        self.startPage.button_image_0 = button_image_0

    def setup_main_page(self):
        canvas = Canvas(
            self.mainPage,
            bg="#D9D9D9",
            height=480,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        image_files = [f"image_{i}.png" for i in range(1, 11)]
        self.main_images = [PhotoImage(file=relative_to_assets(f)) for f in image_files]

        positions = [
            (670, 240), (641, 139), (740, 139), (641, 96), (740, 96),
            (607, 285), (607, 211), (729, 285), (729, 211), (665, 155)
        ]

        for img, (x, y) in zip(self.main_images, positions):
            canvas.create_image(x, y, image=img)

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.mainPage,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_last_page,
            relief="flat"
        )
        button_1.place(x=568.0, y=412.0, width=195.0, height=38.0)
        self.mainPage.button_image_1 = button_image_1

        text_data = [
            (604, 88, "0", "#FFFFFF"), (700, 88, "0", "#434343"),
            (700, 131, "0", "#434343"), (681, 277, "0", "#434343"),
            (681, 204, "0", "#434343"), (604, 131, "0", "#FFFFFF"),
            (560, 203, "0", "#FFFFFF"), (560, 277, "0", "#FFFFFF")
        ]

        for x, y, text, color in text_data:
            canvas.create_text(x, y, anchor="nw", text=text, fill=color, font=("Inter", 15 * -1))

    def setup_last_page(self):
        canvas = Canvas(
            self.lastPage,
            bg="#FFFFFF",
            height=480,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        data = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="#056630", back_color="white")

        qr_code_path = OUTPUT_PATH / "assets" /"frame0" / "qr_code.png"
        qr_code_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(qr_code_path)

        image_image_11 = PhotoImage(file=relative_to_assets("qr_code.png"))
        canvas.create_image(250.0, 279.0, image=image_image_11)
        self.lastPage.image_image_11 = image_image_11

        canvas.create_text(199.0, 26.0, anchor="nw", text="Амжилттай ангиллаа", fill="#056630", font=("Inter Bold", 36 * -1))
        canvas.create_text(199.0, 102.0, anchor="nw", text="QR CODE", fill="#606060", font=("Inter Bold", 20 * -1))
        canvas.create_text(460.0, 129.0, anchor="nw", text="Хуванцар\n\nШил\n\nЛааз\n\nНийт", fill="#606060", font=("Inter Bold", 16 * -1))

        image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
        canvas.create_image(624.0, 111.0, image=image_image_12)
        self.lastPage.image_image_12 = image_image_12

        score_coords = [(572, 132), (632, 132), (572, 167), (632, 167), (572, 205), (632, 205), (572, 243), (632, 243)]
        for x, y in score_coords:
            canvas.create_text(x, y, anchor="nw", text="0", fill="#242424", font=("Inter Bold", 12 * -1))

        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.lastPage,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_start_page,
            relief="flat"
        )
        button_2.place(x=491.0, y=376.0, width=183.0, height=45.0)
        self.lastPage.button_image_2 = button_image_2

    def show_start_page(self):
        self.startPage.tkraise()

    def show_main_page(self):
        self.mainPage.tkraise()

    def show_last_page(self):
        self.lastPage.tkraise()


# Run the app
if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()
