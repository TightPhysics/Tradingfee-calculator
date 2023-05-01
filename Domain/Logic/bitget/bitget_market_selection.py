
def select_option_by_name(name):
    if name == "Futures":
        print("Futures selected")
    elif name == "Spot":
        print("spot selected")
    elif name == "Custom":
        print("done")
        return True
    else:
        print("nothing selected")


def is_custom_selected(self):
    if self.app_instance.gui_events.bitget_frame_checkbox_event:
        option = ["Test", "Test"]
    else:
        option = ["Custom"]
    return option
