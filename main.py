
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# هذا الكود يبني واجهة التطبيق
class MyCalculatorApp(App):
    def build(self):
        # 1. التخطيط الرئيسي (عمودي)
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # 2. شاشة العرض (مكان الارقام)
        # readonly=True لمنع ظهور لوحة مفاتيح الهاتف
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)

        # 3. الأزرار (شبكة)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        grid_layout = GridLayout(cols=4, spacing=10)
        
        for row in buttons:
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    font_size=30,
                    background_color=(0.5, 0.5, 0.5, 1) # لون رمادي
                )
                button.bind(on_press=self.on_button_press)
                grid_layout.add_widget(button)

        main_layout.add_widget(grid_layout)

        # 4. زر "يساوي" (كبير في الأسفل)
        equals_btn = Button(
            text="=", 
            size_hint=(1, 0.2), # يأخذ 20% من الارتفاع
            font_size=40,
            background_color=(0, 0.8, 0, 1) # لون أخضر
        )
        equals_btn.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_btn)

        return main_layout

    # دالة التعامل مع ضغط الأزرار
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # مسح الشاشة
            self.solution.text = ""
        else:
            # منع تكرار العمليات الحسابية (مثل ++ أو //)
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            
            new_text = current + button_text
            self.solution.text = new_text
        
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    # دالة حساب النتيجة
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                # دالة eval تحول النص لعملية رياضية
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception:
                self.solution.text = "Error"

if __name__ == "__main__":
    MyCalculatorApp().run()
