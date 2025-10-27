
import asyncio
import threading
import tkinter as tk
from tkinter import font, messagebox
from kasa import SmartPlug


DEFAULT_PLUG_IP = "100.86.5.14"

# run async function in a background 

def run_coro_in_thread(coro, callback=None, err_callback=None):
    def _target():
        try:
            result = asyncio.run(coro)
            if callback:
                app_root.after(0, lambda: callback(result))
        except Exception as e:
            if err_callback:
                app_root.after(0, lambda: err_callback(e))
            else:
                app_root.after(0, lambda: messagebox.showerror("Error", str(e)))
    threading.Thread(target=_target, daemon=True).start()


# Async Kasa controls

async def get_plug_status(ip):
    plug = SmartPlug(ip)
    await plug.update()
    return plug.is_on, plug.alias

async def turn_plug_on(ip):
    plug = SmartPlug(ip)
    await plug.update()
    await plug.turn_on()
    await plug.update()
    return plug.is_on, plug.alias

async def turn_plug_off(ip):
    plug = SmartPlug(ip)
    await plug.update()
    await plug.turn_off()
    await plug.update()
    return plug.is_on, plug.alias


# GUI handlers

def update_status_label(result):
    is_on, alias = result
    state = "ON" if is_on else "OFF"
    status_var.set(f"{alias} — {state}")
    status_label.config(bg="#A8E6A3" if is_on else "#F3A8A8")

def handle_error(e):
    status_var.set("Error")
    status_label.config(bg="#F7C6C6")
    messagebox.showerror("Kasa Error", str(e))

def refresh_status():
    ip = ip_var.get().strip()
    status_var.set("Checking...")
    status_label.config(bg="#FFF3BF")
    run_coro_in_thread(get_plug_status(ip), callback=update_status_label, err_callback=handle_error)

def do_turn_on():
    ip = ip_var.get().strip()
    status_var.set("Turning ON...")
    status_label.config(bg="#FFF3BF")
    run_coro_in_thread(turn_plug_on(ip), callback=update_status_label, err_callback=handle_error)

def do_turn_off():
    ip = ip_var.get().strip()
    status_var.set("Turning OFF...")
    status_label.config(bg="#FFF3BF")
    run_coro_in_thread(turn_plug_off(ip), callback=update_status_label, err_callback=handle_error)

def do_toggle():
    ip = ip_var.get().strip()
    status_var.set("Toggling...")
    status_label.config(bg="#FFF3BF")
    def after_status(result):
        is_on, _ = result
        if is_on:
            run_coro_in_thread(turn_plug_off(ip), callback=update_status_label, err_callback=handle_error)
        else:
            run_coro_in_thread(turn_plug_on(ip), callback=update_status_label, err_callback=handle_error)
    run_coro_in_thread(get_plug_status(ip), callback=after_status, err_callback=handle_error)

# Build touchscreen GUI

app_root = tk.Tk()
app_root.title("Kasa Touch Control")
app_root.geometry("480x320")   # Typical Pi touchscreen size
app_root.configure(bg="#FFFFFF")
app_root.resizable(False, False)

# Fonts
title_font = font.Font(size=18, weight="bold")
big_font = font.Font(size=16, weight="bold")
small_font = font.Font(size=12)

# Title
title = tk.Label(app_root, text="Smart Plug Control", font=title_font, bg="#FFFFFF")
title.pack(pady=(8, 4))

# IP entry
ip_frame = tk.Frame(app_root, bg="#FFFFFF")
ip_frame.pack(pady=(0, 8))
tk.Label(ip_frame, text="Plug IP:", font=small_font, bg="#FFFFFF").pack(side="left", padx=(4, 6))
ip_var = tk.StringVar(value=DEFAULT_PLUG_IP)
ip_entry = tk.Entry(ip_frame, textvariable=ip_var, font=small_font, width=16)
ip_entry.pack(side="left")
refresh_btn = tk.Button(ip_frame, text="Refresh", font=small_font, command=refresh_status)
refresh_btn.pack(side="left", padx=6)

# Status
status_var = tk.StringVar(value="Unknown")
status_label = tk.Label(app_root, textvariable=status_var, font=big_font, width=28, height=2, bg="#FFF3BF")
status_label.pack(pady=(6, 10), padx=10)

# Buttons
btn_frame = tk.Frame(app_root, bg="#FFFFFF")
btn_frame.pack(pady=6)
on_btn = tk.Button(btn_frame, text="TURN ON", font=big_font, width=10, height=2, command=do_turn_on)
on_btn.grid(row=0, column=0, padx=6, pady=6)
off_btn = tk.Button(btn_frame, text="TURN OFF", font=big_font, width=10, height=2, command=do_turn_off)
off_btn.grid(row=0, column=1, padx=6, pady=6)
toggle_btn = tk.Button(app_root, text="TOGGLE", font=big_font, width=34, height=2, command=do_toggle)
toggle_btn.pack(pady=(8, 6))

# Footer
help_label = tk.Label(app_root, text="Tip: Change IP if your plug address changes.", font=small_font, bg="#FFFFFF")
help_label.pack(side="bottom", pady=(6, 10))

# Auto-refresh on start
app_root.after(200, refresh_status)

app_root.mainloop()
