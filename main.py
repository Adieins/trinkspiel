from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import gamelogic2 as game


class GameScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.players = []
        self.custom_tasks = []
        self.game_tasks = []
        self.current_round = 0

    def start_game(self):
        player_input = self.ids.player_input.text.strip()
        if not player_input:
            self.ids.task_label.text = "⚠️ Bitte mindestens einen Spielernamen eingeben!"
            return

        self.players = [p.strip() for p in player_input.split(",") if p.strip()]
        if not self.players:
            self.ids.task_label.text = "⚠️ Keine gültigen Spielernamen!"
            return

        self.custom_tasks = []
        self._ask_custom_task(0)

    def _ask_custom_task(self, index):
        if index >= len(self.players):
            self._build_game_tasks()
            return

        player = self.players[index]
        content = BoxLayout(orientation="vertical", spacing=10, padding=10)
        input_field = TextInput(
            hint_text=f"{player}, gib eine eigene Aufgabe ein:",
            multiline=False,
            size_hint_y=None,
            height=40,
            padding=10,
            background_color=(0.95,0.95,0.95,1),
            foreground_color=(0,0,0,1)
        )
        content.add_widget(input_field)

        btn = Button(
            text="OK",
            size_hint_y=None,
            height=50,
            background_color=(0.2,0.6,0.9,1),
            color=(1,1,1,1),
            bold=True
        )
        content.add_widget(btn)

        popup = Popup(
            title=f"Custom Task von {player}",
            content=content,
            size_hint=(0.8, 0.4),
            auto_dismiss=False
        )

        def save_task(instance):
            task = input_field.text.strip()
            if task:
                self.custom_tasks.append(task)
            popup.dismiss()
            self._ask_custom_task(index + 1)

        btn.bind(on_press=save_task)
        popup.open()

    def _build_game_tasks(self):
        try:
            self.game_tasks = game.create_game_tasks(self.custom_tasks, total=30)
        except Exception as e:
            self.ids.task_label.text = f"Fehler: {e}"
            return
        self.current_round = 0
        self.ids.task_label.text = "✅ Spiel gestartet! Drücke 'Nächste Aufgabe'."
        self.ids.next_button.disabled = False

    def show_next_task(self):
        if self.current_round >= len(self.game_tasks):
            self.ids.task_label.text = "🎉 Spiel vorbei!"
            self.ids.next_button.disabled = True
            return

        template = self.game_tasks[self.current_round]
        task = game.replace_placeholders(template, self.players)
        self.ids.task_label.text = f"Runde {self.current_round+1}:\n\n{task}"
        self.current_round += 1


class DrinkingGameApp(App):
    def build(self):
        return GameScreen()


if __name__ == "__main__":
    DrinkingGameApp().run()
