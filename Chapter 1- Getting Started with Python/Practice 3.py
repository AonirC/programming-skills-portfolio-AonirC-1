string = " 1. 2. 3. 4. 5. 6. 7. 8. 9."

regex_pattern = r"[,.]"

import re
print("\n".join(re.split(regex_pattern, string))) 