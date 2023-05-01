import Domain.Logic.frame_logic as frame_logic
import Domain.Interfaces.guiconst as const
from Domain.Logic.bitget.bitget_calculation import calculate


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
        elif name == const.market[0]:
            print("Futures selected")
        elif name == const.market[1]:
            print("spot selected")
        elif name == const.market[2]:
            self.add_fee_widgets()
        else:
            print("nothing selected")

    def remove_fee_widgets(self):
        self.app_instance.bitget_frame.entry3.grid_remove()
        self.app_instance.bitget_frame.label3.grid_remove()

    def add_fee_widgets(self):
        self.app_instance.bitget_frame.label3.grid()
        self.app_instance.bitget_frame.entry3.grid()

    def ok_button_event(self):
        print(calculate(
                entry=self.app_instance.bitget_frame.entry1.get(),
                amount=self.app_instance.bitget_frame.entry2.get(),
                fee=self.app_instance.bitget_frame.entry3.get(),
                market=self.app_instance.bitget_frame.optionMenu.get()))

        self.app_instance.bitget_frame.label5.grid_remove()
        self.app_instance.bitget_frame.label5.configure(
            text=calculate(
                entry=self.app_instance.bitget_frame.entry1.get(),
                amount=self.app_instance.bitget_frame.entry2.get(),
                fee=self.app_instance.bitget_frame.entry3.get(),
                market=self.app_instance.bitget_frame.optionMenu.get()))
        self.app_instance.bitget_frame.label5.grid()

    def calculation_event(self):
        self.app_instance.bitget_frame.label5.config(text=calculate(
            entry=self.app_instance.bitget_frame.entry1.get(),
            amount=self.app_instance.bitget_frame.entry2.get(),
            fee=self.app_instance.bitget_frame.entry3.get(),
            market=self.app_instance.bitget_frame.optionMenu.get()))
