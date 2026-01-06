import random
import time
from datetime import datetime
from rich.console import Console
from rich.text import Text
from rich.live import Live

AMOUNT = 84_000_000.06         
YEAR = datetime.now().year      

console = Console()
LINE_WIDTH = 120

# ---------------- HELPERS ----------------

def pause(t=0.5):
    time.sleep(t)

def random_trn():
    return "MAD" + "".join(str(random.randint(0, 9)) for _ in range(14))

def random_api_key():
    chars = "0123456789abcdef"
    parts = [8, 4, 4, 4, 12]
    return "-".join("".join(random.choice(chars) for _ in range(p)) for p in parts)

def random_secret_key():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(random.choice(chars) for _ in range(43))

def green_banner(text):
    # THICK BLACK TEXT ON GREEN
    console.print(f"[bold black on green] {text}!!!!! [/]\n")

def divider():
    # WHITE DIVIDER LINE
    console.print("-" * LINE_WIDTH, style="white")

def inline_progress(label, percent=None):
    if percent is not None:
        box = f" {label} {percent}% "
    else:
        box = f" {label} "

    dots = LINE_WIDTH - len(box)
    left = "-" * (dots // 2)
    right = "-" * (dots - len(left))

    # WHITE LINE + GREEN BOX
    return Text.from_markup(
        f"[white]{left}[/]"
        f"[bold black on green]{box}[/]"
        f"[white]{right}[/]"
    )

def animated_progress(label):
    with Live(console=console, refresh_per_second=20) as live:
        for i in range(0, 101, 5):
            live.update(inline_progress(label, i))
            time.sleep(0.05)

# ---------------- MAIN ----------------

def run():
    console.clear()

    # CONNECTED
    green_banner("CONNECTED")
    console.print(f"[white]{YEAR}[/white]\n")

    trn = random_trn()
    route = f"external_crypto_server/download/usdt/convert/{trn}"

    console.print(route)
    console.print(f"TRN               : {trn}")
    console.print("Client account name : STE TRADIMI S.A.R.L")

    formatted_amount = f"${AMOUNT:,.2f} #DOLLARS#"
    console.print(f"Amount              : [white]{formatted_amount}[/white]\n")

    divider()
    animated_progress("DOWNLOADING")
    divider()

    console.print("\n[bold black on green] DOWNLOAD COMPLETED!!!!! [/]\n")
    console.print(f"external_crypto_server/usdt/convert/{trn}\n")

    divider()
    animated_progress("CONVERTING")
    divider()

    console.print("\n[bold black on green] CONVERT COMPLETED!!!!! [/]\n")
    console.print(f"[white]{YEAR}[/white]\n")

    ip = "203.52.115.115"

    console.print(f"IP LINK            : [white]{ip}[/white]")
    console.print(f"[white]API-KEY            : {random_api_key()}[/white]")
    console.print(f"SECRET KEY         : {random_secret_key()}")
    console.print(
        "[white]Wallet Address (USDT ERC 20) : "
        "0x4B70******************************[/white]\n"
    )

    console.print(f"[white]CRYPTO IP LINK {ip}[/white]")
    console.print(f"[white]{YEAR}[/white]")

# ---------------- ENTRY ----------------

if __name__ == "__main__":
    run()
