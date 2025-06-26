# Logic of the App
import re
class CalculatorLogic:

    def __init__(self):
        self.valid_chars_pattern = re.compile(r'^[\d+\-*/.%() ]*$')

    def process_input(self, current_text: str, btn: str) -> str:
        try:
            if btn == "=":
                expr = current_text.replace("÷", "/").replace("×", "*")
                expr = expr.strip()

                # ✅ Validate expression: only digits and valid math characters
                if not self.valid_chars_pattern.fullmatch(expr):
                    return "Error"

                result = eval(expr)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                return str(result)

            elif btn == "C":
                return ""
            elif btn == "%":
                # only apply percent if the text is a valid number
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
