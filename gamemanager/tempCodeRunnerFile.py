def play_sound(self, name):
        if self.is_enable_sound():
            # print(f"Play sound: {name}")
            self.get_sound(name).play()
        else:
            print(f"Sound is disabled")