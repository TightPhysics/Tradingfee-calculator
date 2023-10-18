import Domain.Interfaces.guiconst as const
import Domain.Logic.frame_logic as frame_logic
from Domain.Logic.bitget.bitget_calculation import calculate


class BitgetUseCase:
    def __init__(self, app_instance):
        self.frame_logic = frame_logic
        self.app_instance = app_instance

    def bitget_navigation_button_event(self):
        self.frame_logic.select_frame_by_name(self=self.app_instance, name=const.navigationButtonText2, const=const)

    def ok_button_event(self):
        try:
            self.app_instance.bitget_frame.label5.grid_remove()
            self.app_instance.bitget_frame.label5.configure(
                text=calculate(
                    entry=self.app_instance.bitget_frame.entry1.get(),
                    amount=self.app_instance.bitget_frame.entry2.get(),
                    fee=self.app_instance.bitget_frame.entry3.get(),
                    market=self.app_instance.bitget_frame.optionMenu.get(),
                    mkortk=self.app_instance.bitget_frame.optionMenu2.get()
                ))
            self.app_instance.bitget_frame.label5.grid()
        except ValueError:
            self.value_error_handling()

    def clipboard_event(self):
        self.app_instance.bitget_frame.clipboard_clear()
        string = self.app_instance.bitget_frame.label5.cget("text")
        self.app_instance.bitget_frame.clipboard_append(string=str(string))

    def value_error_handling(self):

        self.app_instance.bitget_frame.label6.configure(
            text="PLEASE FILL ALL FIELDS",
            text_color="red"
        )
        self.app_instance.bitget_frame.label6.grid()
        self.app_instance.after(2000, lambda: self.app_instance.bitget_frame.label6.grid_remove())

