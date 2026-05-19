# ANSI color codes
RESET = '\033[0m'
BOLD_BRIGHT_RED = '\033[1;31m'  # Bold (1) bright red (31)
YELLOW_BACKGROUND = '\033[43m'  # Yellow background (43)

print(f"{BOLD_BRIGHT_RED}This text is bold and red.{RESET}")
print(f"{YELLOW_BACKGROUND}This text has a yellow background.{RESET}")
print(f"{BOLD_BRIGHT_RED}{YELLOW_BACKGROUND}This text is bold red on a yellow background.{RESET}")
