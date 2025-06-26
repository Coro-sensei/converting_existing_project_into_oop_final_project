# Logic of the App
import re
class CalculatorLogic:

    def __init__(self):
        self.valid_chars_pattern = re.compile(r'^[\d+\-*/.%() ]*$')

    def process_input(self, current_text: str, btn: str) -> str:
        try:
            if btn == "=":
                expr = current_text.replace("÷", "/").replace("×", "*")
                result = eval(expr)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                return str(result)
            elif btn == "C":
                return ""
            elif btn == "%":
                return str(float(current_text) / 100)
            elif btn == "±":
                return str(-float(current_text))
            else:                           # digits, dot, operators
                return current_text + btn
        except Exception:
            return "Error"
    def _is_number(self, text):
        