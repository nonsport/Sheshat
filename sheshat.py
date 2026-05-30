import os
import sys
import asyncio
from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.tree import Tree
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style as PTStyle

from core.loader import load_modules
from core.logger import log_info, log_success, log_error, log_warning

console = Console(style="white")

BANNER = """
┌─────────────────────────────────────────────┐
│                 S E S H A T                 │
└─────────────────────────────────────────────┘

███████╗███████╗███████╗██╗  ██╗ █████╗ ████████╗
██╔════╝██╔════╝██╔════╝██║  ██║██╔══██╗╚══██╔══╝
███████╗█████╗  ███████╗███████║███████║   ██║
╚════██║██╔══╝  ╚════██║██╔══██║██╔══██║   ██║
███████║███████╗███████║██║  ██║██║  ██║   ██║
╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
"""

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def draw_header():
    clear_screen()
    console.print(Align.center(f"[bold white]{BANNER}[/bold white]"))
    console.print(Align.center("[bold white]Advanced OSINT Architecture[/bold white]\n"))

def build_result_tree(data, tree=None, name="Result"):
    if tree is None:
        tree = Tree(f"[bold white]❖ {name} ❖[/bold white]", guide_style="white")
    
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                subtree = tree.add(f"[bold white]{k}[/bold white]")
                build_result_tree(v, subtree, k)
            else:
                tree.add(f"[bold white]{k}:[/bold white] [white]{v}[/white]")
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                subtree = tree.add("[bold white]>[/bold white]")
                build_result_tree(item, subtree, "Item")
            else:
                tree.add(f"[white]{item}[/white]")
    else:
        tree.add(f"[white]{data}[/white]")
    return tree

async def run_module_ui(coro, module_name):
    console.print(Align.center(f"\n[bold white] Выполнение: {module_name} [/bold white]"))
    
    with console.status("[bold white]Анализ данных...[/bold white]", spinner="dots", spinner_style="white"):
        try:
            results = await coro
        except Exception as e:
            log_error(f"Критическая ошибка модуля: {e}")
            return
        
    for mod_key, data in results.items():
        is_error = "error" in str(data).lower()
        if is_error:
            log_warning("В результатах обнаружена ошибка.")
            
        tree = build_result_tree(data, name=mod_key)
        panel = Panel(tree, title=f"[bold white]{mod_key}[/bold white]", border_style="white", expand=False)
        console.print(Align.center(panel))
        console.print()
    log_success("Модуль завершил работу.")

def display_tree_menu(categories):
    mapping = {}
    cat_idx = 1
    
    for cat_name, modules in categories.items():
        console.print(f"[bold white]{cat_idx}. {cat_name}[/bold white]")
        mod_idx = 1
        total_mods = len(modules)
        
        for mod in modules:
            prefix = "└─" if mod_idx == total_mods else "├─"
            cmd_key = f"{cat_idx}.{mod_idx}"
            console.print(f"   [white]{prefix} {cmd_key} {mod['name']}[/white]")
            mapping[cmd_key] = mod
            mod_idx += 1
            
        console.print("")
        cat_idx += 1
        
    console.print("[bold white]0. Exit[/bold white]\n")
    return mapping

async def main():
    categories = load_modules()
    
    style = PTStyle.from_dict({
        'prompt': 'ansiwhite bold',
        'input': 'ansiwhite'
    })
    session = PromptSession(style=style)

    while True:
        draw_header()
        mapping = display_tree_menu(categories)

        try:
            choice = await session.prompt_async("➤ Seshat > ")
            choice = choice.strip()
        except (EOFError, KeyboardInterrupt):
            break

        if choice == '0':
            clear_screen()
            log_info("Завершение работы Seshat...")
            break
            
        if choice in mapping:
            module = mapping[choice]
            target = None
            
            if module["prompt"]:
                target = await session.prompt_async(f"❖ {module['prompt']}")
                
            task = module["execute"](target) if target else module["execute"]()
            await run_module_ui(task, module["name"])
            
            await session.prompt_async("\n[ Enter для возврата в меню ]")
        elif choice != "":
            log_error("Неверная команда. Нажмите Enter.")
            await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n")
        log_warning("Прервано пользователем. Выход...")
