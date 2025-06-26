# Logic of the App

class CalculatorLogic:
    def process_input(self, current_text, clicked_button_text):
        try:
            if clicked_button_text == "=":
                expression = current_text.replace("÷", "/").replace("×", "*")
                result = eval(expression)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                return str(result)
            elif clicked_button_text == "C":
                return ""
            elif clicked_button_text == "%":
                return str(float(current_text) / 100)
            elif clicked_button_text == "±":
                return str(-float(current_text))
            else:
                return current_text + clicked_button_text
        except Exception:
            return "Error"