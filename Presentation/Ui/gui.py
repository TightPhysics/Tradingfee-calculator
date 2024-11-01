import os

import customtkinter
from PIL import Image

import Domain.Interfaces.guiconst as const
from Application.Common.Events.gui_events import GuiEvent
from Presentation.Ui.Frames.NavigationFrame.navigation_frame import NavigationFrame
from Presentation.Ui.Frames.binance_frame import BinanceFrame
from Presentation.Ui.Frames.bitget_frame import BitgetFrame
from Presentation.Ui.Frames.okx_frame import OKXFrame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.gui_events = GuiEvent(app_instance=self)

        self.title(const.titleText)
        self.geometry(const.geometry)
        self.resizable(width=False, height=False)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        self.image_path = os.path.join("images")

        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(
            self.image_path, "large_image_3_binance_edit.png")), size=const.image_largesize)
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(
            self.image_path, "image_icon_light.png")), size=const.image_smallsize)

        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "home_light.png")),
                                                 size=const.image_smallsize)
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "chat_light.png")),
                                                 size=const.image_smallsize)
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(self.image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(self.image_path, "add_user_light.png")), size=const.image_smallsize)

        self.copy_symbol_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(self.image_path, "copy_symbol_dark.png")),
            dark_image=Image.open(os.path.join(self.image_path, "copy_symbol_white.png")), size=const.image_smallsize
        )

        # create navigation frame
        NavigationFrame(app_instance=self)

        # create home frame
        BinanceFrame(app_instance=self)

        # create second frame
        BitgetFrame(app_instance=self)

        # create third frame
        OKXFrame(app_instance=self)

        self.gui_events.dynamic_button_events()
