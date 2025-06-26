# Logic of the App
import re
class CalculatorLogic:

    def __init__(self):
        self.valid_chars_pattern = re.compile(r'^[\d+\-*/.%() ]*$')

    def process_input(self, current_text: str, btn: str) -> str:
        try:
            if btn == "=":
                expression = current_text.replace("÷", "/").replace("×", "*")
                expression = expression.strip()

                if not self.valid_chars_pattern.fullmatch(expression):
                    return "Error"

                result = eval(expression)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                return str(result)

            elif btn == "C":
                return ""
            elif btn == "%":
                if self._is_number(current_text):
                    return str(float(current_text) / 100)
                return "Error"
            elif btn == "±":
                if self._is_number(current_text):
                    return str(-float(current_text))
                return "Error"
            else:
                return current_text + btn
        except Exception:
            return "Error"
    def _is_number(self, text):
        try:
            float(text)
            return True
        except ValueError:
            return False