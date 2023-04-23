import os

import customtkinter
from PIL import Image

import Domain.Interfaces.guiconst as const
import Domain.Logic.frame_logic as frame_logic
from Presentation.Ui.Frames.binance_frame import BinanceFrame
from Presentation.Ui.Frames.bitget_frame import bitget_frame
from Presentation.Ui.Frames.okx_frame import okx_frame
from Presentation.Ui.Frames.NavigationFrame.navigation_frame import NavigationFrame
from Application.Common.Events.gui_events import GuiEvent


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.gui_events = GuiEvent(app_instance=self)

        self.title(const.titleText)
        self.geometry(const.geometry)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join("test_images")

        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")),
                                                       size=const.image_largesize)
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                                       size=const.image_smallsize)
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 size=const.image_smallsize)
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
                                                 size=const.image_smallsize)
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=const.image_smallsize)

        # create navigation frame
        NavigationFrame(app_instance=self)

        # create home frame
        BinanceFrame(app_instance=self)

        # create second frame
        bitget_frame(self=self, customtkinter=customtkinter, const=const)

        # create third frame
        okx_frame(self=self, customtkinter=customtkinter, const=const)

        # select default frame
        frame_logic.select_frame_by_name(self=self, const=const, name=const.navigationButtons[0])

        self.gui_events.dynamic_button_events()
