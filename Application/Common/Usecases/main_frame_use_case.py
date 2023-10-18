import Domain.Interfaces.guiconst as const


class FrameUseCase:
    def __init__(self, app_instance):
        self.app_instance = app_instance

    def select_option_by_name(self, name):
        if name is not const.market[2]:
            self.remove_fee_widgets()
            if not self.app_instance.bitget_frame.optionMenu2.grid_info():
                self.app_instance.bitget_frame.optionMenu2.grid()

            if name == const.market[0]:
                pass
                print("Futures selected")
            elif name == const.market[1]:
                pass
                print("spot selected")

        else:
            self.add_fee_widgets()
            self.app_instance.bitget_frame.optionMenu2.grid_remove()

    def remove_fee_widgets(self):
        self.app_instance.bitget_frame.entry3.grid_remove()
        self.app_instance.bitget_frame.label3.grid_remove()

    def add_fee_widgets(self):
        self.app_instance.bitget_frame.label3.grid()
        self.app_instance.bitget_frame.entry3.grid()
