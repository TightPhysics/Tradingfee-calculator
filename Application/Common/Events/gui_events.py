import Domain.Logic.frame_logic as frame_logic
import Domain.Interfaces.guiconst as const


class GuiEvent:
    def __init__(self, app_instance):
        super().__init__()
        self.app_instance = app_instance

    # navigation menu events
    def dynamic_button_events(self):
        for i in const.navigationButtons:
            frame_logic.select_frame_by_name(self=self.app_instance, const=const, name=i)

    def binance_navigation_button_event(self):
        frame_logic.select_frame_by_name(self=self.app_instance, const=const, name=const.navigationButtonText1)

    def bitget_navigation_button_event(self):
        frame_logic.select_frame_by_name(self=self.app_instance, const=const, name=const.navigationButtonText2)

    def okx_navigation_button_event(self):
        frame_logic.select_frame_by_name(self=self.app_instance, const=const, name=const.navigationButtonText3)

    # bitget_frame events
    def select_option_by_name(self, name):
        if name is not const.market[2]:
            self.remove_fee_widgets()
        elif name == "Futures":
            print("Futures selected")
        elif name == "Spot":
            print("spot selected")
        elif name == "Custom":
            print("done")
            self.add_fee_widgets()
        else:
            print("nothing selected")

    def remove_fee_widgets(self):
        self.app_instance.bitget_frame.entry3.grid_remove()
        self.app_instance.bitget_frame.label3.grid_remove()

    def add_fee_widgets(self):
        self.app_instance.bitget_frame.label3.grid()
        self.app_instance.bitget_frame.entry3.grid()
